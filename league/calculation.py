from django.db.models import Sum

from curriculum.models import CurriculumItem
from league.models import LeagueItem
from users.models import Student, Grade
from datetime import datetime, timedelta


def job():
    students = Student.objects.all()

    for student in students:
        items = CurriculumItem.objects.filter(student=student,
                                              date=datetime.now().date() - timedelta(days=1))

        total_time = items.aggregate(Sum('time'))['time__sum']
        total_test = items.aggregate(Sum('test_count'))['test_count__sum']
        total_question = items.aggregate(Sum('question_count'))['question_count__sum']

        grade = Grade.objects.get(id=student.grade.id)

        # calculate time
        if total_time > grade.max_time:
            time_score = 6
        else:
            time_score = 6 * (total_time / grade.max_time)

        # calculate test
        if total_test > grade.max_test:
            test_score = grade.test_score
        else:
            test_score = grade.test_score * (total_test / grade.max_test)

        # calculate question
        if total_question > grade.max_question:
            question_score = 4 - grade.test_score
        else:
            question_score = (4 - grade.test_score) * (total_question / grade.max_question)

        total_score = test_score + question_score + time_score

        league_item = LeagueItem(student=student,
                                 date=datetime.now().date().today(),
                                 rank=0,
                                 score=total_score,
                                 time=str(total_time),
                                 test=total_test,
                                 question=total_question)
        league_item.save()

    all_today_league = LeagueItem.objects.filter(date=datetime.now().date()).order_by('-score')

    rank = 1
    for item in all_today_league:
        item.rank = rank
        item.save()
        rank += 1
