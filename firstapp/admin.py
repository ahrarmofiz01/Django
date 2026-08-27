from django.contrib import admin
from .models import appvarity, AppReview, Store, AppCertificate


class AppReviewInline(admin.TabularInline):
    model = AppReview
    extra = 2


class AppVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    inlines = [AppReviewInline]


class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('chai_varieties',)


class AppCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'certificate_number')


admin.site.register(appvarity, AppVarietyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(AppCertificate, AppCertificateAdmin)


