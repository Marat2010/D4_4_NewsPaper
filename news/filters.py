import django_filters
from django_filters import FilterSet  # импортируем filterset, чем-то напоминающий знакомые дженерики
from .models import Post, Author


# создаём фильтр
class PostFilter(FilterSet):

    class Meta:
        model = Post
        fields = {
            'dateCreation': ['gte'],
            'author': ['exact'],
                  }

