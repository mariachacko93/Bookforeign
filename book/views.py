from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from rest_framework import authentication, permissions

# Create your views here.
from .models import Book 
from rest_framework.views import APIView
from book.serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly
from rest_framework.generics import CreateAPIView,ListAPIView,DestroyAPIView,RetrieveAPIView,UpdateAPIView
from rest_framework.authentication import TokenAuthentication, BasicAuthentication,SessionAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import filters


class bookCreateView(CreateAPIView):
    # authentication_classes=[TokenAuthentication]
    authentication_classes=[SessionAuthentication]
    authentication_classes=[BasicAuthentication]

    permission_classes=[IsAdminUser]
    serializer_class=BookSerializer

class bookUpdateView(UpdateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    permission_classes=[IsAdminUser]
    authentication_classes=[SessionAuthentication]
    authentication_classes=[BasicAuthentication]
    # authentication_classes=[TokenAuthentication]

class bookDetailView(RetrieveAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    authentication_classes=[SessionAuthentication]
    authentication_classes=[BasicAuthentication]
    # authentication_classes=[TokenAuthentication]

    permission_classes=[IsAuthenticated]

class bookListView(ListAPIView):
    search_fields=['author','bookname']
    filter_backends=(filters.SearchFilter,)
    serializer_class=BookSerializer
    queryset=Book.objects.all()
    authentication_classes=[SessionAuthentication]
    authentication_classes=[BasicAuthentication]
    # authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

class bookDeleteView(DestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    permission_classes=[IsAdminUser]
    authentication_classes=[SessionAuthentication]
    authentication_classes=[BasicAuthentication]
    # authentication_classes=[TokenAuthentication]
    

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })