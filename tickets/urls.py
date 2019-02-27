from django.urls import path
from tickets import views


urlpatterns = [
    path('book_ticket', views.book_ticket, name = 'book_ticket'),
    path('ticket_list', views.ticket_list, name = 'ticket_list'),
    path('create_ticket', views.create_ticket, name = 'create_ticket'),
    path('my_info', views.my_info, name = 'my_info'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('mock', views.mock, name='mock'),
]