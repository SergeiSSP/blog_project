from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.CharField(
        max_length= 1000,
        null=False,
        default="Enter your article"
    )
    date = models.DateTimeField(
        null=True,
    )


    def __str__(self):
        return self.title