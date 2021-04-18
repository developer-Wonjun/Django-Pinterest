from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=200, null=False)
    image = models.ImageField(upload_to='project/', null=True)

    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk} : {self.title}' #f'' = 직접 변수를 출력할 수 있다.