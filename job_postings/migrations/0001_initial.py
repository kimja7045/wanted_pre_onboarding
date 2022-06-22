# Generated by Django 3.2.13 on 2022-06-22 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='회사명')),
                ('country', models.CharField(max_length=32, verbose_name='국가')),
                ('region', models.CharField(max_length=32, verbose_name='지역')),
            ],
            options={
                'verbose_name': '회사',
                'verbose_name_plural': '회사',
                'db_table': 'companies',
            },
        ),
        migrations.CreateModel(
            name='JobPosting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=64, unique=True, verbose_name='채용포지션')),
                ('reward', models.PositiveIntegerField(verbose_name='채용보상금')),
                ('current_tech', models.CharField(max_length=32, verbose_name='사용기술')),
                ('content', models.TextField(verbose_name='채용내용')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_posting_companies', to='job_postings.company', verbose_name='회사')),
            ],
            options={
                'verbose_name': '채용공고',
                'verbose_name_plural': '채용공고',
                'db_table': 'job_postings',
            },
        ),
        migrations.CreateModel(
            name='JobApply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_posting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_apply_job_postings', to='job_postings.jobposting', verbose_name='지원한 채용공고')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_apply_users', to='users.user', verbose_name='지원한 사용자')),
            ],
            options={
                'verbose_name': '채용공고 지원',
                'verbose_name_plural': '채용공고 지원',
                'db_table': 'job_applies',
            },
        ),
    ]
