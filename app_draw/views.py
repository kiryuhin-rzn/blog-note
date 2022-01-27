from django.views.generic.base import TemplateView


class DrawView(TemplateView):

    template_name = "app_draw/index.html"


class ReactView(TemplateView):

    template_name = "app_draw/app_react.html"

