from .views import (AboutClothCreate,AboutClothDelete,AboutClothDetail,AboutClothList,BarterList,BarterCreate,BarterDetail,BarterUpdate,BarterDelete,LoggedInUserView,BlacklistTokenView,RegisterView)
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)
from email.mime import base

router=DefaultRouter()
router.register('register',RegisterView,basename='register')
urlpatterns = [
    path('',include(router.urls)),
    path('barter/', BarterList.as_view()),
    path('barter/<int:pk>/', BarterDetail.as_view()),
    path('barter/register/', BarterCreate.as_view()),
    path('barter-update/<int:pk>/', BarterUpdate.as_view()),
    path('barter-delete/<int:pk>/', BarterDelete.as_view()),
    path('aboutcloth/', AboutClothList.as_view()),
    path('aboutcloth/<int:pk>/', AboutClothDetail.as_view()),
    path('aboutcloth/create/', AboutClothCreate.as_view()),
    path('aboutcloth-delete/<int:pk>/',AboutClothDelete.as_view()),
    
    path('api/token/',TokenObtainPairView.as_view(),name="token_obtain"),
    path('api/token/refresh/',TokenRefreshView.as_view(),name="refresh_token"),
    #path('create/', RegisterView.as_view(), name="create_user"),
    path('logout/blacklist/', BlacklistTokenView.as_view(),
         name='blacklist'),
    path('current-user/', LoggedInUserView.as_view(), name='currentuser'),   
]