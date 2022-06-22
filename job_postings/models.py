from django.db import models
from users.models import User


class Company(models.Model):
    class Meta:
        db_table = 'companies'
        verbose_name = '회사'
        verbose_name_plural = verbose_name

    name = models.CharField(
        verbose_name='회사명',
        max_length=64,
        unique=True
    )
    country = models.CharField(
        verbose_name='국가',
        max_length=32,
    )
    region = models.CharField(
        verbose_name='지역',
        max_length=32,
    )


class JobPosting(models.Model):
    class Meta:
        db_table = 'job_postings'
        verbose_name = '채용공고'
        verbose_name_plural = verbose_name

    company = models.ForeignKey(
        verbose_name='회사',
        to='Company',
        related_name='job_posting_companies',
        on_delete=models.CASCADE,
    )
    position = models.CharField(
        verbose_name='채용포지션',
        max_length=64,
    )
    reward = models.PositiveIntegerField(
        verbose_name='채용보상금',
    )
    current_tech = models.CharField(
        verbose_name='사용기술',
        max_length=32,
    )
    content = models.TextField(
        verbose_name='채용내용',
    )


class JobApply(models.Model):
    class Meta:
        db_table = 'job_applies'
        verbose_name = '채용공고 지원'
        verbose_name_plural = verbose_name

    job_posting = models.ForeignKey(
        verbose_name='지원한 채용공고',
        to='JobPosting',
        related_name='job_apply_job_postings',
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        User,
        verbose_name='지원한 사용자',
        related_name='job_apply_users',
        on_delete=models.CASCADE,
    )
