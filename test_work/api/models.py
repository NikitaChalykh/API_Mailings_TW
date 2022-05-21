from django.db import models


class Contact(models.Model):
    number = models.IntegerField()
    code = models.CharField(max_length=10)
    tag = models.CharField(null=True, blank=False, max_length=50)
    time_zone = models.CharField(max_length=10)


class Mailing(models.Model):
    start_send_time = models.DateTimeField()
    text = models.TextField()
    tag = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    end_send_time = models.DateTimeField()


class Message(models.Model):
    STATUS_CHOICES = (
        ('S', 'send'),
        ('N', 'not send'),
    )
    send_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    mailing = models.ForeignKey(
        Mailing,
        on_delete=models.CASCADE,
        related_name='messages'
    )
    contact = models.ForeignKey(
        Contact,
        on_delete=models.CASCADE,
        related_name='messages'
    )
