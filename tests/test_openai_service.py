import sys
import os
import pytest

# Add project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from services.openai_service import OpenAIChatBot

def test_openai_chatbot_instance():
    bot = OpenAIChatBot()
    assert isinstance(bot, OpenAIChatBot)
