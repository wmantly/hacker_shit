#!/usr/bin/env python3

import sys
import random
from uuid import uuid4
from time import sleep
from faker import Faker
import colorful as color

fake = Faker()

color.use_true_colors()
color.update_palette({'darkred': '#c11b55'})

def func0():
	print(color.plum(uuid4().hex))

def func1():
	print(
		'\nName:', color.green(fake.name()),
		'\nEmail:', color.yellow(fake.email()),
		'\nJob:', color.blue(fake.job()),
		'\nAdress:', color.green(fake.address()),
		'\nSSN:', color.red(fake.ssn()),
		'\nPhone Number:', color.brown(fake.phone_number())
	)

def func2():
	print(
		color.bold_red_on_green(fake.ipv4()),
		color.italic_black_on_white(fake.company()),
		color.black_on_white(fake.country())
	)

def func3():
	print(color.gold('='*80))

def func4():
	words = ' '.join(fake.words(random.randint(3,10)))
	print(color.black_on_red(words))

def func5():
	print(color.purple(fake.sha256()))

def func6():
	print(
		'\nUser Name:', color.italic_coral_on_beige(fake.user_name()),
		'\nPassword:', color.green_on_plum(fake.password()),
		'\nAgent:', color.darkred(fake.user_agent()) 
	)


funcs = [func0, func1, func2, func3, func4, func5, func6]

def main():
	last = None
	count = 0
	while True:
		count += 1
		if count % random.randint(50,500) == 0 or count > 500:
			print("\033c")
			count = 0
		choice = random.choice(funcs)
		if choice == last: continue
		last = choice
		choice()
		sleep(random.randint(1,9)/random.choice([10,100]))


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print('\nBye!')
		sys.exit(0)
