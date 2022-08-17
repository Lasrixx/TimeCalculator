def add_time(*args):
    dayGiven = False
    daysOfWeek = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    #Get all the arguments sorted into variables
    startTime = args[0]
    duration = args[1]
    if len(args) == 3:
        startDay = args[2].lower()
        i=0
        while i < 7:
            if(startDay == daysOfWeek[i]):
                startDayIndex = i
                i=7 #Just to break the loop quicker
            i+=1
        dayGiven = True

    #Convert start time to a 24-hour clock to make it easier to do the maths on
    splitStartTime = startTime.split(" ")
    amPm = splitStartTime[1]
    startHour = int(splitStartTime[0].split(":")[0])
    startMin = int(splitStartTime[0].split(":")[1])
    if(amPm == "PM"):
        startHour+=12
    
    #Split duration time into hour and minutes
    durationHour = int(duration.split(":")[0])
    durationMin = int(duration.split(":")[1])

    #Add the duration to the start time
    endHour = startHour + durationHour
    endMin = startMin + durationMin

    #Sort out the formatting (e.g. if there is more than 60 minutes, increase the hour instead)
    if(endMin >= 60):
        endHour += 1
        endMin = 00 + (endMin-60)
    #Divide hours by 24 to give days (the integer will be the amount of days that have passed, and the decimal will give an indication of whether it is am or pm)
    endDay = endHour / 24.0
    if endHour%24 == 0:
        endTime = "12:"
    elif endHour%24>12:
        endTime = str((endHour % 24)-12) + ":"
    else:
        endTime = str(endHour % 24) + ":"
    if len(str(endMin)) == 1:
        endTime += "0" + str(endMin) 
    else:
        endTime += str(endMin)
    if int(str(endDay).split(".")[1]) / 10**len(str(endDay).split(".")[1]) < 0.5:
        endTime += " AM"
    else:
        endTime += " PM"
    daysOn = int(str(endDay).split(".")[0])   
    if(dayGiven == True):
        if startDayIndex + daysOn > 6:
            endTime += ", " + str.capitalize(str(daysOfWeek[(startDayIndex+daysOn)%7]))
        else:
            endTime += ", " + str.capitalize(str(daysOfWeek[startDayIndex+daysOn]))
    if daysOn == 1:
        endTime += " (next day)"
    elif daysOn!=0:
        endTime += " (" + str(daysOn) + " days later)"

    return endTime



print(add_time("11:59 PM", "24:05"))

