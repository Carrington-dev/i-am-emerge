from django.db import models

class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date_recieved		    = models.DateTimeField(verbose_name='date recieved', auto_now_add=True, blank=True, null=True)
    date_last_viewed		= models.DateTimeField(verbose_name='last viewed', auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.full_name + " @ " + self.email

    def __unicode__(self):
        return self.full_name + " @ " + self.email



class Subscribe(models.Model):
    email                   = models.EmailField(max_length=200, verbose_name='email', unique=True)
    is_subscribed           = models.BooleanField(default=True ,verbose_name='subscribed' )
    date_recieved		    = models.DateTimeField(verbose_name='date recieved', auto_now_add=True)
    date_last_viewed		= models.DateTimeField(verbose_name='last viewed', auto_now=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'



class Calculator(models.Model):
    # email                   = models.EmailField(max_length=200, verbose_name='email', unique=True)
    # is_subscribed           = models.BooleanField(default=True ,verbose_name='subscribed' )
    date_recieved		    = models.DateTimeField(verbose_name='date recieved', auto_now_add=True)
    date_last_viewed		= models.DateTimeField(verbose_name='last viewed', auto_now=True)

    def __str__(self):
        return f"<Calculator @{self.pk}>"

    class Meta:
        verbose_name = 'Calculator'
        verbose_name_plural = 'Calculators'