from pydantic import BaseModel, Field


class BaseChat(BaseModel):
    chat_id: int
    first_name: str
    last_name: str
    username: str
    type: str


class BaseChatCreate(BaseModel):
    chat_id: int


class ChatSchema(BaseModel):
    id: int = Field(...)
    first_name: str = Field(...)
    last_name: str = Field(...)
    username: str = Field(...)
    type: str = Field(...)

    class Config:
        schema_extra = {
            'example': {
                'id': 1234567,
                'first_name': 'John',
                'last_name': 'Doe',
                'username': 'John Doe',
                'type': 'private'
            }
        }
