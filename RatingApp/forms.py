from django import forms
from .models import RatingTable

class RatingTableForm(forms.ModelForm):
    class Meta:
      model = RatingTable
      fields ='__all__'
  