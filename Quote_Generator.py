import random

print("Welcome to quote generator")
print("Kindly choose '1' for Dream quote")
print("Kindly choose '2' for Achieve quote")
print("Kindly choose '3' for Action quote")
print("Kindly choose '4' for Challenge quote")
print("Kindly choose '5' for Persistent quote")

Dream = [
'"All our dreams can come true, if we have the courage to pursue them." — Walt Disney',
'"The future belongs to those who believe in the beauty of their dreams." — Eleanor Roosevelt',
'"Dreams come true. Without that possibility, nature would not incite us to have them." — John Updike',
'\"Dream as if you \'ll live forever. Live as if you\'ll die today.\" — James Dean',
'"Some men see things as they are and say why. I dream things that never were and say why not." — George Bernard Shaw',
]

Achieve = [
'\"Show me a person who has never made a mistake and I \'ll show you someone who has never achieved much.\" — Joan Collins',
'\"Failure is the condiment that gives success its flavor.\" — Truman Capote',
'\"Success means doing the best with what we have. Success is the doing, not the getting; in the trying, not the triumph. Success is a personal standard, reaching for the highest that is in us, becoming all that we can be.\" — Zig Ziglar',
'\"I long to accomplish a great and noble task, but it is my chief duty to accomplish small tasks as if they were great and noble.\" — Helen Keller',
'\"A man is a success if he gets up in the morning and gets to bed at night, and in between does what he wants to do.\" — Bob Dylan',
]

Action = [
'\"In a moment of decision, the best thing you can do is the right thing to do, the next best thing is the wrong thing, and the worst thing you can do is nothing.\" — Theodore Roosevelt',
'\"Amateurs sit and wait for inspiration, the rest of us just get up and go to work.\" — Stephen King',
'\"You will never plough a field if you only turn it over in your mind.\" — Irish proverb',
'\"Take the first step in faith. You don\'t have to see the whole staircase, just take the first step.\" — Martin Luther King, Jr.',
'\"Don\'t wait. The time will never be just right.\" — Napoleon Hill',
]

Challenge = [
'\"Strength does not come from winning. Your struggles develop your strengths. When you go through hardships and decide not to surrender, that is strength." — Arnold Schwarzenegger',
'\"When you get into a tight place and everything goes against you, till it seems as though you could not hang on a minute longer, never give up then, for that is just the place and time that the tide will turn.\" — Harriet Beecher Stowe',
'\"The best way out is always through.\" — Robert Frost',
'\"It is not the critic who counts; not the man who points out how the strong man stumbles, or where the doer of deeds could have done better. The credit belongs to the man who is actually in the arena, whose face is marred by dust and sweat and blood ... who at the worst, if he fails, at least fails while daring greatly, so that his place shall never be with those cold and timid souls who neither know victory nor defeat.\" — Theodore Roosevelt.',
'\"The greater the obstacle, the more glory in overcoming it.\" — Molière',
]

Persistence = [
'\"The man who moves a mountain begins by carrying away small stones.\" — Confucius',
'\"Failure is success in progress." — Albert Einstein',
'\"If you\'re walking down the right path and you\'re willing to keep walking, eventually you\'ll make progress.\" — Barack Obama',
'\"Without continual growth and progress, such words as improvement, achievement and success have no meaning.\" — Benjamin Franklin',
'\"Great things are not done by impulse, but by a series of small things brought together.\" — Vincent Van Gogh'
]

while True:
    Quotes = [Dream, Achieve, Action, Challenge, Persistence]

    def Quote_Generator():
        while True:
            try:
                global user_input
                user_input = int(input("Pick a number between 1 and 5 to choose your type of quote: ")) - 1
                if 0 <= user_input <= 4:
                    return user_input
                else:
                    print("Pick a number between 1 and 5")
            except:
                print("Pick a number between 1 and 5 using digits")
    Quote_Generator()

    def Quote_Selector():
        selected_quote = Quotes[user_input]
        Quote = random.choice(selected_quote)
        print()
        print(f"Quote: {Quote}")
    Quote_Selector()

    print()
    print("Do you want to hear more quotes")
    user_input_2 = input("Type (Y) for Yes or (N) for No: ")
    print()

    if user_input_2.lower() == 'n':
        print("Have a lovely day")
        break