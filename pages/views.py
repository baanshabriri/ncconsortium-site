
# Create your views here.
from django.shortcuts import get_object_or_404, render
from core.models import Page, ProductSection, CompanyOverview, MissionContent, ContactInfo, FooterContent

def page_view(request, slug):
    page = get_object_or_404(Page, slug=slug, is_published=True)
    return render(request, "pages/page.html", {"page": page})

def home(request):
    product_sections = ProductSection.objects.filter(id=1).prefetch_related("items").all()
    other_product_sections = ProductSection.objects.filter(id__in=[2, 3, 4]).prefetch_related("items").all()
    company = CompanyOverview.objects.first()
    mission = MissionContent.objects.first()
    contact = ContactInfo.objects.first()
    footer = FooterContent.objects.first()
    return render(
        request,
        "pages/home.html",
        {
            "product_sections": product_sections,
            "other_product_sections": other_product_sections,            
            "company": company,
            "mission": mission,
            "contact": contact,
            "footer": footer,
        }
    )


