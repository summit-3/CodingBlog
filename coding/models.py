from django.db import models


# Create your models here.
class Code(models.Model):
    problem_numbeer = models.IntegerField(default=0)
    problem_name = models.TextField(max_length=300)
    problem_description = models.TextField(max_length=5000)
    input_format = models.TextField(max_length=1000, default=True)
    output_format = models.TextField(max_length=1000, default=True)
    constaints = models.TextField(max_length=1000, default=True)
    time_limit = models.TextField(max_length=1000, default=True)
    example = models.TextField(max_length=3000, default=True)
    problem_sorceCode = models.TextField(default = True)
    problem_videoLink = models.TextField(max_length=1000, default=True)

    def __str__(self):
	    return self.problem_name




