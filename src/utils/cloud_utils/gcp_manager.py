from google.cloud import storage
from src.utils.base_classes.base_downloader import BaseDownloader


class GCPManager(BaseDownloader):

    def __init__(self):
        super().__init__()

    def upload_to_cloud_storage(self, bucket_name, source_file_path, destination_blob_name):

        try:

            client = storage.Client()
            bucket = client.bucket(bucket_name)
            blob = bucket.blob(destination_blob_name)
            message = f"Upload file {source_file_path} into bucket {bucket_name}"
            self.log_message(message=message, level="info")
            blob.upload_from_filename(source_file_path)

        except Exception as e:
            self.log_message(message=f"{e}", level="error")

    def download_from_cloud_storage(self, bucket_name, source_blob_name, destination_file_path):
        client = storage.Client()
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(source_blob_name)
        blob.download_to_filename(destination_file_path)
