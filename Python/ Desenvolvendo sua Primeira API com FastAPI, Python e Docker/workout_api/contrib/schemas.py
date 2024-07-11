from pydantic import BaseModel


class BaseSchemas(BaseModel):
    class config:
        extra = 'forbid' # significa que não aceita campo extra
        from_attributes = True # server para comverter 
        


