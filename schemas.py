from pydantic import BaseModel

class BookingCreate(BaseModel):
    slot_id: int
    user_name: str
    user_email: str