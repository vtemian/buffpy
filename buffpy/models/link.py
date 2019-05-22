from buffpy.response import ResponseObject


PATHS = {
    "GET_SHARES": "links/shares.json?url={}"
}


class Link(ResponseObject):
    """
        A link represents a unique URL that has been shared through Buffer.
    """

    def __init__(self, api, url):
        shares = api.get(url=PATHS["GET_SHARES"] % url)["shares"]

        super().__init__({"shares": shares, "url": url})

        self.api = api
        self.shares = []

    def get_shares(self):
        """
            Returns an object with a the numbers of shares a link has had using
            Buffer.

            www will be stripped, but other subdomains will not.
        """

        url = PATHS["GET_SHARES"].format(self.url)
        self.shares = self.api.get(url=url)["shares"]

        return self.shares
