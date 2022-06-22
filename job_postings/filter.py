from django_filters import rest_framework as filters
from .models import *
from django.db.models import Q, Subquery, Count


class JobPostingFilter(filters.FilterSet):
    search = filters.CharFilter(method='get_search')

    class Meta:
        model = JobPosting
        fields = [
            'search',
        ]

    def get_search(self, queryset, name, value):
        print('a')
        return queryset.filter(
            Q(company__icontains=value) | Q(position__icontains=value)
        ).distinct()
