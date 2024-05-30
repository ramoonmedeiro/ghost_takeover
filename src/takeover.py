from src.settings import Settings
import dns.resolver
import random
import requests
import json
from colorama import Fore
import urllib3

# Suprimir avisos de verificação SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Takeover:
    def __init__(self):
        self.user_agent = random.choice(Settings.USER_AGENT.value)
        self.path = "../fingerprints/fingerprints.json"
        self.fingerprints = json.load(open(self.path))

    def get_cname(self, url: str):

        """
        This function is responsible for getting the CNAME of a given URL.

        Parameters
        ----------
        url : str
            The URL to get the CNAME.

        Returns
        -------
        str
            The CNAME of the given URL.
        """
        try:
            resolver = dns.resolver.Resolver()
            answer = resolver.resolve(url, 'CNAME')
            for rdata in answer:
                return rdata.to_text()
        except (dns.resolver.NoAnswer,
                dns.resolver.NXDOMAIN,
                dns.exception.Timeout
                ):
            return None

    def get_http_response(self, url: str):

        """
        This function is responsible for getting the HTTP response of a given URL.

        Parameters
        ----------
        url : str
            The URL to get the HTTP response.

        Returns
        -------
        str
            The HTTP response of the given URL.

        int
            The status code of the given URL.
        """

        headers = {
            "User-Agent": self.user_agent
        }

        try:
            response = requests.get(
                url=url,
                headers=headers,
                timeout=10,
                verify=False
            )
            return response.text, response.status_code
        except requests.RequestException:
            return None, None

    def is_vulnerable(self, url: str):

        """
        This function is responsible for checking if a given URL is vulnerable to subdomain takeover.

        Parameters
        ----------
        url : str
            The URL to check if it is vulnerable to subdomain takeover.

        fingerprints : list
            A list of fingerprints to check if the given URL is vulnerable to subdomain takeover.

        Returns
        -------
        bool
            True if the given URL is vulnerable to subdomain takeover, False otherwise.

        str
            The service that the given URL is vulnerable to subdomain takeover.

        str
            The discussion of the given URL is vulnerable to subdomain takeover.
        """

        cname = self.get_cname(url)
        if cname:
            for fingerprint in self.fingerprints:
                if cname in fingerprint["cname"]:
                    return fingerprint["vulnerable"], fingerprint["service"], fingerprint["discussion"]

        content, sc = self.get_http_response("https://" + url)
        if content:
            for fingerprint in self.fingerprints:
                if fingerprint["fingerprint"] in content:
                    return fingerprint["vulnerable"], fingerprint["service"], fingerprint["discussion"]
        if content is None and sc is None:
            return None, None, None

        return False, None, None
