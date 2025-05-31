from crimsonslate_tools.views.mixins import HtmxTemplateResponseMixin
from django.views.generic import TemplateView


class HomepageView(HtmxTemplateResponseMixin, TemplateView):
    extra_context = {"title": "Home"}
    http_method_names = ["get"]
    partial_template_name = "katielawless/partials/_homepage.html"
    template_name = "katielawless/homepage.html"
