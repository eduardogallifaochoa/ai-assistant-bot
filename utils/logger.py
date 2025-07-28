import logging

# Configure logger
logger = logging.getLogger("ai-assistant-bot")
logger.setLevel(logging.ERROR)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)

# Add handler
logger.addHandler(console_handler)
