from datetime import date
from django.forms import *
from django.core.exceptions import ValidationError
from .models import ReviewRequest

class ReviewRequestForm (ModelForm):
	class Meta:
		model = ReviewRequest
		fields = '__all__'
		labels = {
			'requestor': 'Orig Dude'
		}
		help_texts = {
			'requestor': 'This is the name of the person'
		}
		error_messages = {
			'requestor': { 'max_length': 'This is the name of the person' }
		}
		widgets = {
			'dateRequested': DateInput(attrs={"type": "date"}),
			'requestor': TextInput(),
			'customer': TextInput()
		}

	def clean_dateRequested(self):
		d = self.cleaned_data.get("dateRequested")
		if d < date.today():
			raise ValidationError("Request date cannot be in the past")
		return d

