import urllib3

def download():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://httpbin.org/robots.txt')
    r.data
    # b'User-agent: *\nDisallow: /deny\n'
    print(r.status)
