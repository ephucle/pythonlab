class Question:
	def __init__(self, prompt, answer):
		self.prompt = prompt
		self.answer = answer
class Test:
	def __init__(self):
		self.questions = []
	def add_question(self, question):
		self.questions.append(question)
	def run_quiz(self):
		print("Start to run QUIZ")
		score = 0
		for question in self.questions:
			answer = input(question.prompt+"\n >>> ")
		if answer == question.answer:
			score += 1
		print("You got", score, "out of", len(self.questions))
		return score
	def show_questions(self):
		for q in self.questions:
			print(q.prompt, "|", q.answer)

question_datas = [
	("What color are apples?\n(a) Red\n(b) Orange", "a"),
	("What color are bananas?\n(a) Red\n(b) Yellow", "b"),
	("Capital of Vietnam?\n(a) HoChiMinhcity\n(b) Hanoi", "b")
]

test = Test()

for data in question_datas:
	test.add_question(Question(*data))


#test.show_questions()
test.run_quiz()

