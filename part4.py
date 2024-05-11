#I declare that my work contains no examples of misconduct such as plagiarism or collusion.
#Any code taken from other sources is referenced within my code solution.(I have taken code from https://www.w3schools.com/python/default.asp)
#Himath Deepna Malwaththa
#20220663
#w1953306
#Date-14/12/2022

#initial values
list = [0, 20, 40, 60, 80, 100, 120]
progress = 0
trailer = 0
retriever = 0
exclude = 0
adding_dict = {}

#student version
def student_version():
 global Pass, defer, fail, studentID

 studentID =input('Enter studentID:')

 while True:
    try:
        Pass = int(input('Please enter your credits at pass '))
    except:
        print('Integer Required')
    else:
        if Pass not in list:
            print('out of range')
        else:
            break

 while True:
    try:
        defer = int(input('Please enter your credits at defer'))
    except:
        print('Integer Required')
    else:
        if defer not in list:
                print('out of range')
        else:
            break

 while True:
    try:
        fail = int(input('Please enter your credit at fail'))
    except:
        print('Integer required')
    else:
        if fail not in list:
            print('out of range')
        else:
            break

    total_credits = Pass + defer + fail

    if total_credits != 120:
        print('Total Incorrect')
        student_version()
    else:
        studentoutcome()

#student outcome
def studentoutcome():
    global validation ,progress, trailer, exclude, retriever, studentID, Pass, defer, fail

    if Pass == 120:
        print("progress")
        progress += 1

    elif Pass == 100:
        print("Progress(Module Trailer)")
        trailer += 1

    elif fail >= 80:
        print("Exclude")
        exclude += 1

    else:
        print("Module Retriever")
        retriever += 1

#staff version
def staff_version():
    global Pass, defer, fail, studentID
    studentID = input('Enter studentID:')

    while True:
        try:
            Pass = int(input('Enter your total PASS credits'))
        except:
            print('Integer Required')
        else:
            if Pass not in list:
                print('out of range')
            else:
                break

    while True:
        try:
            defer = int(input('Enter your total DEFER credits'))
        except:
            print('Integer Required')
        else:
            if defer not in list:
                print('out of range')
            else:
                break

    while True:
        try:
            fail = int(input('Enter your total Fail credits'))
        except:
            print('Integer Required')
        else:
            if fail not in list:
                print('out of range')
            else:
                break
    total_credits = Pass + defer + fail
    if total_credits != 120:
        print('Total Incorrect')
        staff_version()
    else:
        staffoutcome()

#staff outcome
def staffoutcome():
    global validation, progress, trailer, retriever, exclude, studentID

    if Pass == 120:
        print("progress")
        adding_dict[studentID] = f'progress - {Pass},{defer},{fail}'
        progress += 1

    elif Pass == 100:
        print("progress(Module Trailer)")
        adding_dict[studentID] = f'Progress (Module Trailer)- {Pass},{defer},{fail}'
        trailer += 1

    elif fail >= 80:
        print("Exclude")
        adding_dict[studentID] = f'Exclude - {Pass},{defer},{fail}'
        exclude += 1

    else:
        print("Module Retriever")
        adding_dict[studentID] = f'Module Retriever- {Pass},{defer},{fail}'
        retriever += 1

    user()

#asking whether the user wants to continue or quit
def user():
    global H

    H = input('Would you like to enter another set of data?\n'
              'Enter "y" for yes or "q" to quit and view results :').lower()

    if H == 'y':
        staff_version()

    elif H == 'q':
        horizontal_histogram()
    elif ValueError:
        print('Invalid Input')
        user()

#creating the horizontal histogram
def horizontal_histogram():
    print('---------------------------------')
    print('Horizontal Histogram')
    print('\nProgress', progress, ' : ', '*' * progress)
    print('\nTrailer', trailer, ' : ', '*' * trailer)
    print('\nRetriever', retriever, ' : ', '*' * retriever)
    print('\nExcluded', exclude, ' : ', '*' * exclude)

    total_outcome = progress + trailer + retriever + exclude
    print('\n', total_outcome, 'outcome in total.')
    print('---------------------------')

    for (element1,element2) in  adding_dict.items():
       print(element1, ':' , element2 , end='  ')


def main_part():
    print('------------', 'Menu', '----------')
    choice_1 = input('Enter 1 for student version ; Enter 2 for staff version : ')

    if choice_1 == '1':
        student_version()
        studentoutcome()

    elif choice_1 == '2':
        staff_version()

    else:
        print('Invalid Input')
        main_part()


main_part()


