
from django.contrib import admin
from django.urls import path, include

from task2.views import func_template, ClassTemplate
from task4.views import index, game, cart
from task5.views import sign_up_by_html, sign_up_by_django

urlpatterns = [
    path('admin/', admin.site.urls),
    path('func/', func_template),
    path('class/', ClassTemplate.as_view()),
    path('platform/', include('task5.urls')),
]
