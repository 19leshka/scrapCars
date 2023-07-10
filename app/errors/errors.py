import json


class BaseErrResp(Exception):
    def __init__(self, status: int, title: str, details: list) -> None:
        self.__status = status
        self.__title = title
        self.__detail = details

    def gen_err_resp(self):
        response = {
            "type": "about:blank",
            "title": self.__title,
            "status": self.__status,
            "detail": self.__detail
        }
        return json.dumps(response), self.__status


class InternalError(BaseErrResp):
    def __init__(self, details: list):
        super(InternalError, self).__init__(500, 'Internal Error', details)
