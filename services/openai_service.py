from openai import OpenAI
from config.settings import OPENAI_API_KEY, MODEL
from utils.logger import logger

class OpenAIChatBot:
    """
    A simple wrapper around OpenAI's GPT API for chat-based interaction.
    """

    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def get_response(self, prompt: str) -> str:
        """
        Sends the user input to the OpenAI API and returns the response.
        """
        try:
            response = self.client.chat.completions.create(
                model=MODEL,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=200
            )
            reply = response.choices[0].message.content.strip()
            logger.debug(f"AI Response: {reply}")
            return reply
        except Exception as e:
            logger.error(f"Error fetching response: {e}")
            return "Sorry, I encountered an error."
