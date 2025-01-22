# python manage.py runserver
# python manage.py shell

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from datacenter.models import (
    Schoolkid,
    Teacher,
    Mark,
    Chastisement,
    Commendation,
    Lesson,
    Subject,
)
import random

COMPLIMENT_LIST = [
    "Молодец!",
    "Отлично!",
    "Прекрасно!",
    "Ты сегодня прыгнул выше головы!",
    "Я вижу, как ты стараешься!",
    "Мы с тобой не зря поработали!",
    "Именно этого я давно ждал от тебя!",
    "Ты меня очень обрадовал!",
]


def name_schoolkid(name):
    try:
        schoolkid = Schoolkid.objects.filter(full_name__contains=name).get()
        return schoolkid
    except ObjectDoesNotExist as e:
        print("Error", e)
    except MultipleObjectsReturned as e:
        print("Error", e)


def fix_marks(schoolkid):
    try:
        point = Mark.objects.filter(schoolkid=schoolkid, points__lte=3).update(
            points=5
        )
        print(point)
        point = Mark.objects.filter(schoolkid=schoolkid, points__lte=3)
        print(point.count())
    except ObjectDoesNotExist as e:
        print("Error", e)
    except MultipleObjectsReturned as e:
        print("Error", e)


def remove_chastisements(schoolkid):
    try:
        comments = Chastisement.objects.filter(schoolkid=schoolkid)
        comments.delete()
        print(comments)
    except ObjectDoesNotExist as e:
        print("Error", e)
    except MultipleObjectsReturned as e:
        print("Error", e)


def change_rating(schoolkid):
    try:
        point = Mark.objects.filter(schoolkid=schoolkid, points__lte=3).update(points=5)
        print(point)
        point = Mark.objects.filter(schoolkid=schoolkid, points__lte=3)
        print(point.count())
    except ObjectDoesNotExist as e:
        print("Error", e)
    except MultipleObjectsReturned as e:
        print("Error", e)


def create_commendation(schoolkid):
    try:
        subjects = Subject.objects.filter(year_of_study=6, title="Музыка")
        lessons = Lesson.objects.filter(
            year_of_study=6, group_letter="А", subject=subjects[0]
        ).order_by("date")
        teachers = Teacher.objects.filter(
            full_name__contains="Селезнева Майя Макаровна"
        )
        dates = lessons[0].date

        compliment = Commendation.objects.create(
            subject=subjects[0],
            schoolkid=schoolkid,
            teacher=teachers[0],
            created=dates,
            text=random.choice(COMPLIMENT_LIST),
        )
    except ObjectDoesNotExist as e:
        print("Error", e)
    except MultipleObjectsReturned as e:
        print("Error", e)


if __name__ == "__main__":
    schoolkid = name_schoolkid(name="Голубев Феофан Владленович")
    fix_marks(schoolkid)
    remove_chastisements(schoolkid)
    change_rating(schoolkid)
    create_commendation(schoolkid)
