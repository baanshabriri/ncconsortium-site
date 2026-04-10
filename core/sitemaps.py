# core/sitemaps.py

from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = "weekly"

    def items(self):
        return [
            "home",
            "contact",
            "company",
            "mission",
            "process",
            "products",
            "other products",
        ]

    def location(self, obj):
        if obj in ["process", "products", "other products", "mission", "company"]:
            print(f"Generating URL for {obj}")
            return reverse("home") + f"#{obj}"
        return reverse(obj)

