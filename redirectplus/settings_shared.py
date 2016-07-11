# flake8: noqa
# Django settings for redirectplus project.
import os.path
from ccnmtlsettings.shared import common

project = 'redirectplus'
base = os.path.dirname(__file__)
locals().update(common(project=project, base=base))

PROJECT_APPS = [
    'redirectplus.main',
]

USE_TZ = True
USE_I18N = True

THUMBNAIL_SUBDIR = "thumbs"

MEDIA_ROOT = 'uploads'

INSTALLED_APPS += [  # noqa
    'lti_provider',
]

LTI_TOOL_CONFIGURATION = {
    'title': '',
    'description': '',
    'launch_url': 'lti/',
    'embed_url': '',
    'embed_icon_url': '',
    'embed_tool_id': ''
}

LTI_EXTRA_PARAMETERS = [
    'custom_url',
    'resource_link_title',
    'custom_canvas_course_id',
    'custom_canvas_user_login_id',
    'roles'
]
