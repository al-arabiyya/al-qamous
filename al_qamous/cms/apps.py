"""AppConf for al_qamous.cms"""

from django.apps import AppConfig


# Create your config here.
class CMSConfig(AppConfig):
    """App configuration for al_qamous.cms"""

    name = "al_qamous.cms"
    label = "al_qamous_cms"
    default_auto_field = "django.db.models.BigAutoField"
