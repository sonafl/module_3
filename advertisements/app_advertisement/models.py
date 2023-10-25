from django.contrib.auth import get_user_model
from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse

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

    def get_absolute_url(self):
        return reverse('adv_detail', kwargs={'pk' : self.pk})
  
    @admin.display(description='Дата создания')
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}</span>', created_time
            )
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")
    
    @admin.display(description='Дата создания')
    def updated_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}</span>', created_time
            )
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")
    
    @admin.display(description='фото')
    def get_html_image(self):
        if self.image:
            return format_html(
                '<img src="{url}" style="max-width: 80px; max-height: 80px;"', url=self.image.url
            )
    
    
    def __str__(self):
        return f'Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})'
    
    class Meta:
        db_table = 'advertisements'