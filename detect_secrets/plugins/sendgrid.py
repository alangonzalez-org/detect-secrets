"""
This plugin searches for SendGrid API keys
"""
import re

from detect_secrets.plugins.base import RegexBasedDetector


class SendGridDetector(RegexBasedDetector):
    """Scans for SendGrid API keys."""
    secret_type = 'SendGrid API Key'

    denylist = [
        # SendGrid API key
        # ref. https://d2w67tjf43xwdp.cloudfront.net/Classroom/Basics/API/what_is_my_api_key.html
        re.compile(r'SG\.[a-zA-Z0-9_-]{22}\.[a-zA-Z0-9_-]{43}'),
    ]
