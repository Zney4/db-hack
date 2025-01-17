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


def fix_marks(name):
    try:
        schoolkid = Schoolkid.objects.filter(full_name__contains=name).get()
        point = Mark.objects.filter(schoolkid=schoolkid, points__lte=3).update(points=5)
        print(point)
        point = Mark.objects.filter(schoolkid=schoolkid, points__lte=3)
        print(point.count())
    except NameError as e:
        print("Error", e)

    except ObjectDoesNotExist as e:
        print("Error", e)

    except MultipleObjectsReturned as e:
        print("Error", e)


fix_marks(name="Фролов Иван Григорьевич")


def remove_chastisements(name):
    try:
        schoolkid = Schoolkid.objects.filter(full_name__contains=name).get()
        comments = Chastisement.objects.filter(schoolkid=schoolkid)
        comments.delete()
        print(comments)
    except NameError as e:
        print("Error", e)

    except ObjectDoesNotExist as e:
        print("Error", e)

    except MultipleObjectsReturned as e:
        print("Error", e)

remove_chastisements(name="Голубев Феофан Владленович")


def change_rating(name):
    try:
        schoolkid = Schoolkid.objects.filter(full_name__contains=name).get()
        point = Mark.objects.filter(schoolkid=schoolkid, points__lte=3).update(points=5)
        print(point)
        point = Mark.objects.filter(schoolkid=schoolkid, points__lte=3)
        print(point.count())
    except NameError as e:
        print("Error", e)

    except ObjectDoesNotExist as e:
        print("Error", e)

    except MultipleObjectsReturned as e:
        print("Error", e)

change_rating(name="Голубев Феофан Владленович")


compliment_list = [
    "Молодец!",
    "Отлично!",
    "Прекрасно!",
    "Ты сегодня прыгнул выше головы!",
    "Я вижу, как ты стараешься!",
    "Мы с тобой не зря поработали!",
    "Именно этого я давно ждал от тебя!",
    "Ты меня очень обрадовал!",
]


def create_commendation(compliment_list, name):
    try:
        schoolkid = Schoolkid.objects.filter(full_name__contains=name).get()
        print(schoolkid)
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
            text=random.choice(compliment_list),
        )
    except NameError as e:
        print("Error", e)

    except ObjectDoesNotExist as e:
        print("Error", e)

    except MultipleObjectsReturned as e:
        print("Error", e)

create_commendation(compliment_list, name="Голубев Феофан Владленович")
