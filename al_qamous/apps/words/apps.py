"""AppConf for al_qamous.apps.words"""

from django.apps import AppConfig


# Create your AppConf here.
class WordsConfig(AppConfig):
    """App Configuration for al_qamous.apps.words"""

    label = "al_qamous_words"
    name = "al_qamous.apps.words"
    default_auto_field = "django.db.models.BigAutoField"
