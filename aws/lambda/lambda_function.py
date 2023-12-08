import json
import os
from download import download

def lambda_handler(event, context):
    # TODO implement
    file = '2015-01-01-15.json.gz'
    
    download_res = download('2015-01-01-15.json.gz')
    print(download_res)
    
    
    return download_res