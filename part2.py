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
final_list=[]
temp_list=[]

#student version
def student_version():
    global Pass, defer, fail

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

#checking the progression outcome
def studentoutcome():
    global validation, progress, trailer, exclude, retriever

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
    global Pass, defer, fail
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

#staffoutcome
def staffoutcome():
    global validation, progress, trailer, retriever, exclude

    if Pass == 120:
        print("progress")
        temp_list = (f'Progress - {Pass},{defer},{fail}')
        progress += 1

    elif Pass == 100:
        print("progress(Module Trailer)")
        temp_list = (f'progress(Module Trailer) - {Pass},{defer},{fail}')
        trailer += 1

    elif fail >= 80:
        print("Exclude")
        temp_list = (f'Exclude - {Pass},{defer},{fail}')
        exclude += 1

    else:
        print("Module Retriever")
        temp_list = (f'Module Retriver - {Pass},{defer},{fail}')
        retriever += 1

    final_list.append(temp_list)
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

    for x in final_list:
        print(x)

def main_part():
    print('------------', 'Menu', '----------')
    choice_1 = input('Enter 1 for student version ; Enter 2 for staff version : ')

    if choice_1 == '1':
        student_version()

    elif choice_1 == '2':
        staff_version()

    else:
        print('Invalid Input')
        main_part()


main_part()




















