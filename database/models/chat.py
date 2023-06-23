from pydantic import BaseModel


class BaseChat(BaseModel):
    chat_id: int


class BaseChatCreate(BaseModel):
    chat_id: int
