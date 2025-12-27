
# Register your models here.
from django.contrib import admin
from .models import (
    CompanyOverview,
    MissionContent,
    ContactInfo,
    FooterContent,
    Page, 
    ProductSection, 
    ProductItem
)

@admin.register(CompanyOverview)
class CompanyOverviewAdmin(admin.ModelAdmin):
    pass


@admin.register(MissionContent)
class MissionContentAdmin(admin.ModelAdmin):
    pass


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(FooterContent)
class FooterContentAdmin(admin.ModelAdmin):
    pass
class ProductItemInline(admin.TabularInline):
    model = ProductItem
    extra = 1


@admin.register(ProductSection)
class ProductSectionAdmin(admin.ModelAdmin):
    inlines = [ProductItemInline]
    ordering = ["order"]
    list_display = ["title", "order"]


@admin.register(ProductItem)
class ProductItemAdmin(admin.ModelAdmin):
    list_display = ["name", "section", "order"]
    ordering = ["section", "order"]


admin.site.register(Page)
