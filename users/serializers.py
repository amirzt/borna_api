import threading

from rest_framework import serializers

from shop.models import Transaction
from users.models import CustomUser, Grade, Field, City, Student, Wallet


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['phone']

    def save(self, **kwargs):
        user = CustomUser(phone=self.validated_data['phone'])
        user.save()
        return user


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


def give_invitation_gift(data):
    student = Student.objects.get(invitation_code=data['invitation_code'])
    transaction = Transaction(user=student.user,
                              price=10000,
                              payment_method=Transaction.PaymentMethod.gift,
                              status=Transaction.Status.SUCCESS,
                              description='جایزه دعوت از دوستان خود')
    transaction.save()
    wallet = Wallet.objects.get(student=student)
    wallet.balance += 10000
    wallet.save()


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['grade', 'field', 'city']

    def save(self, **kwargs):
        student = Student(user=self.context.get('user'),
                          grade=self.validated_data['grade'],
                          field=self.validated_data['field'],
                          city=self.validated_data['city'])
        student.save()

        if 'first_name' in self.validated_data:
            student.first_name = self.validated_data['first_name']
        if 'last_name' in self.validated_data:
            student.last_name = self.validated_data['last_name']
        student.save()

        wallet = Wallet(student=student)
        wallet.save()

        if 'invitation_code' in self.validated_data:
            data = {
                'invitation_code': self.validated_data['invitation_code'],
                'student': student,
            }
            thread = threading.Thread(target=give_invitation_gift,
                                      args=[data])
            thread.setDaemon(True)
            thread.start()

        return student


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['balance']


class GetStudentInfoSerializer(serializers.ModelSerializer):
    grade = GradeSerializer()
    field = FieldSerializer()
    city = CitySerializer()
    user = CustomUserSerializer()
    wallet = serializers.SerializerMethodField('get_wallet')

    @staticmethod
    def get_wallet(self):
        return WalletSerializer(Wallet.objects.get(student=self)).data

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'grade', 'field', 'city', 'student_code', 'id', 'user', 'wallet',
                  'invitation_code']
