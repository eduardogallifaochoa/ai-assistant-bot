from services.openai_service import OpenAIChatBot
from utils.logger import logger

def main():
    logger.info("Starting AI Assistant Bot...")
    bot = OpenAIChatBot()
    
    print("Welcome to AI Assistant Bot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Bot: Goodbye!")
            break
        response = bot.get_response(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()
