from socket import fromfd
from rest_framework import viewsets, views, status
from rest_framework.response import Response
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from .filter import JobPostingFilter
from django.db import transaction
from django.db.models import Q
from django.forms import model_to_dict

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

def render_error_message(mesage):
    return Response({
        'success': False, 'message': mesage
    })


class JobApplyView(views.APIView):
    def get(self, request):
        return Response(
            list(JobApply.objects.select_related('job_posting', 'user').
                 values('job_posting', 'user'))
            )

    @transaction.atomic()
    def post(self, request):
        data = request.data
        if not data.get('job_posting_id'):
            return render_error_message('job_posting_id 입력은 필수입니다!')
        elif not data.get('user_id'):
            return render_error_message('user_id 입력은 필수입니다!')
        
        JobApply.objects.create(job_posting_id=data['job_posting_id'], user_id=data['user_id'])
        
        return Response({
            'success': True, 'message': '채용공고에 지원되었습니다.'
            }, status=status.HTTP_201_CREATED
        )