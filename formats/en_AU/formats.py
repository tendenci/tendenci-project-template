"""
    See https://docs.djangoproject.com/en/5.2/ref/settings/#format-module-path
    for details about these settings.
    They are used by **templates** to enable localisation of
    various region-specific settings
"""

DATE_FORMAT = "d M Y" # 25 Oct 2006
DATETIME_FORMAT = "d M Y, h:i A" # 25 Oct 2006 02:40pm
FIRST_DAY_OF_WEEK = 1 # Monday
MONTH_DAY_FORMAT = "d M" # 25 Oct
SHORT_DATE_FORMAT = "d/m/Y" # 25/10/2006
SHORT_DATETIME_FORMAT = "d/m/Y h:i A" # 25/10/2006 02:40pm
TIME_FORMAT = "h:i A" # 02:40pm
YEAR_MONTH_FORMAT = "M Y" # October 2006
DATE_INPUT_FORMATS = [
    "%d/%m/%Y",  # '25/10/2006'
    "%d/%m/%y",  # '25/10/06'
    "%d %b %Y",  # '25 Oct 2006'
    "%d %b, %Y",  # '25 Oct, 2006'
    "%d %B %Y",  # '25 October 2006'
    "%d %B, %Y",  # '25 October, 2006'
    "%Y-%m-%d",  # '2006-10-25'
]

DATETIME_INPUT_FORMATS = [
    "%d/%m/%Y %H:%M:%S",  # '25/10/2006 14:30:59'
    "%d/%m/%Y %H:%M:%S.%f",  # '25/10/2006 14:30:59.000200'
    "%d/%m/%Y %H:%M",  # '25/10/2006 14:30'
    "%d/%m/%y %H:%M:%S",  # '25/10/06 14:30:59'
    "%d/%m/%y %H:%M:%S.%f",  # '25/10/06 14:30:59.000200'
    "%d/%m/%y %H:%M",  # '25/10/06 14:30'
    "%Y-%m-%d %H:%M:%S",  # '2006-10-25 14:30:59'
    "%Y-%m-%d %H:%M:%S.%f",  # '2006-10-25 14:30:59.000200'
    "%Y-%m-%d %H:%M",  # '2006-10-25 14:30'
]

TIME_INPUT_FORMATS = [
    "%H:%M",  # '14:30'
    "%I:%M %p",  # '02:30 PM'
    "%H:%M:%S",  # '14:30:59'
    "%H:%M:%S.%f",  # '14:30:59.000200'
]
