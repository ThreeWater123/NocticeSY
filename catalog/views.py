from django.views import generic
from django.urls import reverse_lazy
from .forms import GroupForm 

from .models import group

# Create your views here.
class group_list(generic.ListView):
    model=group
    template_name="group.html"
class group_detail(generic.DetailView):
    model=group
    template_name="group_detail.html"
class group_UpdateNotice(generic.UpdateView):
    form=GroupForm
    model=group
    template_name="group_update.html"
    fields=('notice',)
    success_url=reverse_lazy("catalog:group")