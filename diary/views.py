from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView

from .models import Entry


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "diary/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        entries = Entry.objects.filter(owner=self.request.user)
        context["entries"] = entries

        context["years"] = entries.dates("created_at", "year")
        context["months"] = entries.dates("created_at", "month")

        title_query = self.request.GET.get("title")
        content_query = self.request.GET.get("content")

        if title_query:
            entries = entries.filter(title__icontains=title_query)

        if content_query:
            entries = entries.filter(content__icontains=content_query)

        context["entries"] = entries
        return context


class IndexView(LoginRequiredMixin, ListView):
    model = Entry
    template_name = "diary/index.html"
    context_object_name = "entries"

    def get_queryset(self):
        queryset = Entry.objects.filter(owner=self.request.user)
        title_query = self.request.GET.get("title")  # Получаем строку поиска по заголовку
        content_query = self.request.GET.get("content")  # Получаем строку поиска по содержимому
        now = timezone.now()
        queryset = queryset.filter(created_at__year=now.year, created_at__month=now.month)

        if title_query:
            queryset = queryset.filter(title__icontains=title_query)  # Фильтруем по заголовку

        if content_query:
            queryset = queryset.filter(content__icontains=content_query)  # Фильтруем по содержимому

        return queryset


class EntryCreateView(LoginRequiredMixin, CreateView):
    model = Entry
    template_name = "diary/create_entry.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("diary:index")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class EntryUpdateView(LoginRequiredMixin, UpdateView):
    model = Entry
    template_name = "diary/edit_entry.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("diary:index")

    def get_queryset(self):
        return Entry.objects.filter(owner=self.request.user)


class EntryDetailView(LoginRequiredMixin, DetailView):
    model = Entry
    template_name = "diary/entry_detail.html"

    def get_queryset(self):
        return Entry.objects.filter(owner=self.request.user)


class EntryDeleteView(LoginRequiredMixin, DeleteView):
    model = Entry
    template_name = "diary/entry_confirm_delete.html"
    success_url = reverse_lazy("diary:index")

    def get_queryset(self):
        return Entry.objects.filter(owner=self.request.user)
