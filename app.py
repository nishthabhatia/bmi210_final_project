from owlready2 import *



#Load the ontology and present the introduction.
def setup():
	#Load the existing ontology
	onto = get_ontology('ProjectOntology.owl')
	onto.load()
	convo_running = True
	#TO DO --> ADD COLOR! 
	header = """
	███████╗██╗████████╗███╗   ██╗███████╗███████╗███████╗
	██╔════╝██║╚══██╔══╝████╗  ██║██╔════╝██╔════╝██╔════╝
	█████╗  ██║   ██║   ██╔██╗ ██║█████╗  ███████╗███████╗
	██╔══╝  ██║   ██║   ██║╚██╗██║██╔══╝  ╚════██║╚════██║
	██║     ██║   ██║   ██║ ╚████║███████╗███████║███████║
	╚═╝     ╚═╝   ╚═╝   ╚═╝  ╚═══╝╚══════╝╚══════╝╚══════╝
	                                                      
	 █████╗ ██████╗ ██╗   ██╗██╗███████╗ ██████╗ ██████╗  
	██╔══██╗██╔══██╗██║   ██║██║██╔════╝██╔═══██╗██╔══██╗ 
	███████║██║  ██║██║   ██║██║███████╗██║   ██║██████╔╝ 
	██╔══██║██║  ██║╚██╗ ██╔╝██║╚════██║██║   ██║██╔══██╗ 
	██║  ██║██████╔╝ ╚████╔╝ ██║███████║╚██████╔╝██║  ██║ 
	╚═╝  ╚═╝╚═════╝   ╚═══╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝ 

	"""

	print(header)
	print ("Welcome! We are so excited to have you here. Today, we will discuss your goals and health, and use them to determine a set of physical fitness activities that may be good for you.\n")
	start_convo(onto)





#return the individual, based on user input
def returnGoalFromNumber(number):
	number = int(number)
	if (number == 1):
		return "toLoseWeight"
	elif (number == 2):
		return "toStrengthenMuscles"
	elif (number == 3):
		return "toImproveCardiopulmonaryFuntion"
	else:
		#TO DO error correction
		return ""


#return a list of health data information, based on user input
def returnHealthDataFromNums(nums):
	health_data = []
	for num in nums:
		num = int(num)
		if (num == 1):
			health_data.append("heartDisease")
		elif (num == 2):
			health_data.append("asthma")
		elif (nume == 3):
			health_data.append("backPain")
	return health_data



# def iterateThroughProperties(individual):
# 	for prop in individual.get_properties():
# 		for value in prop[individual]:
# 			print (".%s == %s" % (prop.python_name, value))

# def printInstancesOfClass(class_name):
# 	print ('Instances of ' + class_name +':')
# 	for i in ontology.class_name.instances(): 
# 		print(i)



#find the exercises a user should not do, based on their health data
def findNonRecommendedExercises(ontology, health_data):
	nonRecExercises = []
	exercisesOfInterest = ontology.search(hasHarmfulHealthData="*")
	for ex in exercisesOfInterest:
		if len(set(ex.hasHarmfulHealthData).intersection(set(health_data))) > 0:
			nonRecExercises.append(ex.name)
	#print(nonRecExercises)
	return nonRecExercises

def findRecommendedExercises(ontology, goal, nr_ex):
	recExercises = []
	exercisesOfInterest = ontology.search(hasEffectOfExercise="*")
	for ex in exercisesOfInterest:
		# print('STUFF')
		# print(ex.hasEffectOfExercise[0])
		# print(goal[0])
		sameIndividuals = ex.hasEffectOfExercise[0].equivalent_to
		if sameIndividuals[0] == goal[0]:
			if ex.name not in nr_ex:
				recExercises.append(ex.name)
	#print(recExercises)
	return recExercises

def start_convo(ontology):	
	convo_running = True
	
	while (convo_running):

		#1. Create a new Person instance
		name = input("First things, first. What is your name? \n")
		new_person = ontology.Person(name)
		print ("\n")
		
		#2. Determine the Goal instance that applies to them --> 
			#you can create a new goal. 
			#and then it must be set equivalent to an existing effect of exercise.
		goal_num = input("Awesome! Hi " + name + """! Which of the following goals do you align with most?
1: Lose Weight
2: Strengthen Muscles
3: Improve Cardiopulmonary Function \n
Please type the number corresponding to your selected goal: \n""")
		print("\n")
		goal = returnGoalFromNumber(goal_num)

		#3. Use hasGoal property to link Person to Goal
		new_person.hasGoal = [ontology.Goal(goal)]
		# print('HAS GOAL')
		# print(new_person.hasGoal)

		#4. Ask for health data. This is important for linking to exercise health data.
		health_data_nums = input("""Great! Just a few more questions. Do any of the following health conditions apply to you?
1: Heart Disease
2: Asthma
3: Back Pain \n
Please type a list of numbers corresponding to conditions that apply to you, separated by a single space. If none apply, please type 0: \n""")
		health_data_nums = health_data_nums.split()
		health_data_list = returnHealthDataFromNums(health_data_nums)
		
		i = 0
		hasHealthDataArr = []

		for i in range(len(health_data_list)):
			# print (i)
			health_data = health_data_list[i]
			hasHealthDataArr.append(ontology.HealthData(health_data))

		new_person.hasHealthData = hasHealthDataArr

		nr_exercises = findNonRecommendedExercises(ontology, hasHealthDataArr)
		r_exercises = findRecommendedExercises(ontology, new_person.hasGoal, nr_exercises)

		print ('\n')

		print ("Thank you! These are the exercises that we recommend for you: \n")
		for ex in r_exercises:
			print (ex)
		print ("...and these are the exercises that we don't recommend for you: ")
		for ex in nr_exercises:
			ex = ''.join(' ' + char if char.isupper() else char.strip() for char in ex).strip()
			print (ex.lower())
		
		print('\n')
		print('Thanks for using the Fitness Advisor! Good luck with your health journey. \n')


		convo_running = False



setup()