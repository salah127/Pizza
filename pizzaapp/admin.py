
from django.contrib import admin
from .models import Pizza

@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
	list_display = ("title", "prix", "disponible", "created_at", "is_recent")
	list_editable = ("disponible",)
	list_display_links = ("title", "prix")
	@admin.action(description="Marquer comme disponible")
	def mark_available(self, request, queryset):
		queryset.update(disponible=True)

	@admin.action(description="Marquer comme indisponible")
	def mark_unavailable(self, request, queryset):
		queryset.update(disponible=False)

	actions = ["mark_available", "mark_unavailable"]
	@admin.display(boolean=True, ordering="created_at", description="Récente ?")
	def is_recent(self, obj):
		from django.utils import timezone
		if obj.created_at:
			return obj.created_at >= timezone.now() - timezone.timedelta(days=7)
		return False
	search_fields = ("title",)
	list_filter = ("disponible", "created_at")
	ordering = ("title",)
	date_hierarchy = "created_at"
	prepopulated_fields = {"slug": ("title",)}
	readonly_fields = ("created_at",)
	fieldsets = (
		("Informations principales", {
			"fields": ("title", "slug", "prix")
		}),
		("Disponibilité et suivi", {
			"fields": ("disponible", "created_at")
		}),
	)
	prepopulated_fields = {"slug": ("title",)}
	readonly_fields = ("created_at",)
	fieldsets = (
		("Informations principales", {
			"fields": ("title", "slug", "prix")
		}),
		("Disponibilité et suivi", {
			"fields": ("disponible", "created_at")
		}),
	)
