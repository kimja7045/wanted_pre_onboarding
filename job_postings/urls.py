from django.urls import path, include
from rest_framework import routers
from job_postings.views import *

router = routers.DefaultRouter()

router.register('job-postings', JobPostingViewSet)
router.register('companies', CompanyViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('a', include(router.urls)),

    # path('gym-teachers', GymTeacherReadView.as_view()),
]
