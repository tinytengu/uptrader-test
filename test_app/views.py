from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "test_app/pages/index.html"


class AboutView(TemplateView):
    template_name = "test_app/pages/about.html"


class LinksView(TemplateView):
    template_name = "test_app/pages/links.html"
