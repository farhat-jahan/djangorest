from django.db import models

# Create your models here.
class Users(models.Model):
	created_date = models.DateField(default=datetime.datetime.now())
	user = models.ForeignKey(User)
	address = models.CharField(max_length=30, blank=True)

	class Meta:
		db_table = "users"


class ExpenseDetail(models.Model):
	user = models.ForeignKey(Users)
	created_date = models.DateField(default=datetime.datetime.now())
	amount_spend = models.DecimalField(decimal_places=2)
	paid_to = models.CharField(max_length=40)
	paid_date = models.DateField()
	description = models.CharField(max_length=60)
	payment_mode = models.CharField(max_length=20)
	balance = modeels.DecimalField(decimal_places=2)

	class Meta:
       		db_table = "expences"



