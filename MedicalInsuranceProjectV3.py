import math as mt

# Medical Insurance Calculator V3.0:
print('''Welcome to the Medical Insurance Calculator V3.0 by Waleed H
''')
input("Press Enter to continue...")
print('''
Let\'s begin!
''')

# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = round(250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500, 2)
  monthly = round((estimated_cost / 12) * 1.0675 , 2)
  print('''
  ''' + name + ''', your estimated medical insurance cost is £''' + str(estimated_cost) + ' anually or £' + str(monthly) + '''  monthly 
    (subject to 6.75% APR)
  ''')
  return estimated_cost
 
# Estimate:
name = input('Before we go any further, what is your name?')
print('''
    Hi ''' + name + '''!
''')

age_prompt = input('Now ' + name + ', what is your age?')

if '.' in age_prompt: 
    age = mt.trunc(float(age_prompt))
else:
    age = int(age_prompt)

print('''
    Nice! You are ''' + str(age) + ''' years old!
''')

# /////////////Might want to add celebrities yo compare ages at some point lol//////////

gender = input('What gender were you assigned at birth?')

if gender.lower() == 'male' :
  sex = 1
elif gender.lower() == 'female':
  sex = 0
else:
  print('''
  Please answer male or female.
  ''')
  

print('''
''')

bmi_prompt = input('What is your BMI? (You can calculate this on the NHS website @ https://www.nhs.uk/live-well/healthy-weight/bmi-calculator/)')

if '.' not in bmi_prompt:
    bmi_value = int(bmi_prompt)
else: 
    bmi_value = float(bmi_prompt)

print('''
    Your BMI is ''' + str(bmi_value) + '''
''' )

smoke = input('Do you smoke?')

if smoke.lower() == 'yes' :
  smoker_status = 1
elif smoke.lower() == 'no':
  smoker_status = 0
else:
  print('''
  Please answer yes or no.
  ''')

if smoker_status == 1:
    print('''
    You are a smoker.
    ''')
else:
    print('''
    You are not a smoker.
    ''')

kids = input('Do you have children?')

if kids.lower() == 'yes' :
  num_kids = input('How many?')
  num_of_children = int(num_kids)
  print('''
  You have ''' + num_kids + ''' children
  ''')
elif kids.lower() == 'no':
    num_of_children = 0
    print('''
  Lucky you :)
  ''')
elif int(kids) >= 0 :
  num_of_children = int(kids) 
else: 
  print('''
  Please answer yes or no.
  ''')
  num_of_children = 0



print('''
Thank you for providing your details. I will now calculate your estimated insurance cost.
''')

print('''
Done!
''')

input('Press Enter to see your insurance estimate...')

estimate_insurance_cost(name, age, sex, bmi = bmi_value, num_of_children = num_of_children, smoker = smoker_status)


# Advice// Smoker Analysis:
def analyse_smoker(smoker_status):

  if smoker_status == 1:
    print('''   To lower your cost, you should consider quitting smoking.
    ''')
  else:
    print('''   Smoking is not an issue for you.
    ''')

analyse_smoker(smoker_status)

#Advice// BMI Analysis

def analyse_bmi(bmi_value):

  if bmi_value > 30:
    print('   Your BMI is in the obese range. To lower your cost, you should significantly lower your BMI.')
  elif bmi_value >= 25 and bmi_value <= 30:
    print('   Your BMI is in the overweight range. To lower your cost, you should lower your BMI.')
  elif bmi_value >= 18.5 and bmi_value < 25:
    print('   Your BMI is in a healthy range.')
  elif bmi_value < 18.5:
    print('   Your BMI is in the underweight range. Increasing your BMI will not help lower your cost, but it will help improve your health.')
  if bmi_value >= 25: 
    req_loss = round(bmi_value - 25, 1)
    print('''
    To bring your BMI into a healthy range, you must lower your BMI by ''' + str(req_loss) + '.')
  if bmi_value < 18.5: 
    req_gain = round(18.5 - bmi_value, 1)
    print('''
    To bring your BMI into a healthy range, you must increase your BMI by ''' + str(req_gain) + '.')


analyse_bmi(bmi_value)