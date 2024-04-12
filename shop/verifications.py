from persiantools.jdatetime import JalaliDate

# from Ticket.models import Ticket, Message
import datetime as dt
# from melipayamak import Api
# from zarinpal.models import MPInfo


def getdate(param):
    return str(JalaliDate(param).day) + "-" + str(
        JalaliDate(param).month) + "-" + str(
        JalaliDate(param).year),


def get_time(param):
    delta = dt.timedelta(hours=1)
    max_time = (dt.datetime.combine(dt.date(1, 1, 1), param) + delta).time()
    return str(max_time)


def send_phone_consultation_verifications(data):
    title = 'تایید سفارش مشاوره تلفنی'
    ticket = Ticket(user=data['user'],
                    title=title)
    ticket.save()
    message_content = 'کاربر گرامی \n سفارش شما برای رزرو یک جلسه مشاوره تلفنی با جناب آقا/خانم ' + data[
        'advisor_name'] + ' و تاریخ ' + getdate(data['date'])[0] + ' باموفقیت ثبت شد و مشاور مد نظر حداکثر تا ساعت ' + \
                      get_time(
                          data['end_time']) + ' در تاریخ رزرو شده، با شما تماس میگیرید. \n ' + 'کدرهگیری سفارش : ' + \
                      data['tracking_code']
    message = Message(ticket=ticket,
                      content=message_content,
                      sender=2)
    message.save()

    # send sms to student
    username = MPInfo.objects.get().username
    password = MPInfo.objects.get().password
    api = Api(username, password)
    sms = api.sms()
    to = data['student_phone']
    _from = '50004001142565'
    text = 'سفارش شما ثبت شد و مشاور حداکثر تا ' + get_time(data['end_time']) + ' باشما تماس میگیرد'
    sms.send(to, _from, text)

    # send sms to advisor
    to_advisor = data['advisor_phone']
    text = 'مشاور گرامی \n یک جلسه جدید برای شما رزرو شده است'
    sms.send(to_advisor, _from, text)


def send_online_class_reservation_verification(data):
    title = 'تایید رزرو کلاس آنلاین'
    ticket = Ticket(user=data['user'],
                    title=title)
    ticket.save()
    message_content = 'کاربر گرامی \n سفارش شما برای رزرو ' + data[
        'class_title'] + ' باموفقیت ثبت شد و در زمان برگذاری کلاس میتوانید با مراجعه به بخش کلاس های رزرو شده، به لینک '\
                         'کلاس دسترسی داشته باشید.' + 'کدرهگیری سفارش : ' + data['tracking_code']
    message = Message(ticket=ticket,
                      content=message_content,
                      sender=2)
    message.save()

    # send sms to student
    username = MPInfo.objects.get().username
    password = MPInfo.objects.get().password
    api = Api(username, password)
    sms = api.sms()
    to = data['user'].phone
    _from = '50004001142565'
    text = 'رزرو کلاس شما با موفقیت انجام شد \n لغو=11'
    sms.send(to, _from, text)
