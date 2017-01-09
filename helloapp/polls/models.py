# Import the 'models' package.
from django.db import models


# Create the class to describe the model.
class Message(models.Model):
    """Stores messages for our bottles."""

    message = models.CharField(max_length=120)
    is_read = models.BooleanField(default=False)

    class Meta:
        # Set the table name.
        db_table = 'messages'

    # Define what to output when the model is printed as a string.
    def __str__(self):
        # Return the message.
        return self.messages
