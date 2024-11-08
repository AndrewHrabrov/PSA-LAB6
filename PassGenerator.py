import argparse
import secrets

parser = argparse.ArgumentParser(
    prog = 'Generator of passwords',
    description = 'Program generate passwords',
    epilog = 'Enter a length of passwords, set of symbols n number of generate passwords'
)

parser.add_argument('-l', '--len',
                    type=int,
                    required=True,
                    choices=range(5, 101),
                    help='length of passwords')

parser.add_argument('-c', '--count',
                    type=int,
                    required=True,
                    choices=range(1, 51),
                    help='Count of passwords')

parser.add_argument('-s', '--set',
                    type=str,
                    required=True,
                    help='Set of symbols, that using in generate passwords! Minimum 10')

args = parser.parse_args()
if len(args.set) < 10:
    parser.print_help()
    exit(0)

class Password:
    def __init__(self, set_symbols):
        self.set_symbols = set_symbols
        self.required_symbols = [secrets.choice(symbol) for symbol in self.set_symbols]

    def generate_password(self, length):
        chars = "".join(self.set_symbols)
        password = "".join(secrets.choice(chars)
                        for _ in range(length - len(self.required_symbols)))
        password = "".join(secrets.choice(password + "".join(self.required_symbols))
                        for _ in range(len(password + "".join(self.required_symbols))))
        return password

password_generator = Password(args.set)
for i in range(args.count):
    print(password_generator.generate_password(length=args.len))