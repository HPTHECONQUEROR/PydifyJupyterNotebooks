# 0th list is offl lang
# 1st list is other lang


states_lang = {
    "Andhra Pradhesh" : [["Telugu", "English"],["Urdu", "Hindi", "Banjara", "Tamil", "Kannada", "Marathi", "Oriya"]],
    "Karnataka" : [["Kannada", "English"],["Urdu", "Telugu", "Tamil", "Marathi"]],
    "Kerala" : [["Malayalam", "English"],["Hindi", "Kannada", "Tamil", "Tulu"]],
    "Tamilnadu" : [["Tamil","English"],["Telugu","Kannada", "Urdu", "Malayalam", "Hindi","Japanese"]],
    "Telangana" : [["Telugu", "Urdu"],["Hindi", "Tamil", "Kannada", "Marathi", "Oriya"]]
}




def max_num_lang():
    def count(state):
         return len(states_lang[state][0])+len(states_lang[state][1])
    max_lang = 0
    max_state = ""

    for i in states_lang:
        cur = count(i)
        if cur > max_lang:
            max_lang = cur
            max_state = i
    return f"The state that uses the maximum number of languages is {max_state}, it has over {max_lang} of languages"

'''
input -- state's name 
output -- show the number of other languages 
'''

def no_otherlang(state):
    return f"The number of spoken languages in {state}, excluding official languages is {len(states_lang[state][1])}"

'''
input -- language (string)  - Tamil
output -- list the states where the given language is an other language --? state_lang[state][1]  (List)
'''

def spoken_lang_per_state(language):
    states_with_lang = ""
    for i in states_lang:
        if language in states_lang[i][1]:
            states_with_lang+=f" {i}"
    return f"The language {language} is spoken in these states as non offl language in {states_with_lang}"

# print(spoken_lang_per_state("Malayalam"))


def unique_finder():
    unique_dict = {}

    for i in states_lang:
        for j in states_lang[i]:
            for x in j:
                if x not in unique_dict:
                    unique_dict[x] = 1
                else:
                    unique_dict[x] += 1
    unique_lang = []
    for i in unique_dict:
        if unique_dict[i] == 1:
            unique_lang.append(i)

    return unique_lang


option = 0

if option == 1:
    print(max_num_lang())
elif option == 2:
    state = input("Enter the state name: ")
    no_otherlang(state)
elif option == 3:
    language = input("Enter the language you wanna find in which state its spoken as an non official language: ")
    spoken_lang_per_state(language)
elif option == 4:
    for i in unique_finder():
        print(i)
else:
    print("Enter the appropriate Value the options available are 1 - 4, Thank you.")

print(unique_finder())

#command line args