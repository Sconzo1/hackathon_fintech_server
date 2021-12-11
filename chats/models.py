from django.contrib.auth import get_user_model
from django.db import models


# Reference tables

class Chat(models.Model):
    id_from_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='from_user',
                                     verbose_name='От кого', db_column='id_from_user')
    id_to_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='to_user',
                                   verbose_name='Кому', db_column='id_to_user')

    class Meta:
        db_table = 'chats'
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'

    def __str__(self):
        return f"{self.id_from_user} => {self.id_to_user}"


# Operated models tables

class Message(models.Model):
    id_chat = models.ForeignKey(Chat, on_delete=models.CASCADE, verbose_name='Чат', db_column='id_chat')
    id_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Пользователь',
                                db_column='id_user')
    datetime = models.DateTimeField('Время отправки')
    content = models.TextField('Тело')

    class Meta:
        db_table = 'messages'
        ordering = ['datetime']
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return f"{self.id_chat} || {self.id_user} || {self.datetime}"
