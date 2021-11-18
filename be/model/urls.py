from django.urls import path
from model.views import PredictView

urlpatterns = [
    path('',
         PredictView.as_view({
             "get": "list",
             "post": "create"}),
         name="predict_view")
]
