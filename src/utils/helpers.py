import re
from datetime import datetime
from src.utils.custom_exceptions import (UnexpectedMonthError, UnexpectedYearError)


def is_valid_url(url):
    # Define the regex pattern to capture the year and month values
    pattern = r'yellow_tripdata_(\d{4})-(\d{2})\.parquet'

    # Use re.search to find the match
    match = re.search(pattern, url)

    if match:
        year = match.group(1)  # Capture group for year
        month = match.group(2)  # Capture group for month

        current_year = datetime.now().year
        current_month = datetime.now().month

        if year > current_year:
            message = "Year cannot be greater than the current year"
            self.log_message(message=message, level="error")
            raise UnexpectedYearError(message)

        elif int(month) > current_month:
            message = "Month cannot be greater than the current month"
            self.log_message(message=message, level="error")
            raise UnexpectedMonthError(message)

        elif not (1 >= int(month) <= 12):
            raise ValueError("Invalid month number as input, month number needs to between 1 and 12")

        else:
            return True

    else:
        return False