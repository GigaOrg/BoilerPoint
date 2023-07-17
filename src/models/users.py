from pydantic import BaseModel, ValidationError


class User(BaseModel):

    
    chat_id: int 
    full_name: str = ''
    gender: bool = None
    user_state: str = ''
    age: int 
    balance: int = 0

    