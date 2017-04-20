# Lab 06
# Machine Learning
# April 18, 2017
#  8:54:42

# Naive Bayes classifier implementation






def status(dataset):
    status={'senior':0, 'junior':0, 'employees':0}

    for data in dataset:
        if data[1] == 'senior':
            status['senior']+=1
        elif data[1] == 'junior':
            status['junior']+=1
        status['employees']+=1
    # print status
    return status


def laplace_smoothing(senior,junior):
    # Laplace smoothing
    alpha = len(senior) - 1

    for key in senior.keys():
        if key == 'senior':
            senior[key] += alpha
        else:
            senior[key] += 1

    for key in junior.keys():
        if key == 'junior':
            junior[key] += alpha
        else:
            junior[key] += 1


    return senior, junior


def department(dataset, prior):

    senior={'sales':0, 'systems':0, 'marketing':0, 'secretary':0, 'senior':prior['senior']}
    junior={'sales':0, 'systems':0, 'marketing':0, 'secretary':0, 'junior':prior['junior']}
    
    for x in dataset:
        if x[1] == 'senior': 
            if x[0] == 'sales':
                senior['sales']+=1
            elif x[0]=='systems':
                senior['systems']+=1
            elif x[0]=='marketing':
                senior['marketing']+=1
            elif x[0]=='secretary':
                senior['secretary']+=1
            
        elif x[1]=='junior':
            if x[0] == 'sales':
                junior['sales']+=1
            elif x[0]=='systems':
                junior['systems']+=1
            elif x[0]=='marketing':
                junior['marketing']+=1
            elif x[0]=='secretary':
                junior['secretary']+=1

    senior, junior = laplace_smoothing(senior, junior)

    return senior,junior


def age(dataset,prior):
  
    senior={'21 25':0, '26 30':0, '31 35':0,  '36 40':0, '41 45':0, '46 50':0, 'senior':prior['senior']}
    junior={'21 25':0, '26 30':0, '31 35':0,  '36 40':0, '41 45':0, '46 50':0, 'junior':prior['junior']}
    
    for x in dataset:
        if x[1] == 'senior': 
            if x[2] == '21 25':
                senior['21 25']+=1
            elif x[2]=='26 30':
                senior['26 30']+=1
            elif x[2]=='31 35':
                senior['31 35']+=1
            elif x[2]=='36 40':
                senior['36 40']+=1
            elif x[2]=='41 45':
                senior['41 45']+=1
            elif x[2]=='46 50':
                senior['46 50']+=1
            
        elif x[1]=='junior':
            if x[2] == '21 25':
                junior['21 25']+=1
            elif x[2]=='26 30':
                junior['26 30']+=1
            elif x[2]=='31 35':
                junior['31 35']+=1
            elif x[2]=='36 40':
                junior['36 40']+=1
            elif x[2]=='41 45':
                junior['41 45']+=1
            elif x[2]=='46 50':
                junior['46 50']+=1

    senior, junior = laplace_smoothing(senior, junior)
    
    return senior,junior


def salary(dataset,prior):

    senior={'26 30':0, '31 35':0,  '36 40':0, '41 45':0, '46 50':0, '66 70':0, 'senior':prior['senior']}
    junior={'26 30':0, '31 35':0,  '36 40':0, '41 45':0, '46 50':0, '66 70':0, 'junior':prior['junior']}
    
    for x in dataset:
        if x[1] == 'senior': 
            if x[3]=='26 30':
                senior['26 30']+=1
            elif x[3]=='31 35':
                senior['31 35']+=1
            elif x[3]=='36 40':
                senior['36 40']+=1
            elif x[3]=='41 45':
                senior['41 45']+=1
            elif x[3]=='46 50':
                senior['46 50']+=1
            elif x[3] == '66 70':
                senior['66 70']+=1
            
        elif x[1]=='junior':
            if x[3]=='26 30':
                junior['26 30']+=1
            elif x[3]=='31 35':
                junior['31 35']+=1
            elif x[3]=='36 40':
                junior['36 40']+=1
            elif x[3]=='41 45':
                junior['41 45']+=1
            elif x[3]=='46 50':
                junior['46 50']+=1
            elif x[3] == '66 70':
                junior['66 70']+=1

    senior, junior = laplace_smoothing(senior, junior)
    
    return senior,junior

#
# def main():
#
#     # dataset = training_data.training_data()
#     #
#     # # Prior probability
#     # prior = status(dataset)
#     # print prior
#     #
#     # # Conditional probability
#     # dept_senior,dept_junior = department(dataset, prior)
#     # print dept_senior,dept_junior
#     #
#     # age_senior, age_junior = age(dataset, prior)
#     # print age_senior,age_junior
#     #
#     # salary_senior, salary_junior = salary(dataset, prior)
#     # print salary_senior,salary_junior
#     #
#     # #Test data
#     # data=test_data()
#
#
#
# main()







