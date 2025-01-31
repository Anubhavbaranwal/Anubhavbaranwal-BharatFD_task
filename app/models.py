
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class FAQ(Base):
    __tablename__ = 'faqs'
    id = Column(Integer, primary_key=True, index=True)
    question = Column(Text, nullable=False)
    answer = Column(Text, nullable=False)
    question_hi = Column(Text)
    answer_hi = Column(Text)
    question_bn = Column(Text)
    answer_bn = Column(Text)

    def get_translation(self, lang):
        if lang == 'hi':
            return self.question_hi, self.answer_hi
        elif lang == 'bn':
            return self.question_bn, self.answer_bn
        return self.question, self.answer