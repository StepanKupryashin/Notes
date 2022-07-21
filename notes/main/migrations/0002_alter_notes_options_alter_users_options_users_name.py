# Generated by Django 4.0.6 on 2022-07-20 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notes',
            options={'verbose_name': 'Заметка', 'verbose_name_plural': 'Заметки'},
        ),
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AddField(
            model_name='users',
            name='name',
            field=models.TextField(db_column='name', default='user', max_length=90, verbose_name='Имя'),
            preserve_default=False,
        ),
    ]