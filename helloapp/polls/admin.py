from django.contrib import admin
# Import our models module.
from polls import models

# Register our "Message" model with the Django Admin/
admin.site.register(models.Message)
