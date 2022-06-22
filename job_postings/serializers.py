from rest_framework import serializers
from .models import JobPosting, JobApply, Company


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'


class JobPostingListSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(read_only=True, source='company.name')
    company_country = serializers.CharField(read_only=True, source='company.country')
    company_region = serializers.CharField(read_only=True, source='company.region')

    class Meta:
        model = JobPosting
        fields = (
            'id',
            'company_name',
            'company_country',
            'company_region',
            # 'company',
            'position',
            'reward',
            'current_tech',
        )


class JobPostingDetailSerializer(serializers.ModelSerializer):
    same_company_job_postings = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = JobPosting
        fields = (
            'id',
            'company',
            'position',
            'reward',
            'content',
            'current_tech',

            'same_company_job_postings'
        )

    def get_same_company_job_postings(self, obj):
        url_id = self.context.get('request').parser_context.get('kwargs')['pk']
        job_postings = list(JobPosting.objects.select_related('company').filter(
            company=obj.company).values_list('id', flat=True))
        job_postings.remove(int(url_id))

        return job_postings
