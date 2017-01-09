from django.conf.urls import url
from polls import views
urlpatterns = [
     url(r'^$', views.MessageView.as_view()),
]
