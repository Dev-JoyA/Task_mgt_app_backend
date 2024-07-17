# from django.db import models

# class Task(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     priority = models.CharField(max_length=10, choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')])
#     category = models.CharField(max_length=100)
#     assigned = models.CharField(max_length=200)  # comma-separated names
#     people = models.IntegerField()
#     total_people = models.IntegerField()
#     start_time = models.DateTimeField()
#     end_time = models.DateTimeField()
#     status = models.CharField(max_length=20, choices=[('in-progress', 'In Progress'), ('completed', 'Completed'), ('overdue', 'Overdue')])

#     def __str__(self):
#         return self.title

from django.db import models

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low')
    ]

    STATUS_CHOICES = [
        ('in-progress', 'In Progress'),
        ('completed', 'Completed'),
        ('overdue', 'Overdue')
    ]

    title = models.CharField(max_length=100)
    desc = models.TextField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    category = models.CharField(max_length=50)
    assigned = models.CharField(max_length=255)
    people = models.IntegerField()
    totalPeople = models.IntegerField()
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title

