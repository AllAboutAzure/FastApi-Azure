"""Module to fetch the secret and assign it as environment variable"""
import os
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from .constants import KEYVAULT_NAME

KEYVAULT_URL = f"https://{KEYVAULT_NAME}.vault.azure.net/"

# Set up the credentials using Managed Identity
credential = DefaultAzureCredential()

# Create a secret client to interact with the Key Vault
secret_client = SecretClient(vault_url=KEYVAULT_URL, credential=credential)

# Function to fetch secrets from Key Vault and set them as environment variables
def load_secrets(secret_list):
    """This is used to get the secrets from keyvault"""
    for secret_name in secret_list:

        os.environ[secret_name] =  secret_client.get_secret(secret_name).value
        print(os.environ[secret_name])
