from django.urls import path
from .views import (
    PerkDetailView,
    PerkDetail,
    Perks,
    ExperienceDetailView,
    ExperienceDetail,
    Experiences,
    ExperienceBookings,
)

urlpatterns = [
    path("perks/", Perks.as_view()),
    path("perks/<int:pk>", PerkDetail.as_view()),
    path("<int:pk>/perks", PerkDetailView.as_view()),
    path("<int:pk>/bookings", ExperienceBookings.as_view()),
    path("experiences/", Experiences.as_view()),
    path("experiences/<int:pk>", ExperienceDetail.as_view()),
    path("<int:pk>/experiences", ExperienceDetailView.as_view()),
]
