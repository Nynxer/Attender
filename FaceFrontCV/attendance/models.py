from django.db import models

class AttendanceRecord(models.Model):
    name = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, default='Present')

    def __str__(self):
        return f"{self.name} - {self.status} at {self.timestamp}"
