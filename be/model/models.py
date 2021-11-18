from django.db import models
from django.db.models.fields.files import FileField

# Create your models here.
class PredictModel(models.Model):
    img = FileField(upload_to="images/")