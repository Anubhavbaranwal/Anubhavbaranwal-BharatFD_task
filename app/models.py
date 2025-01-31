
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from googletrans import Translator


Base = declarative_base()

class FAQ(Base):
    __tablename__ = 'faqs'
    id = Column(Integer, primary_key=True, index=True)
    question = Column(Text, nullable=False)
    answer = Column(Text, nullable=False)

    def get_translation(self, lang):
       translator = Translator()
       if lang and lang != 'en':
           return translator.translate(self.question, dest=lang).text, translator.translate(self.answer, dest=lang).text
       return self.question, self.answer