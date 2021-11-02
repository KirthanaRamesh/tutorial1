
from django.urls import path
from advisorapi import views
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
   path('user/register', views.user_list),
   path('user/login', views.user_login),
   path('user/<int:userid>/advisor',views.user_advisor_list),
   path('user/<int:userid>/advisor/<int:advisorid>',views.user_advisor_booking_list),
   path('user/<int:userid>/advisor/booking',views.user_advisor_booked_list),
   path('user/advisor/booking',views.advisor_booked_list),
   path('admin1/advisor/',views.advisor_list),
   path('api/token',jwt_views.TokenObtainPairView.as_view(),
   name='token_obtain_pair'),
    path('api/token/refresh/',
         jwt_views.TokenRefreshView.as_view(),
         name ='token_refresh'),
]

# user_advisor_booked_full_list