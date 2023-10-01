from datetime import datetime
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
            endBlock = datetime.strptime(busy[j][1], "%H:%M")
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

def debugPrint(input):
    for item in input:
        print(item)
    print("\n");

def main():
    busy = combineSchedules(person1_busy_Schedule, person2_busy_Schedule)
    work = combineSchedules(person1_work_hours, person2_work_hours)

    busy = bubbleSort(busy)
    work = bubbleSort(work)

    # print("All Busy Times")
    # debugPrint(busy)
    # print("All Work Times")
    # debugPrint(work)

    busy = mergeSchedules(busy, "busy")
    work = mergeSchedules(work, "work")

    # print("Condensed Busy Times")
    # debugPrint(busy)
    # print("Condensed Work Times")
    # debugPrint(work)

    work = getFreeSchedules(work, busy)
    work = verifyDuration(work, duration_of_meeting)
    print("Get Free Work Times")
    debugPrint(work)

# TEST CASE 1
person1_busy_Schedule = [['12:00', '13:00'], ['16:00', '18:00']]
person1_work_hours = ['9:00', '19:00']
person2_busy_Schedule = [['9:00','10:30'], ['12:20', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
person2_work_hours = ['9:00', '18:30']
duration_of_meeting = 30

main()

# TEST CASE 2
person1_busy_Schedule = [['12:00','13:00'],['14:00','15:00']]
person1_work_hours = ['9:00','19:00']
person2_busy_Schedule = [['10:15','11:00'],['11:30','12:45'],['14:00','16:00']]
person2_work_hours = ['9:00','18:30']
duration_of_meeting = 30

main()


# TEST CASE 3
person1_busy_Schedule = [['12:00','13:00'],['14:00','15:00']]
person1_work_hours = ['9:00','19:00']
person2_busy_Schedule = [['10:15','11:00'],['11:30','12:45'],['14:00','16:00']]
person2_work_hours = ['9:00','18:30']
duration_of_meeting = 120

main()


# TEST CASE 4
person1_busy_Schedule = [['10:00','13:00'],['14:00','15:00']]
person1_work_hours = ['9:00','19:00']
person2_busy_Schedule = [['10:15','11:00'],['11:30','12:45'],['14:00','16:00']]
person2_work_hours = ['9:00','18:30']
duration_of_meeting = 60

main()
