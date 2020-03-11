from django.db import models, IntegrityError
from django.utils.crypto import get_random_string
from .utils import qr_code_gen


# Create your models here.
class Link(models.Model):
    url = models.URLField(max_length=1000)
    code = models.CharField(unique=True, max_length=1000, null=True, blank=True)
    qr = models.ImageField(upload_to='qr_codes/', blank=True)

    def __str__(self):
        return self.url

    def save(self, *args, **kwargs):
        if not self.code:
            while True:
                try:
                    self.code = get_random_string(length=10)
                except IntegrityError:
                    continue
                break
        if not self.qr:
            self.qr = qr_code_gen(code=self.code, url=self.url)
        return super().save(*args, **kwargs)
