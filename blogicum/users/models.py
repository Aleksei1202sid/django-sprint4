from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    pass
    # bio = models.TextField('Биография', blank=True)
