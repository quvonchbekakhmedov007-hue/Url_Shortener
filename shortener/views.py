# from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import redirect
from .models import Shorturl
from .serializers import ShorturlSerializer, ShorturlDetailSerializer
from .utils import generate_code
from django.conf import settings

# Create your views here.


class ShortenView(APIView):
    def post(self, request):
        serializer = ShorturlSerializer(data=request.data)
        if serializer.is_valid():
            code = generate_code()
            serializer.save(code=code)

            return Response({
                "short_url": f"{settings.BASE_URL}/{code}",
                "code": code
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RedirectView(APIView):
    def get(self, request, code):
        url_obj=get_object_or_404(Shorturl, code=code)
        url_obj.clicks+=1
        url_obj.save()

        return redirect(url_obj.original_url)


class StatsView(APIView):
    def get(self, request, code):
        url_obj=get_object_or_404(Shorturl, code=code)
        serializer=ShorturlDetailSerializer(url_obj)

        return Response(serializer.data)





