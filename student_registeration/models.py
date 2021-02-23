from django.db import models

# Create your models here.
class ProgramDetails(models.Model):
    std_program = models.CharField(max_length=15)

    def __str__(self):
        return self.std_program


class StudentInfo(models.Model):
    std_name = models.CharField(max_length=50)
    std_fname = models.CharField(max_length=50)
    std_phone = models.CharField(max_length=13)
    std_program = models.ForeignKey(ProgramDetails, on_delete=models.CASCADE)