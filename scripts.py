import random
from datacenter.models import Schoolkid, Lesson, Mark, Chastisement, Commendation
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist


def get_schoolkid(name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=name)
        return schoolkid
    except MultipleObjectsReturned:
        print('Several schoolkids with specified name were found')
        return None
    except ObjectDoesNotExist:
        print('There is no schoolkid with specified name')
        return None


def fix_marks(name):
    schoolkid = get_schoolkid(name)
    if not schoolkid:
        return None
    marks = Mark.objects.filter(schoolkid=schoolkid, points__lt=4)
    for mark in marks:
        mark.points = 5
        mark.save()


def remove_chastisements(name):
    schoolkid = get_schoolkid(name)
    if not schoolkid:
        return None
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    chastisements.delete()


def get_commendation():
    commendation_list = [
        'Молодец!',
        'Отлично!',
        'Хорошо!',
        'Ты меня приятно удивил!',
        'Великолепно!',
        'Очень хороший ответ!',
        'Замечательно!',
        'Так держать!',
        'Я вижу, как ты стараешься!',
        'Талантливо!',
    ]
    return random.choice(commendation_list)


def create_commendation(name, subject):
    schoolkid = get_schoolkid(name)
    if not schoolkid:
        return None
    lesson = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter,
        subject__title=subject
        ).order_by('-date')[0]

    Commendation.objects.create(
        text=get_commendation(),
        created=lesson.date,
        schoolkid=schoolkid,
        subject=lesson.subject,
        teacher=lesson.teacher
        )
