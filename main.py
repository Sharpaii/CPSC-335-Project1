person1_busy_schedule = [['12:00', '13:00'], ['16:00', '18:00']]
person1_work_hours = ['9:00', '19:00']
person2_busy_schedule = [['9:00','10:30'], ['12:20, 14:30'], ['14:30, 15:00'], ['16:00', '17:00']]
duration_of_meeting = 30

def combineSchedules(*inputs):
    output = []
    for schedule in inputs:
        if isinstance(schedule[0], list):
            for item in schedule:
                output.append(item)
        else:
            output.append(schedule)
    return output

def convertSchedules(input):
    for item in input:
        temp = []
        for time in item:
            if time[1] == ":":
                temp.append(int(time[0]))
                temp.append(int(time[2:4]))
            else:
                temp.append(int(time[0:2]))
                temp.append(int(time[3:5]))
        input[input.index(item)] = temp

def insertSort(input):
    pass

def sortSchedules(input):
    input.sort() # Change to insert sort
    temp = []
    for item in reversed(input):
        if item[0][1] == ":":
            temp.insert(0, input.pop(input.index(item)))
    for item in reversed(temp):
        input.insert(0, item)

def updateSchedules(input):
    pass

def debugPrint(input):
    for item in input:
        print(item)
    print("\n");

busy = combineSchedules(person1_busy_schedule, person1_work_hours, person2_busy_schedule)
sortSchedules(busy)
debugPrint(busy)
convertSchedules(busy)
updateSchedules(busy)
debugPrint(busy)
