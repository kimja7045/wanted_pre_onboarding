from rest_framework import viewsets,  permissions
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from .filter import JobPostingFilter
from django.db.models import Q


class JobPostingViewSet(viewsets.ModelViewSet):
    queryset = JobPosting.objects.select_related('company')
    serializer_action_classes = {
        'list': JobPostingListSerializer,
    }
    serializer_class = JobPostingDetailSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = JobPostingFilter

    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()

    def get_queryset(self):
        query = self.request.query_params
        if query.get('search'):
            search_keyword = query.get('search')
            return super().get_queryset().filter(
                Q(company__name__icontains=search_keyword) | Q(position__icontains=search_keyword)
            )
        return super().get_queryset()


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
