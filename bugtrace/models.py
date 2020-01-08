from django.db import models
from django.contrib.auth.models import User

class Ticket(models.Model):
    title = models.CharField(max_length=50)
    add_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    description = models.TextField()
    author = models.ForeignKey(User,related_name="author", on_delete=models.CASCADE)
    NEW = 'n'
    IN_PROGRESS = 'ip'
    FINISHED = 'f'
    INVALID = 'iv'
    ticket_status_choices = [
        (NEW, "New"),
        (IN_PROGRESS, "In Progress"),
        (FINISHED, "Finished"),
        (INVALID, "Invalid")
    ]
    ticket_status = models.CharField(max_length=2, choices=ticket_status_choices, default=NEW)
    ticket_assignee = models.ForeignKey(User, null=True,related_name='ticketassignee', on_delete=models.CASCADE)
    ticket_finisher = models.ForeignKey(User,related_name='ticketfinisher', null=True, on_delete=models.CASCADE)

def __str__(self):
    
    return f"{self.author}"