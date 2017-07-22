from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

#レビュー
class Review(models.Model):
    isbn            = models.CharField(primary_key=True, max_length=15, null=False, blank=False)
    emp_num         = models.IntegerField(validators=[MaxValueValidator(99999), MinValueValidator(1)], default=0)
    review          = models.CharField(max_length=200)
    regist_emp_num  = models.IntegerField(validators=[MaxValueValidator(99999), MinValueValidator(1)], default=0)
    update_emp_num  = models.IntegerField(validators=[MaxValueValidator(99999), MinValueValidator(1)], default=0)
    regist_time     = models.DateTimeField(default=timezone.now)
    update_time     = models.DateField(default=timezone.now)
    
    class Meta:
        db_table = 'review'
        unique_together = (('isbn', 'emp_num'),)