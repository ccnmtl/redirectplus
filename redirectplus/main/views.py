from django.views.generic.base import RedirectView, TemplateView


class LTIRedirectView(RedirectView):

    permanent = False
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        self.url = self.request.GET.get('custom_url')
        return super(LTIRedirectView, self).get_redirect_url(*args, **kwargs)


class ReceiverView(TemplateView):
    template_name = 'main/receive.html'

    def get_context_data(self, **kwargs):
        return {
            'params': self.request.GET
        }
