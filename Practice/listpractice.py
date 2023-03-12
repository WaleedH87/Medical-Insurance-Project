names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Add your code here
names.append('Priscilla')
insurance_costs.append(8320.0)

print(names)
print(insurance_costs)

medical_records = list(zip(insurance_costs, names))

print(medical_records)

num_medical_records = len(medical_records)

print('There are ' + str(num_medical_records) + ' medical records.')

first_medical_record = medical_records[0]

print('Here is the first medical record: ' + str(first_medical_record))

medical_records.sort()

print('Here are the medical records sorted by insurance cost: ' + str(medical_records))

cheapest_three = medical_records[:3]

print('Here are the three cheapest insurance costs in our medical records: ' + str(cheapest_three))

priciest_three = medical_records[-3:]

print('Here are the three most expensive insurance costs in our medical records: ' + str(priciest_three))

occurrences_paul = names.count('Paul')

print('There are ' + str(occurrences_paul) + ' individuals with the name Paul in our medical records.')

medical_records_b = list(zip(names, insurance_costs))
medical_records_b.sort()

print('Here are the medical records sorted in alphabetical order: ' + str(medical_records_b))

middle_five_records = medical_records[3:8]

print(middle_five_records)

medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""

# Add your code here

updated_medical_data = medical_data.replace('#', '£')
#print(updated_medical_data)

num_records = 0

for i in updated_medical_data:
  if i == '£':
    num_records += 1

print('There are {num_records} medical records in the data.'.format(num_records=num_records))

medical_data_split = updated_medical_data.split(';')

medical_records = []

for record in medical_data_split:
  medical_records.append(record.split(','))

#print(medical_records)

medical_records_clean = []

for record in medical_records:
  record_clean = []
  for item in record:
    record_clean.append(item.strip())
  medical_records_clean.append(record_clean)

#print(medical_records_clean)

for record in medical_records_clean:
  #print(record[0].upper())

  names = []
  ages = []
  bmis = []
  insurance_costs = []

for record in medical_records_clean:
  names.append(record[0])
  ages.append(record[1])
  bmis.append(record[2])
  insurance_costs.append(record[3])

# print(names)
# print(ages)
# print(bmis)
# print(insurance_costs)

total_bmi = 0

for bmi in bmis:
  total_bmi += float(bmi)

average_bmi = round(float(total_bmi / len(bmis))
, 1)
print('Average BMI: {average_bmi}'.format(average_bmi=average_bmi,))

total_insurance_cost = 0

for cost in insurance_costs:
  costs = []
  costs.append(cost.replace('£', ''))
  for i in costs:

    total_insurance_cost += float(i)

average_cost = round(float(total_insurance_cost / len(insurance_costs)), 2)

print('Average Cost: £{average_cost}'.format(average_cost=average_cost))

full_names = []
first_names = []

for name in names:
  full_names.append(name.split())


for i in range(len(insurance_costs)):
  print('{name} is {age} years old with a BMI of {bmi} and an insurance_cost of {cost}.'.format(name=full_names[i][0], age=ages[i], bmi=bmis[i], cost=insurance_costs[i]))