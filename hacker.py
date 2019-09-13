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

def random_color(text):
	out = ''
	while random.randint(0,1):
		styles = ['bold','italic','underlined','blinkslow','blinkrapid','struckthrough']
		out += random.choice(styles)
		out += '_'
	out += random.choice(list(color.colorful.__dict__['_colorpalette'].keys()))
	if random.randint(0,1):
		out += '_on_'
		out += random.choice(list(color.colorful.__dict__['_colorpalette'].keys()))
	return getattr(color, out)(text)

def func0():
	print(random_color(uuid4().hex))

def func1():
	print(
		'\nName:', random_color(fake.name()),
		'\nEmail:', random_color(fake.email()),
		'\nJob:', random_color(fake.job()),
		'\nAdress:', random_color(fake.address()),
		'\nSSN:', random_color(fake.ssn()),
		'\nPhone Number:', random_color(fake.phone_number()),
	)

def func2():
	print(
		random_color(fake.ipv4()),
		random_color(fake.company()),
		random_color(fake.country())
	)

def func3():
	print(random_color('='*80))

def func4():
	words = ' '.join(fake.words(random.randint(3,10)))
	print(random_color(words))

def func5():
	print(random_color(fake.sha256()))

def func6():
	print(
		'\nUser Name:', random_color(fake.user_name()),
		'\nPassword:', random_color(fake.password()),
		'\nAgent:', random_color(fake.user_agent()) 
	)

def func7():
	count = 1
	while True:
		print('saning --', '!'*count)
		count +=1
		if random.randint(1,10) == 5 or count == 25: return 
		sleep(random.randint(0,3))


funcs = [func0, func1, func2, func3, func4, func5, func6, func7]

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
