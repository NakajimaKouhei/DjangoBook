from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

#像syp
class M_Book_Stock(models.Model):
    book_stock_id          = models.AutoField(primary_key=True)
    isbn            = models.CharField(max_length=15, null=False, blank=False)
    owner_emp_emp_num         = models.IntegerField(validators=[MaxValueValidator(99999), MinValueValidator(1)], default=9999)
    review          = models.CharField(max_length=200)
    regist_emp_num  = models.IntegerField(validators=[MaxValueValidator(99999), MinValueValidator(1)], default=0)
    update_emp_num  = models.IntegerField(validators=[MaxValueValidator(99999), MinValueValidator(1)], default=0)
    regist_time     = models.DateTimeField(default=timezone.now)
    update_time     = models.DateField(default=timezone.now)
    
    class Meta:
        db_table = 'm_book_stock'