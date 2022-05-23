from pydantic import BaseModel, Field

class UserBase(BaseModel):
    email: str = Field(
        ...,
        example="myemail@example.com"
    )
    username:str = Field(
        ...,
        min_length=3,
        max_length=50,
        example="ExampleUserName"
    )

class User(UserBase):
    id: int = Field(
        ...,
        example="1"
    )


class UserRegister(UserBase):
    password: str = Field(
        ...,
        min_length=8,
        max_length=50,
        example="thisIsAStrongPassword123"
    )