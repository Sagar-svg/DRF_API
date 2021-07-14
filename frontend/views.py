from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from ytApi import views
# Create your views here.
class ListDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'profile_detail.html'

    def get(self, request, qu):
        list = views.snippet_list(request, qu)
        
        return Response({'list': list})

    

def index(request):
    return render(request, 'frontend/index.html')

