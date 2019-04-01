from django.contrib import admin
from django.urls import path

from tb_tutorial.views import TutorialBotView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('webhooks/tutorial/', TutorialBotView.as_view()),
]
