def _check_for_inception(root_dict: dict):
    """
    Used to check if there is a dict in a dict
    """

    return {
        key: ResponseObject(response)

        for key, response in root_dict.items()
        if isinstance(response, dict)
    }


class ResponseObject(dict):
    """
    Simple data structure that convert any dict to an empty object
    where all the atributes are the keys of the dict, but also preserve a dict
    behavior
    e.g:

        obj = ResponseObject({"a":"b"})
        obj.key = "value"

        obj.a   => "b"
        ob      => {"a": "b", "key": "value"}
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__dict__ = _check_for_inception(self)
