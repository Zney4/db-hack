# python manage.py runserver
# python manage.py shell

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
    schoolkid = Schoolkid.objects.filter(full_name__contains=name).get()
    point = Mark.objects.filter(schoolkid=schoolkid, points__lte=3).update(points=5)
    print(point)
    point = Mark.objects.filter(schoolkid=schoolkid, points__lte=3)
    print(point.count())


fix_marks(name="Фролов Иван Григорьевич")


def remove_chastisements(name):
    schoolkid = Schoolkid.objects.filter(full_name__contains=name).get()
    point = Mark.objects.filter(schoolkid=schoolkid, points__lte=3).update(points=5)
    print(point)
    point = Mark.objects.filter(schoolkid=schoolkid, points__lte=3)
    print(point.count())
    comments = Chastisement.objects.filter(schoolkid=schoolkid)
    comments.delete()
    print(comments)


remove_chastisements(name="Голубев Феофан Владленович")

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
    schoolkid = Schoolkid.objects.filter(full_name__contains=name).get()
    print(schoolkid)
    subjects = Subject.objects.filter(year_of_study=6, title="Музыка")
    lessons = Lesson.objects.filter(
        year_of_study=6, group_letter="А", subject=subjects[0]
    ).order_by("date")
    teachers = Teacher.objects.filter(full_name__contains="Селезнева Майя Макаровна")
    dates = lessons[0].date

    compliment = Commendation.objects.create(
        subject=subjects[0],
        schoolkid=schoolkid,
        teacher=teachers[0],
        created=dates,
        text=random.choice(compliment_list),
    )


create_commendation(compliment_list, name="Баранова Евфросиния Эльдаровна")
