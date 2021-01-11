# Generated by Django 3.1.5 on 2021-01-10 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pollsdb',
            options={'ordering': ['date_start'], 'verbose_name': 'Анкету', 'verbose_name_plural': 'Анкета'},
        ),
        migrations.AlterModelOptions(
            name='questions',
            options={'ordering': ['polls_id'], 'verbose_name': 'Вопрос анкеты', 'verbose_name_plural': 'Вопросы анкеты'},
        ),
        migrations.AlterModelOptions(
            name='useranswer',
            options={'ordering': ['id_user'], 'verbose_name': 'Ответ респондента', 'verbose_name_plural': 'Ответы респондентов'},
        ),
        migrations.AlterModelOptions(
            name='users',
            options={'ordering': ['user_id'], 'verbose_name': 'Респондент', 'verbose_name_plural': 'Респонденты'},
        ),
    ]