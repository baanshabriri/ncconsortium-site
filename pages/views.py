
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
    print(f"Company Overview: {company}")
    mission = MissionContent.objects.first()
    contact = ContactInfo.objects.first()
    footer = FooterContent.objects.first()
    process = company.process_image if company else None
    print(f"Process Image: {process}")
    return render(
        request,
        "pages/home.html",
        {
            "product_sections": product_sections,
            "other_product_sections": other_product_sections,            
            "company": company,
            "mission": mission,
            "process": process,
            "contact": contact,
            "footer": footer,
        }
    )


