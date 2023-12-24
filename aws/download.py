import requests
 
def download_file(file):
  res = requests.get(f'https://data.gharchive.org/{file}')
  print(res.status_code)
  return res