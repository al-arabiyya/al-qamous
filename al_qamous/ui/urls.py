"""URLConf for al_qamous.ui"""

from django.urls import path

from al_qamous.ui import views

# Create your URLConf here.
app_name = "al_qamous"

urlpatterns = [
    path("search/", views.SearchView.as_view(), name="search"),
]
