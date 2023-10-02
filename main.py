from datetime import datetime
import ast

def getInput(fileName):
    with open(fileName, 'r') as file:
        lines = [line.strip() for line in file]
    fixed = []
    for i in lines:
        if i.strip():
            fixed.append(i)
    return fixed

def reformatString(input):
    fixed = input.replace("':'", "','")
    fixed = ast.literal_eval(fixed)
    return fixed
def combineSchedules(*inputs):
    output = []
    for schedule in inputs:
        if isinstance(schedule[0], list):
            for item in schedule:
                output.append(item)
        else:
            output.append(schedule)
    return output

def bubbleSort(input):
    for i in range(len(input)):
        swap = False
        for j in range(0, len(input) - i - 1):
            time1 = [datetime.strptime(input[j][0], '%H:%M').time(), datetime.strptime(input[j][1], '%H:%M').time()]
            time2 = [datetime.strptime(input[j + 1][0], '%H:%M').time(), datetime.strptime(input[j + 1][1], '%H:%M').time()]
            if time1 > time2:
                input[j], input[j + 1] = input[j + 1], input[j]
                swap = True
        if (swap == False):
            break
    return input

def mergeSchedules(input, type):
    updatedSchedule = [input[0]]
    index = 0
    for i in range(len(input)):
        startTime = datetime.strptime(input[i][0], '%H:%M').time()
        endTime = datetime.strptime(input[i][1], '%H:%M').time()
        maxTime = datetime.strptime(updatedSchedule[index][1], '%H:%M').time()

        if (type == "busy"):
            if (startTime <= maxTime) and (endTime > maxTime):
                updatedSchedule[index][1] = input[i][1]

            elif (startTime > maxTime):
                index += 1
                updatedSchedule.append(input[i])

        elif(type == "work"):
            if (startTime <= maxTime) and (endTime < maxTime):
                updatedSchedule[index][1] = input[i][1]

            elif (startTime > maxTime):
                index += 1
                updatedSchedule.append(input[i])

    return(updatedSchedule)

def getFreeSchedules(free, busy):
    output = free
    index = 0
    for i in range(len(free)):
        for j in range(len(busy)):
            minTime = datetime.strptime(output[index][0], '%H:%M')
            maxTime = datetime.strptime(output[index][1], '%H:%M')
            startBlock = datetime.strptime(busy[j][0], '%H:%M')
            if (startBlock == minTime):
                output[index] = [busy[j][1], free[i][1]]

            elif (startBlock <= maxTime):
                output.append([busy[j][1], output[index][1]])
                output[index][1] = busy[j][0]
                index += 1
    return(output)

def verifyDuration(input, duration):
    output = []
    for i in range(len(input)):
        timeA = datetime.strptime(input[i][0], '%H:%M')
        timeB = datetime.strptime(input[i][1], '%H:%M')
        if(int((timeB - timeA).total_seconds() // 60) >= duration):
            output.append(input[i])
    return output

def main(inp):
    # Overwrite if existing output.txt exists
    f = open("output.txt", "w")
    f.write("")
    f.close()

    repeat = len(inp)/5
    for i in range(int(repeat)):
        person1_busy_Schedule = reformatString(inp[0 + 5*i])
        person1_work_hours = reformatString(inp[1 + 5*i])
        person2_busy_Schedule = reformatString(inp[2 + 5*i])
        person2_work_hours = reformatString(inp[3 + 5*i])
        duration_of_meeting = reformatString(inp[4 + 5*i])

        busy = combineSchedules(person1_busy_Schedule, person2_busy_Schedule)
        work = combineSchedules(person1_work_hours, person2_work_hours)

        busy = bubbleSort(busy)
        work = bubbleSort(work)

        busy = mergeSchedules(busy, "busy")
        work = mergeSchedules(work, "work")

        work = getFreeSchedules(work, busy)
        work = verifyDuration(work, duration_of_meeting)

         # Append Case i in output.txt
        f = open("output.txt", "a")
        if (str(work) == "[]"):
            work = ["No times available for given duration"]
        f.write("Case: " + str(i + 1) + "\n" + str(work) + "\n\n")
        f.close()

    # Read output.txt in console
    f = open("output.txt", "r")
    print(f.read())

main(getInput("input.txt"))
