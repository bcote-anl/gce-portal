// Get Json Data
// =============
async function getJsonData(jsonURL, resourceServer, djangoURL) {
    /* Get Json file via HTTPS request and return its parsed content */
    
    // Define json file properties for fetchAuthenticatedContent()
    let fileJson = {
      'url': jsonURL,
      'mimetype': 'json',
    }
  
    // Get Auth token for the targeted resource server
    var accessToken = null
    try {
      accessToken = await getAccessToken(djangoURL, resourceServer)
    } catch (error) {console.error('Fetching access token failed!', error)}
  
    // Parse and return Json file content
    return data = await fetchAuthenticatedContent(fileJson, accessToken, null)
      .then(response => response.text())
      .then(json => {return JSON.parse(json)})
}
  
