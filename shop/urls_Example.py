from django.urls import path

from . import viewsExample



from . import views

urlpatterns = [
    path("", viewsExample.includeFunction, name = "Shoping"),
    # path("/DeleteAfterLearning", viewsExample.includeFunction, name = "jpt")
]

