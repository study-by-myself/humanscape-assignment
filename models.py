from datetime import datetime
from sqlalchemy import Column, Integer, String

from sqlalchemy.sql.sqltypes import DateTime

from .database import Base


class Trial(Base):
    __tablename__ = "trials"

    id             = Column(Integer, primary_key=True, autoincrement=True)
    name           = Column(String, unique=False)
    trial_id       = Column(String)
    period         = Column(String)
    scope          = Column(String)
    category       = Column(String)
    institution    = Column(String)
    stage          = Column(String)
    subjects_count = Column(Integer)
    department     = Column(String)
    create_at      = Column(DateTime, default=datetime.now)
    update_at      = Column(DateTime, onupdate=datetime.now)
    request_at     = Column(DateTime, onupdate=datetime.now)