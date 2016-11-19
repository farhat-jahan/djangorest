from django.db import models
import datetime
from django.contrib.auth.models import User
from expense_tracker.choices import PAID_FOR_CHOICE, PAYMENT_MODE_CHOICE
from django.utils import timezone

class BaseModel(models.Model):
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		abstract = True


class UserDetail(BaseModel):
	user = models.OneToOneField(User)
	address = models.CharField(max_length=30, blank=True)

	class Meta:
		db_table = "userdetail"


class ExpenseDetail(BaseModel):
	user_detail = models.ForeignKey(User)
	amount_spent = models.DecimalField(max_digits=19, decimal_places=2)
	paid_for = models.CharField(max_length=15,choices=PAID_FOR_CHOICE)
	paid_date = models.DateTimeField(default=timezone.now())
	description = models.TextField(null=True, blank=True)
	payment_mode = models.CharField(max_length=10, choices=PAYMENT_MODE_CHOICE, null=True, blank=True)
	balance = models.DecimalField(max_digits=19, decimal_places=2, null=True)

	class Meta:
		db_table = "expensedetail"

