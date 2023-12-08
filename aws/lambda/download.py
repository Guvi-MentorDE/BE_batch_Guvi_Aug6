import urllib3

def download(file):
    http = urllib3.PoolManager()
    r = http.request('GET', f'https://data.gharchive.org/{file}')
    #r.data
    print(r.status)
    return r.data

