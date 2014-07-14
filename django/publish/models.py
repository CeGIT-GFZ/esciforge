from django.db import models

# Create your models here.

class Affiliation(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    last_name = models.CharField(null=True, max_length=100)
    first_name = models.CharField(null=True, max_length=100)
    email = models.EmailField()
    affiliations = models.ManyToManyField(Affiliation)
    orcid = models.TextField(null=True)

class Submission(models.Model):
    id = models.AutoField(primary_key=True)
    src_repo_url = models.TextField()
    src_repo_type = models.CharField(max_length=8)
    title = models.TextField()
    sub_date = models.DateTimeField(null=True)
    pub_date = models.DateTimeField(null=True)
    doi = models.TextField(null=True)
    authors = models.ManyToManyField(Author)

