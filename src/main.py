from src.modules.file_downloader import FileDownloader
from src.utils.cloud_utils.gcp_manager import GCPManager
from dotenv import dotenv_values


def main():

    file_downloader = FileDownloader()
    year = "2023"
    month = "07"
    file_downloader.download(
        year=year,
        month=month,
        dst_file_name="yellow_trips_data_{year}-{month}.parquet".format(year=year, month=month)
    )

    config = dotenv_values(".env")
    dst_bucket_name = config.get("DST_BUCKET")
    gcp_manager = GCPManager()

    gcp_manager.upload_to_cloud_storage(
        bucket_name=dst_bucket_name,
        source_file_path="yellow_trips_data_{year}-{month}.parquet".format(year=year, month=month),
        destination_blob_name="yellow_trips_data_{year}-{month}.parquet".format(year=year, month=month)

    )


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
