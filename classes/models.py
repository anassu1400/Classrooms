from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
class Classroom(models.Model):
	name = models.CharField(max_length=120)
	teacher = models.ForeignKey(User, on_delete=models.CASCADE,)
	subject = models.CharField(max_length=120)
	year = models.IntegerField()

	def get_absolute_url(self):
		return reverse('classroom-detail', kwargs={'classroom_id':self.id})

class Student(models.Model):
	name = models.CharField(max_length=120)
	date_of_birth = models.DateField()
	MALE = 'M'
	FEMALE = 'F'
	GENDERS = (
		(MALE, 'M'),
		(FEMALE, 'F'),
		)
	gender = models.CharField(max_length=2, choices=GENDERS, default=FEMALE)
	exam_grade = models.DecimalField(max_digits=5, decimal_places=2)
	classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='students')