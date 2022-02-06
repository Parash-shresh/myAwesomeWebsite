from django.urls import path

from django.contrib import admin



from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    #path("", views.shopIndex, name=""),
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="AboutUS"),
    path("contact/", views.contact, name="ContactUS"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("productView/", views.productView, name="ProductViews"),
    path("checkout/", views.checkout, name="checkout"),

]