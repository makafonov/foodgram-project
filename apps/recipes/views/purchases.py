from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import FileResponse
from django.views import View
from django.views.generic import ListView

from apps.recipes.models import Recipe
from apps.recipes.services import generate_pdf


class PurchaseView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/purchases.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(purchases__user=self.request.user)


class DownloadPurchasesListView(View):
    def get(self, request, *args, **kwargs):
        pdf = generate_pdf(request.user)

        return FileResponse(
            pdf,
            as_attachment=True,
            filename='purchases.pdf',
        )
