import json
# class used for the POC Answering Module
class AnsweringModule: 

	#constructor, we need the path of the rules
	def __init__(self, rulesPathInit):
		
		#save it inside the object	
		self.rulesPath = rulesPathInit
		
		#try to open the file
		try:
			with open(self.rulesPath) as f:
				self.rules = json.loads(f.read()) # if success read json

				#print(self.rules)
		except IOError: #else give error
			print("Rules could not be loaded")
			self.rules = None

	#function used to retrieve the answer of a classified post		
	def answerPost(self, post, classification):
		
		#if the rules file is valid
		if self.rules is not None:
			#set empty answer
			answer = None

			#get the dictionary related to the classification
			current_dict = self.rules['classification'][classification]

			while answer is None:
				
				keyword_found = False
				#print("Looping, dictionary is:" + str(current_dict))
				for key in current_dict:
					if key != "_all" and key in post:
						#print("Using " + key + " as key")
						current_dict = current_dict[key]
						keyword_found = True
						break

				if not keyword_found:
					answer = current_dict["_all"]

			return answer



#am = AnsweringModule("exampleRules.json")
#answer = am.answerPost("fuck you nigger Yeah I did it now martyr me https://t.co/EXLSPeh4wM", 1)
#print("Answer: ", answer)