
medical_costs = dict()

medical_costs['Marina'] = 6607.0
medical_costs['Vinay'] = 3225.0
medical_costs.update({'Connie': 8886.0, 'Issac': 16444.0, 'Valentina': 6420.0})

medical_costs['Vinay'] = 3325.0

total_cost = 0

for record in medical_costs:
  total_cost += medical_costs[record]

print(total_cost)

average_cost = total_cost/len(medical_costs)

print('Average Insurance Cost: £' + str(average_cost))

names = ['Marina', 'Vinay', 'Connie', 'Issac', 'Valentina']
ages = [27, 24, 43, 35, 52]

zipped_ages = zip(names,ages)

names_to_ages = {key:value for key, value in zipped_ages}

print(names_to_ages)

marina_age = names_to_ages.get('Marina')

print('Marina\'s age is ' + str(marina_age) + ' years old.')

medical_records = dict()

medical_records['Marina'] = {"Age": 27, "Sex": "Female", "BMI": 31.1, "Children": 2, "Smoker": "Non-smoker", "Insurance Cost": 6607.0}

medical_records['Vinay'] = {"Age": 24, "Sex": "Male", "BMI": 26.6, "Children": 0, "Smoker": "Non-smoker", "Insurance_cost": 3325.0}

medical_records['Connie'] = {"Age": 43, "Sex": "Female", "BMI": 25.3, "Children": 3, "Smoker": "Non-smoker", "Insurance Cost": 8886.0}

medical_records['Issac'] = {"Age": 35, "Sex": "Male", "BMI": 20.6, "Children": 4, "Smoker": "Smoker", "Insurance Cost": 16444.0}

medical_records['Valentina'] = {"Age": 52, "Sex": "Female", "BMI": 18.7, "Children": 1, "Smoker": "Non-smoker", "Insurance Cost": 6420.0}

print(medical_records)

def name_get(name_req):
  for name in medical_records.keys():
    if name_req.lower() == name.lower():
      name_get = name
  return name_get

name = name_get('Connie')
cost_query = '{}\'s insurance cost is £{}'

def cost_print(name):
  print(cost_query.format(name, medical_records[name]['Insurance Cost']))

cost_print(name)

def delete_record(name):

  del medical_records[name.title()]

delete_record('vinay')

print(medical_records)

for name, record in medical_records.items():
    age = record['Age']
    sex = record['Sex']
    smoker = record['Smoker']
    bmi = record['BMI']
    cost = record['Insurance Cost']
    print(f"{name} is a {age} year old {sex} {smoker} with a BMI of {bmi} and insurance cost of £{cost}.")
