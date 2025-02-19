import random

# Data List
data = [
    {'name': 'Instagram', 'follower_count': 346, 'description': 'Social media platform', 'country': 'United States'},
    {'name': 'Cristiano Ronaldo', 'follower_count': 600, 'description': 'Footballer', 'country': 'Portugal'},
    {'name': 'Selena Gomez', 'follower_count': 430, 'description': 'Singer & Actress', 'country': 'United States'},
    {'name': 'National Geographic', 'follower_count': 280, 'description': 'Nature & Science Media', 'country': 'United States'},
    {'name': 'Dwayne Johnson', 'follower_count': 390, 'description': 'Actor & Former Wrestler', 'country': 'United States'},
    {'name': 'Kim Kardashian', 'follower_count': 350, 'description': 'Reality TV Star & Businesswoman', 'country': 'United States'},
    {'name': 'Lionel Messi', 'follower_count': 480, 'description': 'Footballer', 'country': 'Argentina'},
    {'name': 'NASA', 'follower_count': 100, 'description': 'Space Agency', 'country': 'United States'},
    {'name': 'YouTube', 'follower_count': 200, 'description': 'Video Sharing Platform', 'country': 'United States'},
    {'name': 'Virat Kohli', 'follower_count': 260, 'description': 'Cricketer', 'country': 'India'},
    {'name': 'Kylie Jenner', 'follower_count': 400, 'description': 'Model & Entrepreneur', 'country': 'United States'},
    {'name': 'Beyoncé', 'follower_count': 320, 'description': 'Singer & Performer', 'country': 'United States'},
    {'name': 'Oprah Winfrey', 'follower_count': 100, 'description': 'TV Host & Philanthropist', 'country': 'United States'},
    {'name': 'LeBron James', 'follower_count': 160, 'description': 'Basketball Player', 'country': 'United States'},
    {'name': 'Netflix', 'follower_count': 250, 'description': 'Streaming Service', 'country': 'United States'},
    {'name': 'Shakira', 'follower_count': 170, 'description': 'Singer', 'country': 'Colombia'},
    {'name': 'TikTok', 'follower_count': 300, 'description': 'Social Media Platform', 'country': 'China'},
    {'name': 'Billie Eilish', 'follower_count': 150, 'description': 'Singer & Songwriter', 'country': 'United States'},
    {'name': 'Kevin Hart', 'follower_count': 160, 'description': 'Comedian & Actor', 'country': 'United States'},
    {'name': 'Barack Obama', 'follower_count': 140, 'description': 'Former US President', 'country': 'United States'},
    {'name': 'Justin Bieber', 'follower_count': 290, 'description': 'Singer', 'country': 'Canada'},
    {'name': 'Drake', 'follower_count': 180, 'description': 'Rapper & Singer', 'country': 'Canada'},
    {'name': 'Adidas', 'follower_count': 110, 'description': 'Sports Brand', 'country': 'Germany'},
    {'name': 'Nike', 'follower_count': 180, 'description': 'Sports Brand', 'country': 'United States'},
    {'name': 'PewDiePie', 'follower_count': 110, 'description': 'YouTube Content Creator', 'country': 'Sweden'},
    {'name': 'Taylor Swift', 'follower_count': 330, 'description': 'Singer & Songwriter', 'country': 'United States'},
    {'name': 'Elon Musk', 'follower_count': 190, 'description': 'Entrepreneur', 'country': 'United States'},
    {'name': 'Real Madrid', 'follower_count': 160, 'description': 'Football Club', 'country': 'Spain'},
    {'name': 'FC Barcelona', 'follower_count': 140, 'description': 'Football Club', 'country': 'Spain'},
    {'name': 'Amazon', 'follower_count': 120, 'description': 'E-commerce Platform', 'country': 'United States'}
]
"""
# Game Initialization
print("Welcome to Higher Lower!")

A = random.randint(0, len(data) - 1)
B = random.randint(0, len(data) - 1)

while A == B:
    B = random.randint(0, len(data) - 1)  # Ensure A and B are different

points = 0
game_over = False

# Game Loop
while not game_over:
    print(f"\nCompare A: {data[A]['name']}, {data[A]['description']} from {data[A]['country']}")
    print(f"Against B: {data[B]['name']}, {data[B]['description']} from {data[B]['country']}")

    # Validate user input
    uc = input("Who has more followers? Type 'A' or 'B': ").strip().upper()
    while uc not in ["A", "B"]:
        print("Invalid choice! Please type either 'A' or 'B'.")
        uc = input("Who has more followers? Type 'A' or 'B': ").strip().upper()

    # Determine user choice
    uc = A if uc == "A" else B

    # Check if user guessed correctly
    if data[uc]['follower_count'] >= data[B]['follower_count']:  # Handling equal case too
        points += 1
        A = uc
        B = random.randint(0, len(data) - 1)

        # Ensure A and B are different
        while A == B:
            B = random.randint(0, len(data) - 1)

        print(f"Correct! +1 point. Now you have {points} point{'s' if points > 1 else ''}.")
    else:
        print(f"Wrong! {data[B]['name']} has {data[B]['follower_count']}M followers.")
        print(f"Game Over! You ended with {points} points.")
        game_over = True
## okay i just gave stuff to chat gpt and the code is clearly flawed 
"""

## here is my code with the correct logic and still it needs to be updated

print("Welcome to Higher Lower")

A = random.randint(0, len(data)-1)

B = random.randint(0, len(data)-1)

game_over = False

points = 0


while not game_over:

    while A == B:
        B = random.randint(0, len(data) - 1)


    print(f"Compare A   {data[A]['name']}, {data[A]['description']} from {data[A]['country']}")
    print(f"Against B   {data[B]['name']}, {data[B]['description']} from {data[B]['country']}")


    uc = (input("Who has more followers? Type 'A' or 'B':" )).upper()

    if uc == "A":
        uc = A
    if uc == "B":
        uc = B


    if data[uc]['follower_count'] == max((data[uc]['follower_count']),data[B]['follower_count']):
        points += 1

        A = uc
        B = B = random.randint(0, len(data)-1)
        print("Okay +1 point, now check this")
        print(f"now you have {points} point")
    else:
        print(f"You ended the game with {points} points")
        game_over = True
