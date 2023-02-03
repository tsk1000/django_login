from apputils.exception import exception
from django.views.generic import TemplateView


class SampleView(TemplateView):
    """サンプルのビュー"""

    # テンプレート
    template_name = "sample/sample.html"

    @exception
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
        