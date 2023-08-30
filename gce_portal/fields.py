from urllib.parse import urlunsplit, urlencode

# Guest Collection UUID where data is stored
COLLECTION_ID = '96c76fb5-c70a-427c-a8d2-ea72eeff200b'

# Result title
# ============
def title(result):
    '''Return the title of the current search result'''
    return result[0]["directory"]


# Globus App Link
# ===============
def globus_app_link(result):
    '''Return the URL to the Globus transfer web app'''

    # Extract the path to the folder where the result is.
    # This must be from the root of the guest collection.
    url = result[0]['directory']

    # Return the full URL that will redirect users to
    # the selected data, using the Globus web app.
    query_params = {'origin_id': COLLECTION_ID,
                    'origin_path':  url}
    return urlunsplit(('https', 'app.globus.org', 'file-manager',
                      urlencode(query_params), ''))


# HTTPS URL
# =========
def https_url(result):
    '''Return a direct download link to files over HTTPS'''
    path = result[0]['directory'] + "/" + result[0]['directory'] + ".npy"
    return urlunsplit(("https", "g-6996b.fd635.8443.data.globus.org", path, "", ""))