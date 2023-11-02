from dataclasses import dataclass
import requests
import sys
from src.utils.base_classes.base_downloader import BaseDownloader


@dataclass
class FileDownloader(BaseDownloader):

    def __post_init__(self):
        super().__init__()

    def write_to_file(self, dst_file_name, data):
        try:
            with open(dst_file_name, "wb") as file:
                message = f"Writing content data to temporary file {dst_file_name}"
                self.log_message(message=message, level="info")
                file.write(data)

        except Exception as e:
            message = f"{e}"
            self.log_message(message=message, level="error")

    def download_file(self, url: str, dst_file_name: str):
        try:
            message = f"HTTP Get Request for {url}"
            self.log_message(message=message, level="info")

            response = requests.get(url)
            response.raise_for_status()  # Raise HTTPError for non-200 responses

            self.write_to_file(dst_file_name=dst_file_name, data=response.content)

        except requests.exceptions.HTTPError as e:
            message = f"HTTP Error: {e}"
            self.log_message(message=message, level="error")
            raise e  # Re-raise the HTTPError for caller to handle

        except Exception as e:
            message = f"Error: {e}"
            self.log_message(message=message, level="error")
            raise e  # Re-raise the origin
