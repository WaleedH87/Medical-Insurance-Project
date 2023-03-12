# Create calculate_insurance_cost() function below: 
def calculate_insurance_cost(age, sex, bmi, num_of_children, smoker, name):
  estimated_cost = round(250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500, 2)
  print('The estimated insurance cost for ' + name + ' is £' + str(estimated_cost))
  return estimated_cost
### Initial variables for Maria 
'''
age = 28
sex = 0  
bmi = 26.2
num_of_children = 3
smoker = 0  
'''

# Estimate Maria's insurance cost
maria_insurance_cost = calculate_insurance_cost(28, 0, 26.2, 3, 0, 'Maria')

# Initial variables for Omar
'''
age = 35
sex = 1 
bmi = 22.2
num_of_children = 0
smoker = 1  
'''

# Estimate Omar's insurance cost 
omar_insurance_cost = calculate_insurance_cost(35, 1, 22.2, 0, 1, 'Omar')

print(maria_insurance_cost)
print(omar_insurance_cost)

# My estimate

waleed_insurance_cost = calculate_insurance_cost(22, 1, 20.2, 0, 1, 'Waleed')

print(waleed_insurance_cost)

# Difference
def difference_in_cost(person1cost, person1name, person2cost, person2name):
  difference = round(person1cost - person2cost, 2)
  print('The difference in insurance cost for ' + person1name + ' and ' + person2name + ' is £' + str(difference)) 

difference_in_cost(waleed_insurance_cost, 'Waleed', maria_insurance_cost, 'Maria')