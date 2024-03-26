from django import template
from datetime import datetime
import pytz

register = template.Library()

@register.filter
def format_timestamp(timestamp):
    """Format a given timestamp into a more readable string."""

    if isinstance(timestamp, str):
        # Parse the ISO format timestamp string
        timestamp = datetime.fromisoformat(timestamp)

    if not isinstance(timestamp, datetime):
        return "Invalid timestamp"

    now = datetime.now()
    if timestamp.date().day == now.date().day and timestamp.date().month == now.date().month:
        return timestamp.astimezone(pytz.timezone('Africa/Cairo')).strftime('%I:%M %p')  # Display only hour and minute if same day
    elif timestamp.date().year == now.date().year:
        return timestamp.astimezone(pytz.timezone('Africa/Cairo')).strftime('%m-%d %I:%M %p')
    else:
        return timestamp.astimezone(pytz.timezone('Africa/Cairo')).strftime('%Y-%m-%d %I:%M %p')
