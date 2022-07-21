from tabnanny import verbose
from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.TextField(max_length=90, db_column="name", verbose_name="Имя")
    birthday = models.DateField(blank=False, null=False, db_column='birthday', verbose_name="День рождения")
    status = models.TextField(blank=False, null=False, db_column='status', verbose_name="статус", max_length=140)
    bio = models.TextField(blank=False, null=False, db_column='bio', verbose_name="био")  
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        
class Notes(models.Model):
    user = models.ForeignKey("Users", on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True, db_column='date', verbose_name="дата")
    title = models.TextField(max_length=255, db_column='title', verbose_name="заголовок")
    text = models.TextField(max_length=255, db_column='text', verbose_name="текст")
    
    class Meta:
        verbose_name = "Заметка"
        verbose_name_plural = "Заметки"
    