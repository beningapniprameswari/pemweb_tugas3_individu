from sqlalchemy import Column, Integer, String, Text
from database import Base

class Review(Base):
    __tablename__ = "review"
    __allow_unmapped__ = True

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text)
    sentiment = Column(String)
    keypoints = Column(Text)

