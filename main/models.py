from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    # ----
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Lists/Tasks
class ListItem(models.Model):
    name = models.CharField(max_length=50)
    isCompleted = models.BooleanField(default=False)
    due_date = models.DateField(blank=True)
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    # ----
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class TaskList(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)
    items = models.ForeignKey(ListItem, on_delete=models.CASCADE, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    # ----
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)