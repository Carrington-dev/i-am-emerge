from django.db import models

class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.full_name + " @ " + self.email

    def __unicode__(self):
        return self.full_name + " @ " + self.email
