import requests

from utilities.constants import Constants

class BaseTest():
    @staticmethod
    def get_public_ip() -> str:
        """Function to retrieve public IP address.

        Returns:
            str: Public IP address.
        """
        return requests.get(
            "http://checkip.amazonaws.com",
            timeout=40,
            headers={"User-Agent": Constants.AUTOMATION_USER_AGENT},
        ).text.rstrip()
