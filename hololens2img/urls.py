from django.shortcuts import render
from django.urls import path
from . import views


urlpatterns = [
    path("", lambda request: render(request, "index.html")),
    path("ms1/", views.MS1View.as_view(), name="ws1"),
    path("ms2/", views.MS2View.as_view(), name="ws2"),
    path("ms3/", views.MS3View.as_view(), name="ws3"),
    path("ms4/", views.MS4View.as_view(), name="ws4"),
    path("ms5/", views.MS5View.as_view(), name="ws5"),
    path("ms6/", views.MS6View.as_view(), name="ws6"),
    path("wh/", views.WHView.as_view(), name="wh"),
]
