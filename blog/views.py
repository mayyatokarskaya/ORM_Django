from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .models import BlogPost


class BlogListView(ListView):
    model = BlogPost
    template_name = "blog/blog_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        # Фильтруем только опубликованные записи
        return BlogPost.objects.filter(is_published=True)


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = "blog/blog_detail.html"
    context_object_name = "post"

    def get_object(self, queryset=None):
        # Получаем объект, увеличиваем счетчик просмотров и сохраняем
        obj = super().get_object(queryset)
        obj.view_count += 1
        obj.save()
        return obj


class BlogCreateView(CreateView):
    model = BlogPost
    template_name = "blog/blog_form.html"
    fields = ["title", "content", "preview_image", "is_published"]
    success_url = reverse_lazy("blog:blog_list")


class BlogUpdateView(UpdateView):
    model = BlogPost
    template_name = "blog/blog_form.html"
    fields = ["title", "content", "preview_image", "is_published"]
    # success_url = reverse_lazy("blog:blog_list")

    def get_success_url(self):
        # Перенаправляем на страницу редактируемой статьи
        return reverse_lazy("blog:blog_detail", kwargs={"pk": self.object.pk})


class BlogDeleteView(DeleteView):
    model = BlogPost
    template_name = "blog/blog_confirm_delete.html"
    success_url = reverse_lazy("blog:blog_list")
