from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from api.views.employee import EmployeeView
from api.views.menu import MenuView
from api.views.restaurant import RestaurantView
from api.views.vote import VoteView

urlpatterns = {
    path('employee/', EmployeeView.as_view(), name='employee'),
    path('restaurant/', RestaurantView.as_view(), name='restaurant'),
    path('menu/', MenuView.as_view(), name='menu'),
    path('menu/today/', MenuView.today, name='menu-today'),
    path('vote/', VoteView.as_view(), name='vote'),
    path('vote/today-result/', VoteView.today_result, name='vote-today-result')
}

urlpatterns = format_suffix_patterns(urlpatterns)
