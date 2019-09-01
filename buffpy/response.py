from typing import Any


def _check_for_inception(node: Any):
    """
    Used to check if there is a dict in a dict
    """

    if isinstance(node, list):
        return [
            _check_for_inception(item)
            for item in node
        ]

    if isinstance(node, dict):
        return {
            key: ResponseObject(item) if isinstance(item, dict) else item
            for key, item in node.items()
        }

    return node


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

    def __setattr__(self, item, value):
        self[item] = value
        super().__setattr__(item, value)
