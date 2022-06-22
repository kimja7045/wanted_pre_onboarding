from rest_framework import views, status
from .models import User
from django.db import transaction
from django.http import JsonResponse
from django.forms import model_to_dict

class UserView(views.APIView):
    def get(self, request):
        return True
        # return {''}

    @transaction.atomic()
    def post(self, request):
        data = request.data
        if not data.get('name'):
            return JsonResponse({
                'success': False, 'detail': 'name은 필수입니다!'
                })
        user = User.objects.create(name=data['name'])
        return JsonResponse(model_to_dict(user), status=status.HTTP_201_CREATED)

