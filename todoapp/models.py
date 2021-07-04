from django.db import models

# Create your models here.
class TodoModel(models.Model):
  content = models.CharField(max_length=100)
  postdate = models.DateField(auto_now_add=True)
  def __str__(self):
    return self.content