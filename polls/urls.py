from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path('all/', views.polls_list, name='polls_list'),
    path('<int:question_id>/frequency/', views.frequency, name='frequency'),
    path('add/', views.add, name='add'),
    path('confirm_add/', views.confirm_add, name='confirm_add'),

]