from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    email = models.EmailField(max_length=250, null=True, blank=False)

    groups = models.ManyToManyField(
        Group,
        related_name='customer',
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customer_permissions',
        blank=True,
        verbose_name='customer permissions',
        help_text='Specific permissions for this customer.',
    )

    def __str__(self):
        if self.addresses.exists():
            return str(self.addresses.first())
        else:
            return f"{self.username} (No Address Found)"
            

class Address(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='addresses')
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    county = models.CharField(max_length=255)
    post_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.county} {self.post_code}"
