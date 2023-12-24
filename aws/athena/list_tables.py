import boto3
import os
#python -m pip install boto3 
#python3 -m pip install boto3
#pip install boto3
 
os.environ.setdefault('AWS_DEFAULT_REGION', 'us-east-1')
 
athena_client = boto3.client('athena')
 
# Get metadata for all tables in given database
athena_client.list_table_metadata
 
athena_client.list_table_metadata(
    CatalogName='AwsDataCatalog',
    DatabaseName='mydb'
)
 
tables = athena_client.list_table_metadata(
    CatalogName='AwsDataCatalog',
    DatabaseName='mydb')
 
type(tables)
 
tables['TableMetadataList']
 
[table['Name'] for table in tables['TableMetadataList']]
 
# Get metadata for a given table in given database
athena_client.get_table_metadata
 
athena_client.get_table_metadata(
    CatalogName='AwsDataCatalog',
    DatabaseName='mydb',
    TableName='custs_txt'
)
 
table_metadata = athena_client.get_table_metadata(
    CatalogName='AwsDataCatalog',
    DatabaseName='mydb',
    TableName='structuredata'
)
 
table_metadata
 
table_metadata['TableMetadata']['TableType']
 
table_metadata['TableMetadata']['Columns']
 
table_metadata['TableMetadata']['Parameters']['location']
 
# Processing metadata of all the tables returned by list_table_metadata
tables = athena_client.list_table_metadata(
    CatalogName='AwsDataCatalog',
    DatabaseName='mydb'
)
 
[table['Parameters']['location'] for table in tables['TableMetadataList']]