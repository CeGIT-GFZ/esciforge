from django.contrib import admin
from publish.models import Submission,Author,Affiliation

# Register your models here.
admin.site.register(Submission)
admin.site.register(Author)
admin.site.register(Affiliation)
