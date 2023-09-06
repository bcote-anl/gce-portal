from django.urls import path, include

# Load function to generate access tokens
from alcf_data_portal.api import get_access_token
api = [
    path('access_token/', get_access_token, name='access_token')
]

urlpatterns = [

    # API to generate access tokens
    path('api/v1/', include(api)),

    # Provides the basic search portal
    path('', include('globus_portal_framework.urls')),
    
    # Provides Login urls for Globus Auth
    path('', include('social_django.urls', namespace='social')),
    
    # Provides urls for GCE portal app
    #path('gce_portal', include('gce_portal.urls', namespace="gce_portal")),
]
