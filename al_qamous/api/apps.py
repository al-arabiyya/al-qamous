"""AppConf for al_qamous.api"""

from django.apps import AppConfig


# Create your AppConf here.
class APIConfig(AppConfig):
    """App Configuration for al_qamous.api"""

    name = "al_qamous.api"
    label = "al_qamous_api"
    default_auto_field = "django.db.models.BigAutoField"
