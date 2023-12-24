from django.db import models

class Article (models.Model):
    title = models.CharField('Назва', max_length = 256)
    anons = models.CharField('Анонс', max_length = 256)
    full_text = models.TextField('Текст')
    data = models.DateTimeField('Дата')

    def __str__(self):
        return self.title