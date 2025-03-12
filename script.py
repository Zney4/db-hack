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
from django.shortcuts import get_object_or_404

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


class CustomExceptionHandler(Exception):
    def __init__(self):
        self.exceptions_to_handle = (
            NameError,
            ObjectDoesNotExist,
            MultipleObjectsReturned,
        )

    def handle(self, func, **kwargs):
        try:
            return func(**kwargs)
        except self.exceptions_to_handle as e:
            self._log_exception(e)
            return None

    @staticmethod
    def _log_exception(exception):
        print(f"Error: {exception}")


handler = CustomExceptionHandler()


def name_schoolkid(name):
    schoolkid = Schoolkid.objects.filter(full_name__contains=name).get()
    print("Найден школьник", schoolkid)
    return schoolkid


schoolkid = handler.handle(name_schoolkid, name="Голубев Феофан Владленович")
print(schoolkid)


def fix_marks(schoolkid):
    point = Mark.objects.filter(schoolkid=schoolkid, points__lte=3).update(points=5)
    print(point)
    point = Mark.objects.filter(schoolkid=schoolkid, points__lte=3)
    print(point.count())


result = handler.handle(fix_marks, schoolkid=schoolkid)
print(result)


def remove_chastisements(schoolkid):
    comments = Chastisement.objects.filter(schoolkid=schoolkid)
    comments.delete()
    print(comments)


result = handler.handle(remove_chastisements, schoolkid=schoolkid)
print(result)


def create_commendation(schoolkid):
    subjects = get_object_or_404(Subject, year_of_study=6, title="Музыка")
    lessons = Lesson.objects.filter(
        year_of_study=6, group_letter="А", subject=subjects
    ).order_by("date")
    teachers = get_object_or_404(
        Teacher, full_name__contains="Селезнева Майя Макаровна"
    )
    if lessons:
        dates = lessons[0].date
        compliment = Commendation.objects.create(
            subject=subjects,
            schoolkid=schoolkid,
            teacher=teachers,
            created=dates,
            text=random.choice(COMPLIMENT_LIST),
        )


result = handler.handle(create_commendation, schoolkid=schoolkid)
print(result)
