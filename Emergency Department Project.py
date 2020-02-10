# Lab 09: Emergency department triage of acute cardiac ischemia
# Your name
# Your email

# prompts
welcome_msg = 'Welcome to the Emergency Department Decision Support System'
q1 = 'Q1: Is there ECG evidence of acute Myocardial Infarction (MI)? (Y/N) '
q2 = 'Q2: Is there ECG evidence of acute Ischemia? (Y/N) '
q3 = 'Q3: How many urgent factors are present? (0/1/2/3) '

### INSERT YOUR CODE BELOW THIS LINE ###
a = str(input(q1))
if a == "Y":
	print("Assesment: High Risk")
	print("Assignment: Coronary Care Unit")
elif a == "N":
	b = str(input(q2))
	if b == "Y" or b == "N":
		c = int(input(q3))
		if c >= 2 and c <= 3 and b == "Y":
			print("Assesment: High RisK")
			print("Assignment: Coronary Care Unit")
		elif c < 2 and c >= 0 and b == "Y":
			print("Assesment: Moderate Risk")
			print("Assignment: Inpatient Telemetry Unit")
		elif b == "N" and c >= 2 and c <= 3:
			print("Assesment: Moderate Risk")
			print("Assignment: Inpatient Telemetry Unit")
		elif b == "N" and c == 1:
			print("Assesment: Low Risk")
			print("Assignment: Inpatient Telemetry Unit")
		elif b == "N" and c == 0:
			print("Assesment: Very Low Risk")
			print("Assignment: Observation Unit")
		else:
			print("Invalid input. Please Start Over")	
	else:
		print("Invalid input. Please Start Over")

else:
	print("Invalid input. Please Start Over")				
