call_minutes = float(input("How many minutes did the call last?\n> "))
total_hours = int(call_minutes//60)                          #Total call hours
remaining_min_1 = int(call_minutes%60)  #Yields the integer part of the number
remaining_min_2 = call_minutes%60    #Yields the whole number as a float value

conditional = remaining_min_2//60   #Save the integer's value of remaining_min

if (conditional == 0):                                 #If the integer is zero
    #Convert the remainung minutes in seconds
    total_secs = (remaining_min_2-remaining_min_1)*10
else:                                    #If the integer is bigger than zero
    total_secs = remaining_min_2//60
print(total_hours,"hours,", remaining_min_1,"min,",total_secs,"secs")
