# Lab 06
# Machine Learning
# April 18, 2017
#  8:54:42

# Naive Bayes classifier implementation

from __future__ import division

import training_data
import naive_bayesian_classifier as classifier
import test_data


dataset = training_data.training_data()

# Prior probability
prior = classifier.status(dataset)
# print prior

# Conditional probability
dept_senior, dept_junior = classifier.department(dataset, prior)
# print dept_senior, dept_junior

age_senior, age_junior = classifier.age(dataset, prior)
# print age_senior, age_junior

salary_senior, salary_junior = classifier.salary(dataset, prior)
# print salary_senior, salary_junior

# Test data
data = test_data.test_data()

# test instance A
A = data[0]
# print A
# Status: Senior
department = A[0]
age = A[2]
salary = A[3]

# print department, age, salary

# print salary_senior[salary]
# print salary_senior['senior']
#
# print salary_senior[salary]/salary_senior['senior']
p_senior_A = (prior['senior']/prior['employees'])\
             *(dept_senior[department]/dept_senior['senior'])\
             *(age_senior[age]/age_senior['senior'])*(salary_senior[salary]/salary_senior['senior'])
print 'p(senior/A)= ',p_senior_A

p_junior_A = (prior['junior']/prior['employees'])\
             *(dept_junior[department]/dept_junior['junior'])\
             *(age_junior[age]/age_junior['junior'])*(salary_junior[salary]/salary_junior['junior'])

print 'p(junior/A)= ',p_junior_A

if p_senior_A > p_junior_A:
    print('According to Naive Bayesian Classifier status of ', A, ' is', 'senior')
else:
    print('According to Naive Bayesian Classifier status of ', A, ' is', 'junior')

print ' '
# test instance B
B = data[1]
# print B
# Status: Senior
department = B[0]
age = B[2]
salary = B[3]

# print department, age, salary

# print salary_senior[salary]
# print salary_senior['senior']
#
# print salary_senior[salary]/salary_senior['senior']
p_senior_B = (prior['senior']/prior['employees'])\
             *(dept_senior[department]/dept_senior['senior'])\
             *(age_senior[age]/age_senior['senior'])*(salary_senior[salary]/salary_senior['senior'])
print 'p(senior/B)= ', p_senior_B

p_junior_B = (prior['junior']/prior['employees'])\
             *(dept_junior[department]/dept_junior['junior'])\
             *(age_junior[age]/age_junior['junior'])*(salary_junior[salary]/salary_junior['junior'])

print 'p(junior/B)= ',p_junior_B

if p_senior_B > p_junior_B:
    print('According to Naive Bayesian Classifier status of ', B, ' is', 'senior')
else:
    print('According to Naive Bayesian Classifier status of ', B, ' is', 'junior')

