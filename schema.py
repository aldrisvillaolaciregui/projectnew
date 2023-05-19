from pydantic import BaseModel


class usuariosBasemodel(BaseModel):
    username:str
    password:str