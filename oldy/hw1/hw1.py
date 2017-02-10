# tceh homework 1
# game python riddles


# get user name
name = input('Please enter your name: ')
print('Hello, {}'.format(name))

# questions and answers in dict
questions = {
				'What language are you learning? ': 'python',
				'Who invented it?, just a name ': 'guido',
				'Python was named after? ': 'monty python',
				'What was your first typped program? ': 'hello, world',
				'What is a keyword to make a function? ': 'def'
}

# counter how many right ansers
correct_answers = 0

for question in questions:
	answer = input(question)
	if answer.lower() == questions[question]:
		correct_answers += 1
		print('Awesome! You have guessed: ', correct_answers)
	else:
		print('Sorry man, you were wrong.')

print('Ok, you have answered on {}'.format(correct_answers))