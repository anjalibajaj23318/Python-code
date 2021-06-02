names = ["Chandler Bling","Phoebe Buffay","Monica Geller","Ross Geller"]
assignments =  [3,6,0,2]
grades =  [81,77,92,88]


# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

for name,assignment,grade in zip(names,assignments,grades):
    print(message.format(name,assignment,grade,int(grade)+2*int(assignment)))