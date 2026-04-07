from django.db import models

class Page(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class ProductSection(models.Model):
    title = models.CharField(max_length=100)   # TURMERIC, GINGER, etc.
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title


class ProductItem(models.Model):
    section = models.ForeignKey(
        ProductSection,
        on_delete=models.CASCADE,
        related_name="items"
    )
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="products/", blank=True)
    image_url = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name



class CompanyOverview(models.Model):
    heading = models.CharField(max_length=200, default="COMPANY OVERVIEW")
    body = models.TextField()
    image = models.ImageField(upload_to="company_overview/", blank=True)
    process_image = models.ImageField(upload_to="company_overview/", blank=True)

    def __str__(self):
        return "Company Overview"


class MissionContent(models.Model):
    mission_points = models.JSONField(
        help_text="List of mission bullet points"
    )
    core_values = models.JSONField(
        help_text="List of core values"
    )
    image = models.ImageField(upload_to="mission_content/", blank=True)

    def __str__(self):
        return "Mission & Core Values"


class ContactInfo(models.Model):
    company_name = models.CharField(max_length=200)
    gstin = models.CharField(max_length=50)
    phone_primary = models.CharField(max_length=20)
    phone_secondary = models.CharField(max_length=20, blank=True)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return "Contact Information"


class FooterContent(models.Model):
    tagline = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return "Footer Content"
    

class ContactSubmission(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"