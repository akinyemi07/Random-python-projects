import random

quotes = [
    "Believe you can and you're halfway there.",
    "Your limitation—it’s only your imagination.",
    "Push yourself, because no one else is going to do it for you.",
    "Success doesn’t just find you. You have to go out and get it.",
    "Great things never come from comfort zones."
]

def display_random_quote():
    quote = random.choice(quotes)
    print(f"💡 Motivational Quote:\n{quote}")

display_random_quote()

