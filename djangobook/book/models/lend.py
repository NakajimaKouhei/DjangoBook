from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

#貸出
class Lend(models.Model):
    lend_id         = models.AutoField(primary_key=True)
    book_stock_id   = models.IntegerField(validators=[MaxValueValidator(99999), MinValueValidator(1)], default=0)
    emp_num         = models.IntegerField(validators=[MaxValueValidator(99999), MinValueValidator(1)], default=0)
    owner_emp_num   = models.IntegerField(validators=[MaxValueValidator(99999), MinValueValidator(1)], default=0)
    lend_date       = models.DateField()
    return_due_date = models.DateField()
    return_date     = models.DateField()
    regist_emp_num  = models.IntegerField(validators=[MaxValueValidator(99999), MinValueValidator(1)], default=0)
    update_emp_num  = models.IntegerField(validators=[MaxValueValidator(99999), MinValueValidator(1)], default=0)
    regist_time     = models.DateTimeField(default=timezone.now)
    update_time     = models.DateField(default=timezone.now)

    class Meta:
        db_table = 'lend'