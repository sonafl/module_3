from django.db import models

# Create your models here.
# Заголовок, цена, описание, дата создания, дата обновления, уместен ли торг 

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
  
    def __str__(self):
        return f'Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})'
    
    class Meta:
        db_table = 'advertisements'