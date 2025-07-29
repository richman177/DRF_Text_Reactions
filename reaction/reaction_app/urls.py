from django.urls import path
from .views import QuoteListCreateView, AddReactionView

urlpatterns = [
    path('quotes/', QuoteListCreateView.as_view()),
    path('quotes/<int:pk>/react/', AddReactionView.as_view()),
]
