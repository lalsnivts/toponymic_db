from django.views import generic
from .models import GeoNames




class IndexView(generic.ListView):
    template_name = 'toponymic_db/index.html'
    context_object_name = 'geonames'

    def get_queryset(self):
        return GeoNames.objects.order_by('geoname').prefetch_related('source_id', 'motivation_id')

class DetailView(generic.DetailView):
    model = GeoNames
    template_name = 'toponymic_db/detail.html'



