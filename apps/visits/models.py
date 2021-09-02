from django.db import models
from datetime import datetime
from django.utils import timezone
from django.utils.dateformat import format

from ..students.models import Student

class Visit(models.Model):
    # Required Identification Fields
    student = models.ForeignKey(Student, models.SET_NULL, null=True, blank=True, related_name='student_visits')
    
    # Time Fields
    start = models.DateTimeField()
    end = models.DateTimeField(blank=True, null=True)
    duration = models.DurationField(blank=True, null=True)

    # Misc Fields
    visit_reason = models.TextField(blank=True)

    @property
    def student_info(self):
        return f"{self.student.name} ({self.student.student_id})"

    @property
    def start_simple(self):
        stime = self.start.strftime("%H:%M:%S")
        return f"{stime}"
    
    @property
    def unix_time(self):
        return format(self.start, 'U')

    def end_visit(self):
        self.end = timezone.now()
        self.duration = self.end - self.start
        self.save()

    def __str__(self):
        return f"{self.student} | {self.start} -> {self.end}"