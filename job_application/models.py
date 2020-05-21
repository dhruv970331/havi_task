from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models import Q

job_choices = [
    ("sde1", "SDE 1"),
    ("sde2", "SDE 2"),
    ("graphic_designer", "Graphic Designer"),
    ("hr", "HR"),
    ("tech_lead", "Tech Lead")
]


class SearchManager(models.Manager):
    def search_term(self, term):
        qs = self.get_queryset()
        or_lookup = (Q(first_name__icontains=term) | Q(last_name__icontains=term) |
                     Q(email__icontains=term) | Q(contact__icontains=term) |
                     Q(job_title__icontains=term) | Q(notes__icontains=term))
        try:
            or_lookup |= (Q(expected_ctc=int(term)) | Q(current_ctc=int(term)))
        except Exception as e:
            pass
        return qs.filter(or_lookup).order_by("email","id","-application_date").distinct("email").order_by("id")

# Create your models here.


class JobApplication(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    expected_ctc = models.PositiveIntegerField()
    current_ctc = models.PositiveIntegerField(null=True, blank=True)
    contact = PhoneNumberField()
    job_title = models.CharField(choices=job_choices, max_length=50)
    application_date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(null=True, blank=True)
    objects = SearchManager()
