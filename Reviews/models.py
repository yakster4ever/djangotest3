from django.db import models

# -----------------------------------------------------------------------------------
# LOV for types of reviews
# -----------------------------------------------------------------------------------
class ReviewType (models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return f"{self.name}"

# -----------------------------------------------------------------------------------
# This represents a review request.
# -----------------------------------------------------------------------------------
class ReviewRequest (models.Model):
	requestor = models.CharField(max_length=100)
	dateRequested = models.DateField()
	customer = models.CharField(max_length=400)

	# Priority field
	PRIO_LOW = 0
	PRIO_MED = 1
	PRIO_HIGH = 2
	PRIO_CHOICES = ((PRIO_LOW, 'Low'),(PRIO_MED, 'Medium'),(PRIO_HIGH,  'High'))
	priority = models.IntegerField(choices=PRIO_CHOICES, default=PRIO_MED)

	# Review type (FK)
	reviewType = models.ForeignKey(ReviewType, on_delete=models.SET_NULL, null=True, blank=True)

	def __str__(self):
		return f"{self.requestor} requested review for client {self.customer} on {self.dateRequested}: Type is {self.reviewType}"

