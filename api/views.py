from django.shortcuts import render
from rest_framework import generics
from .serializers import (BarterSerializer,UserSerializer,RegisterSerializer,AboutClothSerializer)
from .models import (Barter,AboutCloth,UserManager,User)
from rest_framework import generics,mixins,viewsets,status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.permissions import AllowAny

# Create your views here

class RegisterView(viewsets.GenericViewSet,mixins.CreateModelMixin):
    serializer_class=RegisterSerializer
    queryset=User.objects.all()


class LoggedInUserView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

class BlacklistTokenView(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        try:
            refresh_token=request.data["refresh_token"]
            token=RefreshToken(refresh_token)
            token.blacklist()
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
            
class  BarterList(generics.ListAPIView):
    queryset= Barter.objects.all()
    serializer_class= BarterSerializer

    '''def get_queryset(self):
        queryset= Donor.objects.all()
        bg = self.request.query_params.get('bg')
        if bg is not None:
            queryset= queryset.filter(blood_group=bg)
        return queryset'''

class BarterCreate(generics.CreateAPIView):
    queryset = Barter.objects.all()
    serializer_class=BarterSerializer

class AboutClothCreate(generics.CreateAPIView):
    queryset = AboutCloth.objects.all()
    serializer_class=AboutClothSerializer

class AboutClothList(generics.CreateAPIView):
    queryset = AboutCloth.objects.all()
    serializer_class=AboutClothSerializer    

class AboutClothDetail(generics.RetrieveAPIView):
    queryset =AboutCloth.objects.all()
    serializer_class = AboutClothSerializer    

class AboutClothDelete(generics.RetrieveDestroyAPIView):
    queryset = AboutCloth.objects.all()
    serializer_class =AboutClothSerializer  

class BarterDetail(generics.RetrieveAPIView):
    queryset =Barter.objects.all()
    serializer_class = BarterSerializer

class BarterUpdate(generics.RetrieveUpdateAPIView):
    queryset = Barter.objects.all()
    serializer_class = BarterSerializer

class BarterDelete(generics.RetrieveDestroyAPIView):
    queryset = Barter.objects.all()
    serializer_class = BarterSerializer
    
