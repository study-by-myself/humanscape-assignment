
from datetime import date, datetime
from typing import List, Optional

from sqlalchemy.sql.expression import insert

from pydantic import BaseModel

class TrialBase(BaseModel):
    period         : Optional[str] = None
    stage          : Optional[str] = None
    subjects_count : Optional[int] = None


class TrialCreate(TrialBase):
    pass


class Trial(TrialBase):
    id          : int
    name        : str
    trial_id    : str
    scope       : str
    category    : str
    institution : str
    department  : str
    created_at  : datetime
    update_at   : datetime
    request_at  : datetime

    class Config:
        orm_mode = True