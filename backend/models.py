from sqlalchemy import Column, Integer, String
from database import Base

class SearchHistory(Base):

    __tablename__ = "search_history"

    id = Column(Integer, primary_key=True, index=True)
    user_prompt = Column(String)
    ai_response = Column(String)