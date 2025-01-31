from sqlalchemy import Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from googletrans import Translator
from .redis_client import redis_client

Base = declarative_base()

class FAQ(Base):
    __tablename__ = 'faqs'
    id = Column(Integer, primary_key=True, index=True)
    question = Column(Text, nullable=False)
    answer = Column(Text, nullable=False)

    def get_translation(self, lang):
        cache_key = f"faq:{self.id}:{self.question}:translation:{lang}"
        cached_translation = redis_client.get(cache_key)
        if cached_translation:
            question, answer = cached_translation.split('|')
            return question, answer

        translator = Translator()
        if lang and lang != 'en':
            question = translator.translate(self.question, dest=lang).text
            answer = translator.translate(self.answer, dest=lang).text
            redis_client.setex(cache_key, 3600, f"{question}|{answer}")
            return question, answer

        return self.question, self.answer