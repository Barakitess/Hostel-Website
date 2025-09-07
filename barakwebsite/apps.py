from django.conf import settings
import mongoengine
from django.apps import AppConfig

class BarakwebsiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'barakwebsite'

    def ready(self):
        mongoengine.connect(**settings.MONGODB_SETTINGS)