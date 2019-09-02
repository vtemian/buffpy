from buffpy.response import ResponseObject


PATHS = {
    "GET_PROFILE": "profiles/{}.json",
    "GET_PROFILES": "profiles.json",
    "GET_SCHEDULES": "profiles/{}/schedules.json",
    "UPDATE_SCHEDULES": "profiles/{}/schedules/update.json"
}


class Profile(ResponseObject):
    """
        A Buffer profile represents a connection
        to a single social media account.
    """

    def __init__(self, api, raw_response):
        super(Profile, self).__init__(raw_response)

        self.api = api
        self.__schedules = None

    @property
    def schedules(self):
        """
            Returns details of the posting schedules associated with a social
            media profile.
        """

        url = PATHS["GET_SCHEDULES"].format(self.id)

        self.__schedules = self.api.get(url=url)

        return self.__schedules

    @schedules.setter
    def schedules(self, schedules: dict):
        """
            Set the posting schedules for the specified social media profile.
        """

        url = PATHS["UPDATE_SCHEDULES"].format(self.id)

        data_format = "schedules[0][{}][]={}&"
        post_data = []

        for format_type, values in list(schedules.items()):
            for value in values:
                post_data.append(data_format.format(format_type, value))

        self.api.post(url=url, data="".join(post_data))

    @property
    def updates(self):
        from buffpy.managers.updates import Updates
        return Updates(api=self.api, profile_id=self.id)
