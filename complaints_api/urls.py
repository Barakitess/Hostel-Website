from django.urls import path
from .views import RegisterComplaintView, AllComplaintsView, ComplaintDetailView

urlpatterns = [
    path('register/', RegisterComplaintView.as_view(), name='register_complaint'),
    path('all/', AllComplaintsView.as_view(), name='all_complaints'),
    path('detail/<int:pk>/', ComplaintDetailView.as_view(), name='complaint_detail'),
]
