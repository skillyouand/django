from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField('书名',unique=True,max_length=50,default='')
    pub = models.CharField('出版社',max_length=50,default='')
    price = models.DecimalField('价格',max_digits=7,decimal_places=2,default=0.00)
    market_price = models.DecimalField('出版社价格',max_digits=7,decimal_places=2,default=0.00)
    is_active = models.BooleanField('是否活跃',default=True)

    def __str__(self):
        return '%s_%s_%s_%s'%(self.title,self.pub,self.price,self.market_price)
