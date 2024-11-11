print('Welecome To My Computer Quiz!')

playing=input('Do You Want To play The Game Or not? ')

count=0

if playing.lower() !="yes":
    quit()

print("Okay! let's play : ")

answer=input('What is CPU Stand for? ')
if answer.lower() == "central processing unit":
    print('Answer is correct!')
    count=count+1
else:
    print('Answer is not correct')

answer=input('What is RAM Stand for? ')
if answer.lower() == "random access memory":
    print('Answer is correct!')
    count=count+1
else:
    print('Answer is not correct')
    
answer = input("What is the output of 10 % 3? A) 3 B) 0 C) 1 D) 2. Type the letter of the correct answer: ")
if answer.lower() == "c":
    print("Correct!")
    count += 1
else:
    print("Incorrect. The correct answer is C) 1.")


answer = input("What is the output of 5 ** 3? A) 15 B) 125 C) 8 D) 25. Type the letter of the correct answer: ")
if answer.lower() == "b":
    print("Correct!")
    count += 1
else:
    print("Incorrect. The correct answer is B) 125.")

answer = input("If x = 10 and we write x += 3, what is the new value of x? A) 13 B) 10 C) 7 D) 3. Type the letter of the correct answer: ")
if answer.lower() == "a":
    print("Correct!")
    count += 1
else:
    print("Incorrect. The correct answer is A) 13.")


answer = input("What is the output of 5 == 5? A) True B) False. Type the letter of the correct answer: ")
if answer.lower() == "a":
    print("Correct!")
    count += 1
else:
    print("Incorrect. The correct answer is A) True.")


answer = input("What is the output of 10 != 10? A) True B) False. Type the letter of the correct answer: ")
if answer.lower() == "b":
    print("Correct!")
    count += 1
else:
    print("Incorrect. The correct answer is B) False.")


answer = input("What is the output of True and False? A) True B) False. Type the letter of the correct answer: ")
if answer.lower() == "b":
    print("Correct!")
    count += 1
else:
    print("Incorrect. The correct answer is B) False.")


answer = input("What is the output of not (10 > 5)? A) True B) False. Type the letter of the correct answer: ")
if answer.lower() == "b":
    print("Correct!")
    count += 1
else:
    print("Incorrect. The correct answer is B) False.")


answer = input("What is the output of 5 & 3? A) 1 B) 2 C) 5 D) 3. Type the letter of the correct answer: ")
if answer.lower() == "a":
    print("Correct!")
    count += 1
else:
    print("Incorrect. The correct answer is A) 1.")

answer = input("What is the output of 5 | 3? A) 1 B) 2 C) 7 D) 3. Type the letter of the correct answer: ")
if answer.lower() == "c":
    print("Correct!")
    count += 1
else:
    print("Incorrect. The correct answer is C) 7.")


answer = input("What is the output of 10 / 2? A) 2 B) 5.0 C) 5 D) 10. Type the letter of the correct answer: ")
if answer.lower() == "b":
    print("Correct!")
    count += 1
else:
    print("Incorrect. The correct answer is B) 5.0.")


answer = input("What is the output of 10 // 3? A) 3.33 B) 3 C) 2 D) 1. Type the letter of the correct answer: ")
if answer.lower() == "b":
    print("Correct!")
    count += 1
else:
    print("Incorrect. The correct answer is B) 3.")


answer = input("What does 'is' check for in Python? A) Equality B) Identity C) Boolean D) None of these. Type the letter of the correct answer: ")
if answer.lower() == "b":
    print("Correct!")
    count += 1
else:
    print("Incorrect. The correct answer is B) Identity.")


answer = input("What will be the output of 'a' in 'apple'? A) True B) False. Type the letter of the correct answer: ")
if answer.lower() == "a":
    print("Correct!")
    count += 1
else:
    print("Incorrect. The correct answer is A) True.")


answer = input("What is the output of (5 > 3) or (3 > 5)? A) True B) False. Type the letter of the correct answer: ")
if answer.lower() == "a":
    print("Correct!")
    count += 1
else:
    print("Incorrect. The correct answer is A) True.")


answer = input("What is the output of 4 << 1? A) 2 B) 4 C) 8 D) 6. Type the letter of the correct answer: ")
if answer.lower() == "c":
    print("Correct!")
    count += 1
else:
    print("Incorrect. The correct answer is C) 8.")


answer = input("What is the output of 8 >> 2? A) 1 B) 2 C) 4 D) 16. Type the letter of the correct answer: ")
if answer.lower() == "c":
    print("Correct!")
    count += 1
else:
    print("Incorrect. The correct answer is C) 4.")

answer = input("What is the output of 5 + 3 * 2? A) 11 B) 16 C) 13 D) 10. Type the letter of the correct answer: ")
if answer.lower() == "a":
    print("Correct!")
    count += 1
else:
    print("Incorrect. The correct answer is A) 11.")


answer = input("What is the output of (5 + 3) * 2? A) 11 B) 16 C) 13 D) 10. Type the letter of the correct answer: ")
if answer.lower() == "b":
    print("Correct!")
    count += 1
else:
    print("Incorrect. The correct answer is B) 16.")


answer = input("What is the output of 10 > 9? A) True B) False. Type the letter of the correct answer: ")
if answer.lower() == "a":
    print("Correct!")
    count += 1
else:
    print("Incorrect. The correct answer is A) True.")


answer = input("If x = 5 and y = 5, what does x is not y return? A) True B) False. Type the letter of the correct answer: ")
if answer.lower() == "b":
    print("Correct!")
    count += 1
else:
    print("Incorrect. The correct answer is B) False.")

answer = input("In Python, which symbol is used to assign a value to a variable? ")
if answer == "=":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is '='.")


answer = input("What type of variable is used to store true/false values? A) String B) Integer C) Boolean D) Float. Type the letter of the correct answer: ")
if answer.lower() == "c":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is C) Boolean.")


answer = input("Which loop in Python is used when you know the exact number of iterations? A) while B) for C) both D) None. Type the letter of the correct answer: ")
if answer.lower() == "b":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is B) for.")


answer = input("What type of loop would you use if you want to run until a condition is met? A) for B) while C) both D) None. Type the letter of the correct answer: ")
if answer.lower() == "b":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is B) while.")


answer = input("Is '1variable' a valid variable name in Python? A) Yes B) No. Type the letter of the correct answer: ")
if answer.lower() == "b":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is B) No.")


answer = input("What will be the output of: for i in range(3): print(i)? A) 1,2,3 B) 0,1,2 C) 1,2,3,4 D) 0,1,2,3. Type the letter of the correct answer: ")
if answer.lower() == "b":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is B) 0,1,2.")


answer = input("What will be the output of this code? x = 1; while x < 4: print(x); x += 1. A) 1 2 3 B) 1 2 3 4 C) Infinite loop D) 1 2. Type the letter of the correct answer: ")
if answer.lower() == "a":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is A) 1 2 3.")


answer = input("Where is a variable defined inside a function accessible? A) Anywhere B) Only inside the function C) Only outside the function D) None. Type the letter of the correct answer: ")
if answer.lower() == "b":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is B) Only inside the function.")


answer = input("What does the 'continue' statement do in a loop? A) Stops the loop B) Skips the current iteration C) Exits the program D) None. Type the letter of the correct answer: ")
if answer.lower() == "b":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is B) Skips the current iteration.")


answer = input("What does the 'break' statement do in a loop? A) Stops the loop B) Skips the current iteration C) Continues the loop D) None. Type the letter of the correct answer: ")
if answer.lower() == "a":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is A) Stops the loop.")

answer = input('What method can be used to convert a string to all uppercase letters in Python? ')
if answer.lower() == "upper" or answer.lower() == "str.upper":
    print('Answer is correct!')
    count += 1
else:
    print('Answer is not correct. The correct answer is upper() or str.upper.')


answer = input('What method adds an item to the end of a Python list? ')
if answer.lower() == "append" or answer.lower() == "list.append":
    print('Answer is correct!')
    count += 1
else:
    print('Answer is not correct. The correct answer is append() or list.append.')


answer = input("What method would you use to retrieve all keys in a dictionary? ")
if answer.lower() == "keys" or answer.lower() == "dict.keys":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is keys() or dict.keys.")


answer = input("What is recursion in Python? A) Loop B) Function calling itself C) Function returning None D) Variable declaration. Type the letter of the correct answer: ")
if answer.lower() == "b":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is B) Function calling itself.")


answer = input("What keyword is used to define a function in Python? ")
if answer.lower() == "def":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is def.")


answer = input("What will be the output of print(type([]))? A) list B) [] C) <class 'list'> D) List type. Type the letter of the correct answer: ")
if answer.lower() == "c":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is C) <class 'list'>.")


answer = input("What is the data type of 5 in Python? A) float B) int C) str D) bool. Type the letter of the correct answer: ")
if answer.lower() == "b":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is B) int.")


answer = input("What will be the output of 'Python'.lower()? A) PYTHON B) python C) Python D) None. Type the letter of the correct answer: ")
if answer.lower() == "b":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is B) python.")


answer = input("What will be the output of [1, 2, 3, 4][1:3]? A) [1, 2] B) [2, 3] C) [3, 4] D) [2, 3, 4]. Type the letter of the correct answer: ")
if answer.lower() == "b":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is B) [2, 3].")


answer = input("What will be the output of bool([])? A) True B) False C) None D) []. Type the letter of the correct answer: ")
if answer.lower() == "b":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is B) False.")

answer = input("Which method converts a string to uppercase? ")
if answer.lower() == "upper" or answer.lower() == "str.upper":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is upper() or str.upper.")


answer = input("Which method converts a string to lowercase? ")
if answer.lower() == "lower" or answer.lower() == "str.lower":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is lower() or str.lower.")


answer = input("What does the 'find' method return when the substring is not found? A) -1 B) 0 C) None D) False. Type the letter of the correct answer: ")
if answer.lower() == "a":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is A) -1.")


answer = input("Which method is used to split a string into a list? ")
if answer.lower() == "split" or answer.lower() == "str.split":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is split() or str.split.")


answer = input("What method combines a list of strings into a single string? ")
if answer.lower() == "join" or answer.lower() == "str.join":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is join() or str.join.")


answer = input("What does the 'replace' method do in Python strings? A) Replace a character B) Change case C) Remove spaces D) Sort string. Type the letter of the correct answer: ")
if answer.lower() == "a":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is A) Replace a character.")


answer = input("Which method adds an element to the end of a list? ")
if answer.lower() == "append" or answer.lower() == "list.append":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is append() or list.append.")


answer = input("What does the 'extend' method do in Python lists? A) Add an element B) Add multiple elements C) Remove element D) Sort list. Type the letter of the correct answer: ")
if answer.lower() == "b":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is B) Add multiple elements.")

answer = input("What does the 'pop' method return if no argument is passed? A) Removes the last item B) Removes the first item C) None D) Returns True. Type the letter of the correct answer: ")
if answer.lower() == "a":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is A) Removes the last item.")


answer = input("What method sorts a list in ascending order by default? ")
if answer.lower() == "sort" or answer.lower() == "list.sort":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is sort() or list.sort.")


answer = input("What does 'keys()' return in a dictionary? A) List of keys B) List of values C) List of items D) None. Type the letter of the correct answer: ")
if answer.lower() == "a":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is A) List of keys.")


answer = input("Which method returns all values in a dictionary? ")
if answer.lower() == "values" or answer.lower() == "dict.values":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is values() or dict.values.")


answer = input("What method gives a list of key-value pairs in a dictionary? ")
if answer.lower() == "items" or answer.lower() == "dict.items":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is items() or dict.items.")


answer = input("What does 'get()' return if the key is not found? A) Error B) None C) False D) Empty list. Type the letter of the correct answer: ")
if answer.lower() == "b":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is B) None.")


answer = input("What does 'isdigit()' check for in a string? A) Digits only B) Letters only C) Lowercase D) Special characters. Type the letter of the correct answer: ")
if answer.lower() == "a":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is A) Digits only.")


answer = input("What does 'count' method do in a list? ")
if answer.lower() == "counts occurrences" or answer.lower() == "list.count":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is count() or counts occurrences.")


answer = input("True or False: Tuples are mutable data types. ")
if answer.lower() == "false":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is False.")


answer = input("Which method adds an element to a set? ")
if answer.lower() == "add" or answer.lower() == "set.add":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is add() or set.add.")

answer = input("What does 'remove()' do in a set? A) Adds an element B) Deletes an element C) Sorts elements D) Merges sets. Type the letter of the correct answer: ")
if answer.lower() == "b":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is B) Deletes an element.")


answer = input("What does 'reverse()' do in a list? A) Returns reversed list B) Reverses list in place C) Sorts list D) Removes elements. Type the letter of the correct answer: ")
if answer.lower() == "b":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is B) Reverses list in place.")

answer = input("Which type of variable is defined inside a function? A) Global B) Local C) Both A and B D) None. Type the letter of the correct answer: ")
if answer.lower() == "b":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is B) Local.")


answer = input("Which type of variable is defined outside all functions? A) Global B) Local C) Both A and B D) None. Type the letter of the correct answer: ")
if answer.lower() == "a":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is A) Global.")


answer = input("Can a local variable access a global variable? Yes or No: ")
if answer.lower() == "yes":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. Local variables can access global variables but not the other way around.")


answer = input("Which keyword is used to modify a global variable inside a function? A) global B) nonlocal C) local D) None. Type the letter of the correct answer: ")
if answer.lower() == "a":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is A) global.")


answer = input("Can a local variable override a global variable with the same name? Yes or No: ")
if answer.lower() == "yes":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. A local variable can override a global variable.")

answer = input("Which type of argument is passed based on the position of the parameter? A) Keyword Argument B) Positional Argument C) Default Argument D) Arbitrary Argument. Type the letter of the correct answer: ")
if answer.lower() == "b":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is B) Positional Argument.")


answer = input("Which type of argument is passed based on the name of the parameter? A) Positional Argument B) Keyword Argument C) Default Argument D) Arbitrary Argument. Type the letter of the correct answer: ")
if answer.lower() == "b":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is B) Keyword Argument.")


answer = input("Which type of argument has a default value when no argument is provided? A) Positional Argument B) Keyword Argument C) Default Argument D) Arbitrary Argument. Type the letter of the correct answer: ")
if answer.lower() == "c":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is C) Default Argument.")


answer = input("Which type of argument allows passing a variable number of arguments? A) Positional Argument B) Keyword Argument C) Default Argument D) Arbitrary Argument. Type the letter of the correct answer: ")
if answer.lower() == "d":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is D) Arbitrary Argument.")

answer = input("Can you mix positional and keyword arguments? Yes or No: ")
if answer.lower() == "yes":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. You can mix positional and keyword arguments, but positional arguments must come first.")


answer = input("What does the 'map' function do in Python? A) Applies a function to each item of an iterable B) Filters out items based on condition C) Sorts an iterable D) None of the above. Type the letter of the correct answer: ")
if answer.lower() == "a":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is A) Applies a function to each item of an iterable.")


answer = input("What is a lambda function in Python? A) A function with a name B) A function without a name C) A function with multiple arguments D) None of the above. Type the letter of the correct answer: ")
if answer.lower() == "b":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is B) A function without a name.")


answer = input("What does the 'filter' function do in Python? A) Filters out None values B) Filters elements based on a condition C) Converts a list to a string D) None of the above. Type the letter of the correct answer: ")
if answer.lower() == "b":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is B) Filters elements based on a condition.")


answer = input("Which combination is used to apply a function to each item of an iterable? A) lambda + filter B) map + lambda C) lambda + list D) map + set. Type the letter of the correct answer: ")
if answer.lower() == "b":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is B) map + lambda.")

answer = input("Which combination is used to filter elements of an iterable based on a condition? A) filter + lambda B) map + lambda C) lambda + sum D) filter + reduce. Type the letter of the correct answer: ")
if answer.lower() == "a":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is A) filter + lambda.")


answer = input("How many arguments can a lambda function have in Python? A) One B) Two C) Any number D) None. Type the letter of the correct answer: ")
if answer.lower() == "c":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is C) Any number.")

answer = input("What will be the output of 'map(lambda x: x * 2, [1, 2, 3])'? A) [2, 4, 6] B) [1, 2, 3] C) [2, 2, 2] D) [1, 4, 9]. Type the letter of the correct answer: ")
if answer.lower() == "a":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is A) [2, 4, 6].")

answer = input("What will be the output of 'filter(lambda x: x > 2, [1, 2, 3])'? A) [1, 2] B) [3] C) [1, 3] D) [2, 3]. Type the letter of the correct answer: ")
if answer.lower() == "b":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is B) [3].")

answer = input("How do you write a lambda function with two arguments to add them together? A) lambda x, y: x + y B) lambda: x + y C) lambda (x, y): x + y D) lambda x y: x + y. Type the letter of the correct answer: ")
if answer.lower() == "a":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is A) lambda x, y: x + y.")


answer = input("Can a lambda function have multiple conditions? Yes or No: ")
if answer.lower() == "yes":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. Lambda functions can have multiple conditions.")

answer = input("What will be the output of 'filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])'? A) [2, 4] B) [1, 3, 5] C) [2, 3, 4, 5] D) [1, 2, 3]. Type the letter of the correct answer: ")
if answer.lower() == "a":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is A) [2, 4].")

answer = input("What will be the output of 'map(lambda x: x + 1, [1, 2, 3])'? A) [1, 2, 3] B) [2, 3, 4] C) [0, 1, 2] D) [1, 1, 1]. Type the letter of the correct answer: ")
if answer.lower() == "b":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is B) [2, 3, 4].")


answer = input("What happens when you use 'map(lambda x, y: x + y, [1, 2], [3, 4])'? A) [4, 6] B) [3, 5] C) [1, 2] D) Error. Type the letter of the correct answer: ")
if answer.lower() == "a":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is A) [4, 6].")


answer = input("Can 'filter()' function be used with multiple conditions in a single lambda function? Yes or No: ")
if answer.lower() == "yes":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. You can use 'filter' with multiple conditions in a single lambda.")

answer = input("What will be the result of the lambda expression: 'lambda x: x if x % 2 == 0 else x * 2'? A) Return even numbers unchanged, double odd numbers B) Double all numbers C) Return only odd numbers D) None of the above. Type the letter of the correct answer: ")
if answer.lower() == "a":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is A) Return even numbers unchanged, double odd numbers.")


answer = input("Can lambda functions be passed as arguments to other functions? Yes or No: ")
if answer.lower() == "yes":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. Lambda functions can be passed as arguments to other functions.")


answer = input("What will be the output of 'sorted([('apple', 3), ('banana', 2), ('cherry', 1)], key=lambda x: x[1])'? A) [('apple', 3), ('banana', 2), ('cherry', 1)] B) [('cherry', 1), ('banana', 2), ('apple', 3)] C) [('banana', 2), ('cherry', 1), ('apple', 3)] D) Error. Type the letter of the correct answer: ")
if answer.lower() == "b":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is B) [('cherry', 1), ('banana', 2), ('apple', 3)].")


answer = input("What does the expression 'list(map(lambda x: x * 2, [1, 2, 3]))' return? A) [1, 2, 3] B) [2, 4, 6] C) [0, 1, 2] D) [1, 1, 1]. Type the letter of the correct answer: ")
if answer.lower() == "b":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is B) [2, 4, 6].")

answer = input("What will be the output of 'list(filter(lambda x: x.startswith('a'), ['apple', 'banana', 'avocado']))'? A) ['apple', 'avocado'] B) ['banana', 'avocado'] C) ['apple', 'banana'] D) ['avocado']. Type the letter of the correct answer: ")
if answer.lower() == "a":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is A) ['apple', 'avocado'].")


answer = input("What will be the output of 'list(map(lambda x: (x[0], x[1] * 2), [(1, 2), (3, 4), (5, 6)]))'? A) [(1, 4), (3, 8), (5, 12)] B) [(1, 2), (3, 4), (5, 6)] C) [(2, 4), (6, 8), (10, 12)] D) None of the above. Type the letter of the correct answer: ")
if answer.lower() == "a":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is A) [(1, 4), (3, 8), (5, 12)].")


answer = input("Which of the following is a keyword argument? A) def add(x, y): return x + y B) def add(x=2, y=3): return x + y C) def add(*args): return sum(args). Type the letter of the correct answer: ")
if answer.lower() == "b":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is B) def add(x=2, y=3): return x + y.")

answer = input("What does *args in a function parameter mean? A) It means you can pass any number of arguments B) It refers to one argument C) It can be used only for keyword arguments D) None of the above. Type the letter of the correct answer: ")
if answer.lower() == "a":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. *args allows passing any number of positional arguments.")

answer = input("What will the lambda expression 'lambda x: 'Even' if x % 2 == 0 else 'Odd'' return for x = 5? A) 'Odd' B) 'Even' C) 'True' D) 'False'. Type the letter of the correct answer: ")
if answer.lower() == "a":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is A) 'Odd'.")


answer = input("What will be the output of 'list(filter(None, [0, 1, '', 'hello', False, True]))'? A) [1, 'hello', True] B) [0, False] C) ['', False] D) None. Type the letter of the correct answer: ")
if answer.lower() == "a":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is A) [1, 'hello', True].")

answer = input("What will 'lambda x: 'Even' if x % 2 == 0 else 'Odd' if x % 2 != 0 else 'Neither'' return for x = 0? A) 'Even' B) 'Odd' C) 'Neither' D) None of the above. Type the letter of the correct answer: ")
if answer.lower() == "a":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is A) 'Even'.")

answer = input("What will be the result of 'sorted(['apple', 'banana', 'pear'], key=lambda x: len(x))'? A) ['pear', 'apple', 'banana'] B) ['banana', 'pear', 'apple'] C) ['apple', 'banana', 'pear'] D) None of the above. Type the letter of the correct answer: ")
if answer.lower() == "a":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is A) ['pear', 'apple', 'banana'].")


answer = input("How would you sort a dictionary by values using lambda? A) sorted(d.items(), key=lambda x: x[0]) B) sorted(d.items(), key=lambda x: x[1]) C) sorted(d.items(), key=lambda x: x[2]) D) None of the above. Type the letter of the correct answer: ")
if answer.lower() == "b":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is B) sorted(d.items(), key=lambda x: x[1]).")


answer = input("What will be the output of 'list(map(lambda x: x**2, [1, 2, 3]))'? A) [1, 4, 9] B) [1, 2, 3] C) [2, 4, 6] D) [0, 1, 2]. Type the letter of the correct answer: ")
if answer.lower() == "a":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is A) [1, 4, 9].")

answer = input("What will be the output of 'lambda x: x if x > 10 else 0'(for x = 5)? A) 5 B) 0 C) 10 D) None of the above. Type the letter of the correct answer: ")
if answer.lower() == "b":
    print("Answer is correct!")
    count += 1
else:
    print("Answer is not correct. The correct answer is B) 0.")
print(f'You got {count} answer correct')