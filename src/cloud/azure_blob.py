from azure.storage.blob import BlobServiceClient
from src.config.settings import settings

blob_service = BlobServiceClient.from_connection_string(
    settings.AZURE_BLOB_CONNECTION_STRING
)

container = blob_service.get_container_client(
    settings.AZURE_BLOB_CONTAINER
)


def read_blob(path: str):

    blob = container.get_blob_client(path)

    return blob.download_blob().readall().decode("utf-8")