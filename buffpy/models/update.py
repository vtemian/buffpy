from buffpy.response import ResponseObject


PATHS = {
    "DELETE": "updates/{}/destroy.json",
    "EDIT": "updates/{}/update.json",
    "GET_INTERACTIONS": "updates/{}/interactions.json",
    "GET_UPDATE": "updates/{}.json",
    "MOVE_TO_TOP": "updates/{}/move_to_top.json",
    "PUBLISH": "updates/{}/share.json",
}


class Update(ResponseObject):
    """
        An update represents a single post to a single social media account. An
        update can also include media attachments such as pictures and links.
    """

    def __init__(self, api, id=None, raw_response=None):
        if id and not raw_response:
            raw_response = api.get(url=PATHS["GET_UPDATE"].format(id))

        super().__init__(raw_response)

        self.api = api
        self.__interactions = []

    @property
    def interactions(self):
        """
            Returns the detailed information on individual interactions with the social
            media update such as favorites, retweets and likes.
        """

        url = PATHS["GET_INTERACTIONS"].format(self.id)
        response = self.api.get(url=url)

        self.__interactions = [
            interaction
            for interaction in response["interactions"]
        ]

        return self.__interactions

    def edit(self, text: str, media: dict = None, utc: str = None, now: str = None,
             service_geolocation_id: str = None, service_geolocation_name: str = None):
        """
            Edit an existing, individual status update.
        """

        url = PATHS["EDIT"].format(self.id)

        post_data = ["text={}&".format(text)]

        if now:
            post_data.append("now={}&".format(now))

        if utc:
            post_data.append("utc={}&".format(utc))

        if media:
            media_format = "media[{}]={}&"

            for media_type, media_item in list(media.items()):
                post_data.append(media_format.format(media_type, media_item))

        if service_geolocation_id:
            post_data.append("service_geolocation_id={}&".format(service_geolocation_id))

        if service_geolocation_name:
            post_data.append("service_geolocation_name={}&".format(service_geolocation_name))

        response = self.api.post(url=url, data="".join(post_data))

        return Update(api=self.api, raw_response=response["update"])

    def publish(self):
        """
            Immediately shares a single pending update and recalculates times for
            updates remaining in the queue.
        """

        return self.api.post(url=PATHS["PUBLISH"].format(self.id))

    def delete(self):
        """
            Permanently delete an existing status update.
        """

        return self.api.post(url=PATHS["DELETE"].format(self.id))

    def move_to_top(self):
        """
            Move an existing status update to the top of the queue and recalculate
            times for all updates in the queue. Returns the update with its new
            posting time.
        """

        response = self.api.post(url=PATHS["MOVE_TO_TOP"].format(self.id))
        return Update(api=self.api, raw_response=response)
