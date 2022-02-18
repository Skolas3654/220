"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem
that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""


def name_reverse():
    name = input("Enter a name(first last): ")
    reversed_name = name.split()
    last_name, first_name = reversed_name[1], reversed_name[0]
    print(last_name + ", " + first_name)

#name_reverse()

def company_name():
    com_name = input("Enter a company domain" )
    print(com_name[4:len(com_name)-4])

#company_name()

def initials():
    student_value = eval(input("How many students are in the class?"))  # odd note, adding \n to the end of the input completley marks it as an F when running the test program
    for i in range(student_value):
        student_name = input("What is the name of student " + str(i+1) + "? ")
        space_loc = student_name.find(" ")
        print(student_name[0] + student_name[space_loc + 1])

#initials()

def names():
    names = input("Enter a list of names: ")
    name_list = names.split()

    initials = ""
    initials_list = []

    for i in name_list:
        initials += i[0]

    for r in range(0, len(initials), 2):
        initials_list.append(initials[r:r + 2])
    intitials_list = " ".join(initials_list)

    print(intitials_list)

#names()



def thirds():
    sentence_count = eval(input("Enter the number of sentences: "))
    thirds_output = []
    for i in range(sentence_count):
        sentence = input("Enter sentence " + str(i+1) + ": ")

        for r in range(0,len(sentence), 3):
            thirds_output.append(str(sentence[r]))
        thirds_output.append("\n")
    thirds_output = "".join(thirds_output)
    print(thirds_output)

#thirds()

def word_average():
    sentence = input("Enter a sentence: ")
    space_count = sentence.count(" ")
    world_list = sentence.split()
    count = len(sentence) - space_count
    average = count/len(world_list)

    print(average)


#word_average()

def pig_latin():
    sentence = input("Enter a sentence to convert to pig latin: ")
    sentence = sentence.split()
    for i in range(0,len(sentence)):
        word = sentence[i]
        first_letter = word[0]
        pig_lat_res = word[1:] + first_letter + "ay"
        print(pig_lat_res.lower(), end=" ")

#pig_latin()



if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()
    pass
