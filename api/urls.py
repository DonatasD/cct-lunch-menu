from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import EmployeeView, RestaurantView

urlpatterns = {
    path('employee/', EmployeeView.as_view(), name='employee'),
    path('restaurant/', RestaurantView.as_view(), name='restaurant')
}

urlpatterns = format_suffix_patterns(urlpatterns)
