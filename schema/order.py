from pydantic import BaseModel
import enum
from typing import List

class Method(enum.Enum):
    online = "online"
    pay_receive = "pay-receive"


class OrderIn(BaseModel):
    method: Method
    amount: str
    cust_Id: int
    Order_Desc: List[int]

