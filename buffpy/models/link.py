from buffpy.response import ResponseObject


PATHS = {
    "GET_SHARES": "links/shares.json?url={}"
}


class Link(ResponseObject):
    """
        A link represents a unique URL that has been shared through Buffer.
    """

    def __init__(self, api, url):
        super().__init__({"url": url})
        self.api = api

        self.get_shares()

    def get_shares(self):
        """
            Returns an object with a the numbers of shares a link has had using
            Buffer.

            www will be stripped, but other subdomains will not.
        """

        url = PATHS["GET_SHARES"].format(self.url)
        self.shares = self.api.get(url=url).get("shares", [])

        return self.shares
