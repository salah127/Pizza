
from django.db import models
# Create your models here.
class Pizza(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField(max_length=120, unique=True, null=True, blank=True)
	prix = models.DecimalField(max_digits=6, decimal_places=2)
	disponible = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.title} - {self.prix}€ ({'Disponible' if self.disponible else 'Indisponible'})"

# Create your models here.
