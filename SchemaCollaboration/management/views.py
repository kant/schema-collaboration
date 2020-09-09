from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from comments.forms import CommentForm
from comments.views import AbstractAddCommentView
from core.models import Datapackage, Person
from management.forms import PersonModelForm, DatapackageModelForm


class DatapackageListView(ListView):
    template_name = 'management/schema-list.html'
    model = Datapackage
    context_object_name = 'schemas'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sidebar_active'] = 'datapackages'
        context['breadcrumb'] = [{'name': 'Datapackages'}]

        for schema in context['schemas']:
            schema.edit_link = self.request.build_absolute_uri(f'{reverse("datapackage-ui")}?load={schema.uuid}')

        return context


class PersonMixin():
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sidebar_active'] = 'people'
        return context


class PersonListView(PersonMixin, ListView):
    template_name = 'management/person-list.html'
    model = Person
    context_object_name = 'people'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumb'] = [{'name': 'People'}]

        for person in context['people']:
            person.list_datapackages_url = self.request.build_absolute_uri(
                reverse('datapackage-list', kwargs={'collaborator_uuid': person.uuid}
                        ))

        return context


class PersonCreateView(PersonMixin, CreateView):
    model = Person
    form_class = PersonModelForm
    template_name = 'management/person-form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumb'] = [{'name': 'People', 'url': reverse('management:list-people')},
                                 {'name': 'Create'}]
        return context


class PersonUpdateView(PersonMixin, UpdateView):
    model = Person
    form_class = PersonModelForm
    template_name = 'management/person-form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumb'] = [{'name': 'People', 'url': reverse('management:list-people')},
                                 {'name': 'Edit'}]
        return context


class PersonDeleteView(DeleteView):
    model = Person
    success_url = reverse_lazy('management-list-people')


class PersonDetailView(PersonMixin, DetailView):
    model = Person
    template_name = 'management/person-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumb'] = [{'name': 'People', 'url': reverse('management:list-people')},
                                 {'name': 'Detail'}]
        return context


class DatapackageMixin():
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sidebar_active'] = 'datapackages'
        return context


class DatapackageDetailView(DatapackageMixin, DetailView):
    model = Datapackage
    template_name = 'management/datapackage-detail.html'
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['breadcrumb'] = [{'name': 'Datapackage', 'url': reverse('management:list-schemas')},
                                 {'name': 'Detail'}]

        person = Person.objects.get(user=self.request.user)

        context['comment_form'] = CommentForm(person=person,
                                              datapackage_id=self.object.id,
                                              form_action_url=reverse('management:datapackage-add-comment',
                                                                      kwargs={'uuid': self.object.uuid}))

        return context


class DatapackageUpdateView(DatapackageMixin, UpdateView):
    model = Datapackage
    form_class = DatapackageModelForm
    template_name = 'management/datapackage-form.html'
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'

    def get_success_url(self):
        return reverse('management:datapackage-detail', kwargs={'datapackage_uuid': self.object.uuid})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumb'] = [{'name': 'Datapackage', 'url': reverse('management:list-people')},
                                 {'name': 'Edit'}]
        return context


class DatapackageAddCommentView(AbstractAddCommentView):
    def __init__(self, *args, **kwargs):
        success_url = None
        failure_url = None  # Unused

        super().__init__(*args, user=self.request.user,
                         success_view_name='management:datapackage-detail',
                         failure_url=None, **kwargs)
