from django.db import models

class Variable(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return '{}'.format(self.name)
