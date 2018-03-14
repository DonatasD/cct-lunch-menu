from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import EmployeeView

urlpatterns = {
    path('employee/', EmployeeView.as_view(), name='employee'),
}

urlpatterns = format_suffix_patterns(urlpatterns)
