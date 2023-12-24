import boto3
import os
 
os.environ.setdefault('AWS_DEFAULT_REGION', 'us-east-1')
 
athena_client = boto3.client('athena')
 
athena_client.list_databases
 
databases = athena_client.list_databases(CatalogName='AwsDataCatalog')
 
type(databases)
print(type(databases['DatabaseList']))
 
[database['Name'] for database in databases['DatabaseList']]