from django.db import models, IntegrityError
from django.utils.crypto import get_random_string


# Create your models here.
class Link(models.Model):
    url = models.URLField(unique=True, max_length=1000)
    code = models.CharField(unique=True, max_length=1000,null=True,blank=True)

    def __str__(self):
        return self.url

    def save(self, *args,**kwargs):
        if not self.code:
            while True:
                try:
                    self.code = get_random_string(length=10)
                except IntegrityError:
                    continue
                break
        return super().save(*args, **kwargs)