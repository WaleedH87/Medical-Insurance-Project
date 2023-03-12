medical_costs = {
    'Marina': 6607.0,
    'Vinay': 3325.0,
    'Connie': 8886.0,
    'Issac': 16444.0,
    'Valentina': 6420.0
}

total_cost = sum(medical_costs.values())
average_cost = total_cost / len(medical_costs)

print(f'Total Insurance Cost: £{total_cost:.2f}')
print(f'Average Insurance Cost: £{average_cost:.2f}')

names = ['Marina', 'Vinay', 'Connie', 'Issac', 'Valentina']
ages = [27, 24, 43, 35, 52]
names_to_ages = dict(zip(names, ages))

print(names_to_ages)

marina_age = names_to_ages.get('Marina')

print(f"Marina's age is {marina_age} years old.")

medical_records = {
    'Marina': {'Age': 27, 'Sex': 'Female', 'BMI': 31.1, 'Children': 2, 'Smoker': 'Non-smoker', 'Insurance Cost': 6607.0},
    'Vinay': {'Age': 24, 'Sex': 'Male', 'BMI': 26.6, 'Children': 0, 'Smoker': 'Non-smoker', 'Insurance Cost': 3325.0},
    'Connie': {'Age': 43, 'Sex': 'Female', 'BMI': 25.3, 'Children': 3, 'Smoker': 'Non-smoker', 'Insurance Cost': 8886.0},
    'Issac': {'Age': 35, 'Sex': 'Male', 'BMI': 20.6, 'Children': 4, 'Smoker': 'Smoker', 'Insurance Cost': 16444.0},
    'Valentina': {'Age': 52, 'Sex': 'Female', 'BMI': 18.7, 'Children': 1, 'Smoker': 'Non-smoker', 'Insurance Cost': 6420.0}
}

print(medical_records)

def get_name(name_req):
    for name in medical_records:
        if name_req.lower() == name.lower():
            return name

name = get_name('Connie')
cost_query = "{}'s insurance cost is £{}"

def print_cost(name):
    print(cost_query.format(name, medical_records[name]['Insurance Cost']))

print_cost(name)

def delete_record(name):
    del medical_records[name.title()]

delete_record('Vinay')
print(medical_records)

for name, record in medical_records.items():
    print(f"{name} is a {record['Age']} year old {record['Sex']} {record['Smoker']} with a BMI of {record['BMI']} and insurance cost of £{record['Insurance Cost']}.")


#Changes made:

#Improved formatting, spacing and indentation for better readability
#Changed medical_costs.update to a dictionary initialization for better readability
#Corrected the spelling of the variable total_cost when printing
#Simplified the calculation of the total_cost using the sum() function
#Simplified the calculation of the average_cost
#Simplified the creation of the dictionary names_to_ages using zip()
#Used f-strings for better readability in the print statements
#Changed name_get() to get_name(), and made it return the name immediately when found (no need to store in a variable)
#Changed cost_print() to `print_cost