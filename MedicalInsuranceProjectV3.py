import math as mt
import numpy as np

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
confirm_name = False
name_prompt = input('Before we go any further, what is your full name?')

while confirm_name != True:
  if name_prompt == '' or name_prompt.startswith(' '):
    print('''
  Please provide your full name.
  ''')
    name_prompt = input('What is your full name?')
  else:
    confirm_name = True
    name = str(name_prompt)
    print('''
    Hi ''' + name + '''!
''')

age_prompt = input('Now ' + name + ', what is your age?')
confirm_age = False

while confirm_age != True:
  if age_prompt not in str(list(range(999))) or age_prompt == '' or ' ' in age_prompt:
    print('''
  Please provide your age as a whole number (E.g. If you are 19 and a half, please answer 19).
  ''')
    age_prompt = input('Now ' + name + ', what is your age?')
  elif int(age_prompt) > 100:
     print('''
  Sorry, we do not provide medical insurance for persons aged 101 or more. Please find a different insurance provider or provide an age below 101.
  ''')
     age_prompt = input('Now ' + name + ', what is your age?')
  else:
      age = int(age_prompt)
      confirm_age = True

# Celebrities

def same_age(age):
  celebrities = ['a new-born baby', 'Lilibet Diana Mountbatten-Windsor', 'Steel McBroom', 'Posie Rayne LaBrant', 'Stormi', 'Dream Kardashian', 'Saint West', 'Princess Charlotte', 'Royalty Brown', 'Prince George', 'Blue Ivy', 'Ryan\'s World', 'CR7 Jr.', 'Walker Scobell', 'Tiana Wilson', 'That Girl Lay Lay', 'Javon Walton', 'IShowSpeed', 'Millie Bobby Brown', 'Olivia Rodrigo', 'Billie Eilish', 'Lil TJay', 'Willow Smith', 'NBA YoungBoy', 'Shawn Mendes', 'Kylie Jenner', 'Tom Holland', 'Lil Baby', 'Justin Bieber', 'KSI', 'Selena Gomez', 'Travis Scott', 'Taylor Swift', 'Chris Brown', 'Rihanna', 'Lionel Messi', 'Drake', 'LeBron James', 'Future', 'Nicki Minaj', 'Lil Wayne', 'Beyonce', 'Kim Kardashian', 'Kevin Hart', 'James Corden', 'Kanye West', 'Ryan Renolds', '50 Cent', 'Lil Kim', 'Nas', 'Dwayne Johnson', 'Snoop Dogg', 'Jay-Z', 'J-Lo', 'Will Smith', 'Gordon Ramsay', 'Adam Sandler', 'Robert Downey Jr.', 'Brad Pitt', 'Michael Jordan', 'Jim Carrey', 'Barack Obama', 'Jeremy Clarkson', 'Simon Cowell', 'Ellen DeGeneres', 'Steve Harvey', 'Tom Hanks', 'Bill Gates', 'Jackie Chan', 'Hulk Hogan', 'Liam Neeson', 'Tommy Hilfiger', 'Dr. Phil', 'King Charles III', 'Mohamed Hadid', 'Elton John', 'Sylvester Stallone', 'Danny DeVito', 'Diana Ross', 'Robert De Niro', 'Harrison Ford', 'Martha Stewart', 'Tina Turner', 'Ralph Lauren', 'Jerry West', 'Morgan Freeman', 'King Salman', 'Maggie Smith', 'Giorgio Armani', 'Quincy Jones', 'Rita Moreno', 'James Earl Jones', 'Clint Eastwood', 'Gangsta Grandma', 'Bob Cousy', 'Pope Benedict XVI', 'David Attenborough', 'Bill Hayes', 'Jimmy Carter', 'Glynis Johns', 'Norman Lear' ]
  twin = celebrities[age]
  print('''
    Nice! You are the same age as ''' + str(twin) + '''!
''')

same_age(age=age)


gender = input('What gender were you assigned at birth?')
confirm_gender = False

while confirm_gender != True:
  if gender.lower() == 'female' or gender.lower() == 'male':
    confirm_gender = True
    if gender.lower() == 'male':
      sex = 1
    elif gender.lower() == 'female':
      sex = 0
  elif gender.lower() != 'male' and gender.lower != 'female' :
    print('''
  Please answer male or female.
  ''')
    gender = input('What gender were you assigned at birth?')
  
    
  

print('''
''')

# Ethnicity Factor

bmi_prompt = input('What is your BMI? (You can calculate this on the NHS website @ https://www.nhs.uk/live-well/healthy-weight/bmi-calculator/)')
confirm_bmi = False

while confirm_bmi != True:
  if str(bmi_prompt) not in str(np.linspace(0, 99, num=991)) or bmi_prompt == '' or ' ' in bmi_prompt:
    print('''
  Please provide a number less than 99.
  ''')
    bmi_prompt = input('What is your BMI? (You can calculate this on the NHS website @ https://www.nhs.uk/live-well/healthy-weight/bmi-calculator/)')
  elif float(bmi_prompt) >= 40:
     print('''
  Sorry, we do not provide medical insurance for persons with a BMI of 40 or more. Please find a different insurance provider, try again once you have lowered your BMI or provide a BMI below 40.
  ''')
     bmi_prompt = input('What is your BMI? (You can calculate this on the NHS website @ https://www.nhs.uk/live-well/healthy-weight/bmi-calculator/)')
  else:
      confirm_bmi = True
      bmi_value = bmi_prompt
      


print('''
    Your BMI is ''' + str(float(bmi_value)) + '''
''' )




smoke = input('Do you smoke?')
confirm_smoke = False

while confirm_smoke != True:
  if smoke.lower() == 'yes' :
    confirm_smoke = True
    smoker_status = 1
  elif smoke.lower() == 'no':
    confirm_smoke = True
    smoker_status = 0
  else:
    print('''
    Please answer yes or no.
    ''')
    smoke = input('Do you smoke?')

if smoker_status == 1:
    print('''
    You are a smoker.
    ''')
else:
    print('''
    You are not a smoker.
    ''')

kids = input('Do you have children?')
confirm_kids = False

while confirm_kids != True:
 
  if kids.lower() == 'no' or kids.lower() == 'yes':
    confirm_kids = True
  elif kids.lower() != 'no' or kids.lower() != 'yes':
    print('''
    Please answer yes or no.
    ''')
    kids = input('Do you have children?')
  
if kids.lower() == 'yes' :
  confirm_kids2 = False
else: 
  confirm_kids2 = True
  num_of_children = 0
  print('''
      No kids? Lucky you :)
      ''')
      
if confirm_kids2 == False:
   num_kids = input('How many?')

while confirm_kids2 != True:
    
  if num_kids not in str(list(range(999))) or num_kids == '' or ' ' in num_kids:
    print('''
  Please provide your number of children.
  ''')
    num_kids = input('How many?')
  
  else:
    confirm_kids2 = True
    num_of_children = int(num_kids)
    print('''
      You have ''' + num_kids + ''' children
      ''')

      



print('''
Thank you for providing your details. I will now calculate your estimated insurance cost.
''')

print('''
Done!
''')

input('Press Enter to see your insurance estimate...')

estimate_insurance_cost(name, age, sex, bmi = float(bmi_value), num_of_children = num_of_children, smoker = smoker_status)


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


analyse_bmi(float(bmi_value))