from django.contrib.auth import authenticate, get_user_model, login  # Import login
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
import logging

logger = logging.getLogger('taskmanager')

User = get_user_model()

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        logger.debug(f"Attempting to log in with email: {email}")
        logger.debug(f"Received email: {email}")  # Log received email
        logger.debug(f"Received password: {password}") 
        
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)  # Use login here
            token, created = Token.objects.get_or_create(user=user)  
            logger.debug(f"Token created: {created}") # Generate token
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            logger.warning(f"Login failed for email: {email}")
            return Response({'non_field_errors': ['Invalid credentials']}, status=status.HTTP_400_BAD_REQUEST)

class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)
