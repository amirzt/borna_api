from rest_framework import serializers

from field.models import FieldIntro, FieldAudio, FieldQuestion


class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldAudio
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldQuestion
        fields = '__all__'


class FieldIntroSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField('get_question')
    audios = serializers.SerializerMethodField('get_audios')

    def get_question(self, data):
        qs = FieldQuestion.objects.filter(intro=data)
        return QuestionSerializer(qs, many=True).data

    def get_audios(self, data):
        ad = FieldAudio.objects.filter(intro=data)
        return AudioSerializer(ad, many=True).data

    class Meta:
        model = FieldIntro
        fields = '__all__'
