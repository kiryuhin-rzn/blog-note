from django.views.generic.base import TemplateView


class DrawView(TemplateView):

    template_name = "app_draw/index.html"


class ReactView(TemplateView):

    template_name = "app_draw/app_react.html"


class CanvasView(TemplateView):

    template_name = "app_draw/canvasjs.html"


class ExampleView(TemplateView):

    template_name = "app_draw/example.html"

class AnimateView(TemplateView):

    template_name = "app_draw/animate.html"

class MenuView(TemplateView):

    template_name = "app_draw/menu.html"

class MakeupView(TemplateView):

    template_name = "app_draw/makeup.html"