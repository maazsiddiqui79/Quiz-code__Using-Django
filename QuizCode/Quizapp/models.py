from django.db import models

# Create your models here.
# ADDED MANAUALLY

class Subject(models.Model):
    name = models.CharField(max_length=100)
    # extra
    q_hint_text = models.CharField(max_length=500, default="No hint available")

    
        
    def __str__(self):
        return self.name
    
    
class Question(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    question_text  = models.CharField(max_length=300)
    
    option1  = models.CharField(max_length=100)
    option2  = models.CharField(max_length=100)
    option3  = models.CharField(max_length=100)
    option4  = models.CharField(max_length=100)
    correct_option  = models.IntegerField(choices=[(1,'Option1'),(2,'Option2'),(3,'Option3'),(4,'Option4'),])
    
    def __str__(self):
        return self.question_text
    
    
#     Migration process:
#         python manage.py makemigrations
#         python manage.py migrate
    
    
