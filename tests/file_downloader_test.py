from src.modules.file_downloader import FileDownloader
from unittest.mock import MagicMock
from requests_mock import Mocker
import pytest
import requests


class TestFileDownloader:
    file_downloader = FileDownloader()
    test_url = "http://example.com/test-file"

    # Fixture to set up the requests-mock library
    @pytest.fixture
    def requests_mock(self):
        with Mocker() as m:
            yield m

    def test_download_file_success(self, requests_mock):
        # Define the test URL and content
        test_content = b"Test file content"

        # Set up a mock response for a successful download
        requests_mock.get(self.test_url, text=test_content.decode(), status_code=200)

        # Define the destination file name
        dst_file_name = "test_output.txt"

        # Call the download_file function
        self.file_downloader.download_file(self.test_url, dst_file_name)

        # Verify that the file was written successfully
        with open(dst_file_name, "rb") as file:
            content = file.read()
            assert content == test_content

    def test_download_file_http_error(self, requests_mock):

        requests_mock.get(self.test_url, status_code=404)  # Simulate an HTTP error
        dst_file_name = "test_output.txt"

        # Use pytest's `raises` to verify that an HTTPError is raised
        with pytest.raises(requests.exceptions.HTTPError):
            self.file_downloader.download_file(self.test_url, dst_file_name)

    def test_download_file_general_error(self, requests_mock):
        # Define the test URL with a connection error
        test_url = "http://invalid-url-that-will-cause-error"

        # Use pytest's `raises` to verify that a general exception is raised
        with pytest.raises(Exception):
            self.file_downloader.download_file(test_url, "test_output.txt")




