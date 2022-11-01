# Initial variables
age = 20
sex = 0
bmi = 27.1
num_of_children = 1
smoker = 1

print('''Policyholder's Details:

Name: Yousra Ennaanai
D.O.B = 04/04/2002
Age = ''' + str(age) + '''
Sex = Female
BMI = ''' + str(bmi) + ''' 
Number of Children = ''' + str(num_of_children) + ''' 
Smoker? = Yes 
''' )

# Insurance estimate formula
insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
insurance_cost_pm = round((insurance_cost / 12) * 1.0675 , 2)
print('''
This person\'s insurance cost is ''' + str(insurance_cost) + ' dollars anually or ' + str(insurance_cost_pm, ) + ' dollars monthly (subject to 6.75% APR).')

# Age Factor
new_age = age + 4
new_insurance_cost = 250 * new_age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
change_in_insurance_cost_pm = round((change_in_insurance_cost / 12) * 1.0675 , 2)
print('''
The change in cost of insurance after ageing by 4 years is ''' + str(change_in_insurance_cost) + ' dollars anually or ' + str(change_in_insurance_cost_pm)+ ' dollars monthly (subject to 6.75% APR).')

# BMI Factor
bmi += 3.1
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
change_in_insurance_cost_pm = round((change_in_insurance_cost / 12) * 1.0675 , 2)
print('''
The change in cost of insurance after a BMI increase of 3.1 is ''' + str(change_in_insurance_cost) + ' dollars anually or ' + str(change_in_insurance_cost_pm)+ ' dollars monthly (subject to 6.75% APR).')

# Male vs. Female Factor
bmi -= 3.1
sex = 1
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
change_in_insurance_cost_pm = round((change_in_insurance_cost / 12) * 1.0675 , 2)
print('''
The change in cost of insurance for being female instead of male is ''' + str(change_in_insurance_cost) + ' dollars anually or ' + str(change_in_insurance_cost_pm)+ ' dollars monthly (subject to 6.75% APR).')


# Smoker
sex = 0
smoker = 0
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
change_in_insurance_cost_pm = round((change_in_insurance_cost / 12) * 1.0675 , 2)
print('''
The change in cost of insurance if the person was a non-smoker would be ''' + str(change_in_insurance_cost) + ' dollars anually or ' + str(change_in_insurance_cost_pm)+ ' dollars monthly (subject to 6.75% APR).')

# Offspring Factor
smoker = 1
num_of_children += 2
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
change_in_insurance_cost_pm = round((change_in_insurance_cost / 12) * 1.0675 , 2)
print('''
The change in cost of insurance if the person were to have another two children would be ''' + str(change_in_insurance_cost) + ' dollars anually or ' + str(change_in_insurance_cost_pm)+ ' dollars monthly (subject to 6.75% APR).')