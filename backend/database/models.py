from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import DateTime

from datetime import datetime

from database.database import Base


class Incident(Base):

    __tablename__ = "incidents"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    timestamp = Column(
        DateTime,
        default=datetime.utcnow
    )

    source = Column(
        String
    )

    anomaly = Column(
        Boolean
    )

    threat_level = Column(
        String
    )

    recommended_action = Column(
        String
    )