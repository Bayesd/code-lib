def ConvertToList(stringInput):
    li = list(stringInput.split(" "))
    return li

def listToString(listInput):
    str1 = ""
    for i in listInput:
        str += i

def checkCode(code):

def combineCodeAndVars(code, variables, positions):
    saveToFile(combine(code, variables, positions))

def saveToFile(code):

# Initialization of local variables

user_code = input("Enter code: ")
code_list = ConvertToList(user_code)
variable_pos = []
variables = []
code_with_variables = ""
counter = 1

uniqueVarValues = input(f"How many unique variable values are there in\n\t{user_code}")

# Identify the variables for user code
for value in uniqueVarValues:
    for i in code_list: 
        part = f"{i}"
        print("[" + str(counter) + "] : " + part)
        counter += 1
    variable_pos = ConvertToList(input('Identify the values for var1?\n'
        'Enter the corresponding number, separate with space if there are multiple variable values:\n'))

for i in variable_pos:
    print(code_list[int(i)-1])

print(variable_pos)
for i in variable_pos:
    variables += code_list[int(i) - 1]

print(variables)
if uniqueVarValues < 1:
    print(f"Is this the complete code?\n\t{user_code}")
elif len(variables) > 1 and uniqueVarValues == 1:
    print(f"Is this the complete code\n\t{user_code}")
elif len(variables) <= 1 and uniqueVarValues > 1:
    oneVarValue = input("Does these variables share the same value? (y/n)")
    if oneVarValue == "y":
        print("Is this the correct code?\n")
else:
    saveToFile(user_code)
