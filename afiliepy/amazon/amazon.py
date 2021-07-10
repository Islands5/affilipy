import urllib.request
import urllib.parse

class NoRedirection(urllib.request.HTTPErrorProcessor):
    def http_response(self, request, response):
        return response
    https_response = http_response

def replace(url, your_key):
    """
    change simple format your affiliate link.
    https://affiliate.amazon.co.jp/help/node/topic/GP38PJ6EUR6PFBEC
    """
    target_url = get_target_url(url)
    params = { 'language':'ja_JP','tag': your_key }
    url_parts = list(urllib.parse.urlparse(target_url))
    url_parts[4] = urllib.parse.urlencode(params) # 4 is query

    return urllib.parse.urlunparse(url_parts)

def get_target_url(url):
    req = urllib.request.Request(url, method="HEAD")
    opener = urllib.request.build_opener(NoRedirection)
    resp = opener.open(req)
    if resp.status == 301:
      url = resp.headers['Location']
    else:
      url = resp.url
    return url