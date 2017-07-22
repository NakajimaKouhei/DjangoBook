import re

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, _user_has_perm
)
from django.core import validators
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

#カスタムユーザーモデル
class M_EMPManager(BaseUserManager):
    def create_user(self, emp_num, email_address, password, **extra_fields):
        now = timezone.now()
        if not email_address:
            raise ValueError('Users must have an email address.')
        email_address = M_EMPManager.normalize_email(email_address)
        user = self.model(
            emp_num=emp_num,
            email_address=email_address,
            is_active=True,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, emp_num, email_address, password, **extra_fields):
        user = self.create_user(emp_num, email_address, password)
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        # user.is_superuser = True
        user.save(using=self._db)
        return user

class M_EMP(AbstractBaseUser):
    """M_EMP """
    emp_num         = models.IntegerField(_('emp num'), primary_key=True, unique=True, null=False, blank=False,
                                      validators=[MaxValueValidator(99999), MinValueValidator(1)])
    email_address   = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    emp_name        = models.CharField(_('emp name'), max_length=50, null=True, blank=True)
    admin_flag       = models.CharField(_('admin flag'), max_length=1, default=0)
    regist_emp_num  = models.IntegerField(_('regist emp num'),validators=[MaxValueValidator(99999), MinValueValidator(1)], default=0)
    update_emp_num  = models.IntegerField(_('update emp num'),validators=[MaxValueValidator(99999), MinValueValidator(1)], default=0)
    regist_time     = models.DateTimeField(_('regist time'), default=timezone.now)
    update_time     = models.DateField(_('update time'), default=timezone.now)

    is_active   = models.BooleanField(default=True)
    is_staff    = models.BooleanField(default=False)
    is_admin    = models.BooleanField(default=False)

    objects = M_EMPManager()

    USERNAME_FIELD  = 'email_address'
    REQUIRED_FIELDS = ['emp_num']

    class Meta:
        db_table = 'm_emp'

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email_address])

    def user_has_perm(user, perm, obj):
        return _user_has_perm(user, perm, obj)

    def has_perm(self, perm, obj=None):
        return _user_has_perm(self, perm, obj=obj)

    def has_module_perms(self, app_label):
        return self.is_admin

    def get_short_name(self):
        return self.emp_num

    @property
    def is_superuser(self):
        return self.is_admin