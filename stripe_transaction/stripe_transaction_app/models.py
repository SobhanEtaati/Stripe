from django.db import models

# Create your models here.
class Transaction_response(models.Model):
    response_text = models.TextField()
    class Meta:
        app_label = 'stripe_transaction_app'