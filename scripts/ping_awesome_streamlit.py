"""This job pings the awesome-streamlit site regularly to keep it alive

- https://lnx.azurewebsites.net/python-app-on-azure-web-apps-frequently-restarts/
- https://stackoverflow.com/questions/30847090/
django-fastcgi-app-on-azure-frequent-restarts/30854511#30854511
"""
import logging
import time
from typing import Optional

import requests

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)


def ping(url: str = "https://awesome-streamlit.org", sleep_secs: Optional[float] = 600):
    """Pings the url every sleep_secs seconds

    Awesome-streamlit uses this job to keep the web application awake. Cf

    - https://lnx.azurewebsites.net/python-app-on-azure-web-apps-frequently-restarts/
    - https://stackoverflow.com/questions/30847090/
django-fastcgi-app-on-azure-frequent-restarts/30854511#30854511

    Keyword Arguments:
        url {str} -- The site to pint (default: {"https://awesome-streamlit.azurewebsites.net/"})
        sleep_secs {float} -- If None the site will be pinged once.
If not None the site will be pinged every sleeps_seconds seconds (default: {200})

    If we setup multiple tenants later we should change the request to a specific website_instance
    ```python
    cookies = dict(ARRAffinity=website_instance_id)
    response = requests.get(url, cookies)  # type:ignore
    ```
    """
    count = 1
    while count == 1 or sleep_secs:
        logging.info("Request %s sent to %s", count, url)

        response = requests.get(url)
        logging.info(
            "Response %s received, status_code=%s, elapsed=%s",
            count,
            response.status_code,
            response.elapsed,
        )
        text_len = len(response.text)
        logging.info(
            "Response text %s received, len(text)=%s, elapsed=%s",
            count,
            text_len,
            response.elapsed,
        )

        count += 1
        logging.info("Sleeping %s seconds", sleep_secs)
        if sleep_secs:
            time.sleep(sleep_secs)  # type: ignore


if __name__ == "__main__":
    ping(sleep_secs=60)
