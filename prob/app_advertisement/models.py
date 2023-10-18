from django.contrib.auth import get_user_model
from django.db import models
from django.contrib import admin
from django.utils.html import format_html

# Create your models here.
# Заголовок, цена, описание, from django.contrib.auth import get_user_model

User = get_user_model()

class Advertisement(models.Model):
    # СharField - строковое поле для небольших строк 
    title = models.CharField('Заголовок', max_length=128)
    # TextField - строковое поле для больших строк 
    description = models.TextField('Описание')
    # 22300,55
    # DecimalField - похоже на float в Питоне - числовое поле 
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    # BooleanField - логическое поле, принимающее 2 значения: True/False
    auction = models.BooleanField('Торг', help_text='Отметьте, если торг будет уместен')
    # DateTimeField - cпециальное поле для работы с датами 
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE, blank=True,null=True)
    image = models.ImageField("изображение", upload_to="advertisements/")
  
    @admin.display(description='Дата создания')
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}</span>', created_time
            )
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")
    
<<<<<<< HEAD
    @admin.display(description='Дата создания')
    def updated_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}</span>', created_time
            )
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")
    
=======
    @admin.display(description='дата последнего обновления')
    def updated_date(self):
        from django.utils import timezone
        if self.updated_at.date() == timezone.now().date():
            created_time = self.updated_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color: red; font-weight: bold;">Сегодня в {}</span>', created_time
            )
        return self.updated_at.strftime("%d.%m.%Y в %H:%M:%S")
>>>>>>> aff0d0f9e223afdb28d9be9e84e4540b2ddc44f9
    
    def __str__(self):
        return f'Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})'
    
    class Meta:
        db_table = 'advertisements'