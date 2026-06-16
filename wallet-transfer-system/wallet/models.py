from django.db import models

class Wallet(models.Model):
    username = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Transfer(models.Model):
    sender = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name="sent_transfers")
    receiver = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name="received_transfers")
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    status = models.CharField(
        max_length=10,
        choices=[
            ("SUCCESS", "SUCCESS"),
            ("FAILED", "FAILED"),
            ("PENDING", "PENDING"),
        ],
        default="PENDING"
    )

    created_at = models.DateTimeField(auto_now_add=True)