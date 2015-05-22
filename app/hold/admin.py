from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from app.hold.models import Stock
from app.hold.models import Fund
from app.hold.models import Hold

class StockAdmin(admin.ModelAdmin):
	list_display = ("code", "name",)
	search_fields = ("code", "name",)

class FundAdmin(admin.ModelAdmin):
	list_display = ("code", "name", "rate", "amount",)
	search_fields = ("code", "name",)

class HoldAdmin(admin.ModelAdmin):
	list_display = ("stock", "fund", "rate",)
	search_fields = ("stock", "fund",)

admin.site.register(Stock, StockAdmin)
admin.site.register(Fund, FundAdmin)
admin.site.register(Hold, HoldAdmin)
