import argparse

def hello(name, lang):
    greetings = {
        "English": "Hello",
        "Spanish": "Hola",
        "French": "Bonjour"
    }
    msg = f"{greetings[lang]} {name}!"
    print(msg)

parser = argparse.ArgumentParser(description="A simple command-line tool to demonstrate argparse.")


#note : the main difference between Input is executed inside the code whereas argparse is executed from the command line.

# parser.add_argument("name", type=str, help="Your name")
# parser.add_argument("--age", type=int, help="Your age", default=0)
# parser.add_argument("--greet", action="store_true", help="Whether to greet the user")
# args = parser.parse_args()
# if args.greet:
#     print(f"Hello, {args.name}!")
# if args.age > 0:
#     print(f"You are {args.age} years old.")

parser.add_argument("-n", "--name", metavar="name", required=True, help="Your name")
parser.add_argument("-l", "--lang", metavar="Language", choices=["English","Spanish","French"], help="Language to greet in (English, Spanish, French)", default="English")


args = parser.parse_args()

hello(args.name, args.lang)

# msg = f"Hello, {args.name}!"
# print(msg)