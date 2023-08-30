import os
# from django.conf import settings
from django.apps import AppConfig

from gce_portal import fields

APP_DIR = os.path.join(os.path.dirname(__file__))


class GCEIndexConfig(AppConfig):
    name = 'gce_portal'

SEARCH_INDEXES = {
    'gce': {
        'uuid': 'cb2e5415-b5ee-49b0-b46d-3b33d44757a3',
        'name': 'GCE Index',
        'base_templates': 'globus-portal-framework/v2/',
        'tabbed_project': False,
        'access': 'private',
        'template_override_dir': 'gce',
        'description': (
            'Galactic Chemical Evolution (GCE) is a field of astronomy '
            'that studies the origin and evolution of the elements '
            'within galaxies.'
        ),
        'facets': [
          {
            'name': 'Stellar yields',
            'field_name': 'table'
          },
          {
            'name': 'Star formation efficiency',
            'field_name': 'sfe'
          },
        ],
        "fields": [
            ("title", fields.title),
            ("globus_app_link", fields.globus_app_link),
            ("https_url", fields.https_url),
        ],
        "sort": [{"field_name": "table", "order": "asc"},
                 {"field_name": "sfe", "order": "asc"}],
    }
}
