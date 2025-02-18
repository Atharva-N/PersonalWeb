from django.db import models

class UserDetails(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_number = models.CharField(max_length=20, blank=True, null=True, help_text="Enter phone number with country code")
    message = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
