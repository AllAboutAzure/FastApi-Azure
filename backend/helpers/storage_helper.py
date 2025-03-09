from azure.storage.blob import BlobServiceClient, BlobClient
from azure.identity import DefaultAzureCredential
import io
import pandas as pd

# Set your Azure Storage account name and container name
account_url = "https://<your-storage-account-name>.blob.core.windows.net"
container_name = "<your-container-name>"
blob_name = "<your-csv-file-name.csv>"

# Use DefaultAzureCredential for authentication (this will work with Azure CLI, Managed Identity, or environment variables)
credential = DefaultAzureCredential()

# Create a BlobServiceClient using the account URL and credential
blob_service_client = BlobServiceClient(account_url=account_url, credential=credential)

# Get the BlobClient for the specific blob (CSV file) you want to fetch
blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

# Download the blob data into memory (as bytes)
blob_data = blob_client.download_blob()
csv_content = blob_data.readall()

# Convert CSV content to a pandas DataFrame (optional, if you need to process the CSV data)
csv_stream = io.BytesIO(csv_content)
df = pd.read_csv(csv_stream)

# Display the DataFrame (optional)
print(df)
#TODO: to be converted as different functions for CRUD operations.