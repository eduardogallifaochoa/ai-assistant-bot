import sys
import os
import pytest

# Add project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from services.openai_service import OpenAIChatBot

def test_openai_chatbot_instance(monkeypatch):
    # Mock the OPENAI_API_KEY to avoid needing a real one
    monkeypatch.setenv("OPENAI_API_KEY", "fake-key")
    bot = OpenAIChatBot()
    assert isinstance(bot, OpenAIChatBot)
