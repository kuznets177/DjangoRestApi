from django.db import models

# МОДЕЛЬ ОПРОСА ПОЛЬЗОВАТЕЛЕЙ ###

# задаем макет анкеты
class PollsDB(models.Model):
    name_poll = models.CharField(max_length=200, verbose_name="Название анкеты", null=False)
    description_text = models.TextField(verbose_name="Описание опроса", blank=True, null=True)
    date_start = models.DateField('Дата начала')
    date_end = models.DateField('Дата окончания')

    class Meta:
        ordering = ['date_start']
        verbose_name = 'Анкету'
        verbose_name_plural = 'Анкета'

    def __str__(self):
        return self.name_poll

# прописываем вопросы для анкеты
class Questions(models.Model):

    polls_id = models.ForeignKey(PollsDB, on_delete=models.CASCADE, related_name="questions",
                                 verbose_name="Название опроса")
    question_text = models.TextField(verbose_name="Текст вопроса", null=False)
    TYPE_CHOICES = (
        ('S', 'Один ответ'),
        ('M', 'Несколько ответов'),
        ('T', 'Ответ текстом'),)
    type_quest = models.CharField('Варианты ответов', max_length=1, blank=False, choices=TYPE_CHOICES,
                                  default='S',
                                  null=False)

    class Meta:
        ordering = ['polls_id']
        verbose_name = 'Вопрос анкеты'
        verbose_name_plural = 'Вопросы анкеты'

    def __str__(self):
        return self.question_text

# ответы на впоросы
class Answers(models.Model):
    quest_id = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name="answers")
    answer_text = models.CharField(max_length=200, verbose_name="Текст ответа", null=True)
    votes = models.IntegerField(default=0)

    class Meta:
        ordering = ['quest_id']
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return self.answer_text


# создаем модель ответов пользователей ###

# Пользователи проходившие опросы
class Users(models.Model):
    user_id = models.BigIntegerField(default=1)
    user_ip = models.CharField(max_length=20, default='127.0.0.1')

    class Meta:
        ordering = ['user_id']
        verbose_name = 'Респондент'
        verbose_name_plural = 'Респонденты'

# ответы пользователя
class UserAnswer(models.Model):
    id_user = models.ForeignKey(Users, on_delete=models.CASCADE, default=1, related_name="users")
    id_polls = models.ForeignKey(PollsDB, on_delete=models.CASCADE, related_name="user_polls")
    id_quest = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name="user_questions")
    id_answer = models.ForeignKey(Answers, on_delete=models.CASCADE, related_name="user_answers")
    answer_text = models.CharField(max_length=200,
                                   verbose_name="Текст ответа пользователя, если выбран текстовый ответ", null=True)

    class Meta:
        ordering = ['id_user']
        verbose_name = 'Ответ респондента'
        verbose_name_plural = 'Ответы респондентов'