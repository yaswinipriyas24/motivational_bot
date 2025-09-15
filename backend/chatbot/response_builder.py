import random

# List of greetings
greetings = [
    "hello", "hi", "hey", "good morning", "good evening"
]

# Example list of responses per value
value_responses = {
    "empathy": [
        "It's okay to feel this way. You're not alone.",
        "Be kind to yourself. Small steps lead to progress.",
        "Everyone struggles sometimes. Keep going!"
    ],
    "well_being": [
        "Taking care of your health is the first step to happiness.",
        "A balanced life helps you stay strong and resilient.",
        "Small habits build a better tomorrow."
    ],
    "compassion": [
        "Reach out to someone you trust. Sharing helps.",
        "Compassion towards yourself is just as important as towards others.",
        "You have the strength to overcome this challenge."
    ],
    "trust": [
        "Believe in yourself. You've handled difficulties before.",
        "Trust grows when you take action, even if small.",
        "Your efforts are noticed and appreciated."
    ],
    "discipline": [
        "Stay consistent, even when it's hard.",
        "Discipline turns dreams into achievements.",
        "Every effort counts towards your goal."
    ],
    "responsibility": [
        "Taking responsibility empowers you.",
        "You are capable of making a difference.",
        "Face your challenges with courage and purpose."
    ],
    "general": [
        "I'm here to support you no matter what.",
        "Let's take this one step at a time together.",
        "Every new day is a fresh start."
    ]
}

# Example motivational stories
motivational_stories = [
    "Once there was a small seed buried in the soil. It struggled against the earth but kept growing, reaching for the sun. Eventually, it blossomed into a beautiful tree.",
    "A young boy failed many times but never gave up. With each attempt, he learned something new and finally achieved his dreams.",
    "A traveler lost his way but met strangers who helped him find his path. Kindness turned a challenge into an opportunity.",
    "A girl dreamed of touching the stars. Even when everyone doubted her, she studied hard and worked with passion. Her persistence made the impossible possible.",
    "A man faced difficulties every day, but instead of giving up, he smiled and took one step forward. His positive attitude changed his life.",
    "An old craftsman taught a child that greatness comes from patience and practice. The child’s determination led to mastery over time.",
    "During a storm, a sailor kept steering his ship with courage. He knew calm seas are not promised, but persistence is his strength.",
    "A family helped each other rebuild their home after a disaster. Together, they learned that unity is the greatest power one can have."
]

# Track previous replies and counts to detect repetition
previous_replies = {}
repeat_counter = {}

def build_response(problem_key, values, values_data, user_input):
    global previous_replies, repeat_counter
    
    # Check if the user input is a greeting
    if any(word in user_input.lower() for word in greetings):
        return "Hello! 👋 I'm here to motivate and support you. Tell me what's on your mind or any problem you're facing.", ""

    responses = []
    
    # Initialize repeat counter if not present
    if problem_key not in repeat_counter:
        repeat_counter[problem_key] = 0
    repeat_counter[problem_key] += 1
    
    for value in values:
        possible = value_responses.get(value, ["Stay positive."])
        
        # Get last reply to avoid repetition
        last_reply = previous_replies.get(value)
        
        # Filter out last reply if possible
        filtered = [r for r in possible if r != last_reply]
        
        # If all are same, fallback to original list
        if not filtered:
            filtered = possible
        
        reply = random.choice(filtered)
        responses.append(reply)
        
        # Update last reply
        previous_replies[value] = reply

    final_message = " ".join(responses)
    quote = ""

    # If repeated more than once, add a story instead of simple replies
    if repeat_counter[problem_key] > 1:
        story = random.choice(motivational_stories)
        final_message = story
        quote = "Keep believing in yourself!"
    else:
        quote = random.choice(motivational_stories)  # Add one quote on first interaction

    return final_message, quote
