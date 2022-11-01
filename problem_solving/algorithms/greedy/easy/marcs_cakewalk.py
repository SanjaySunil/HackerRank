def marcsCakewalk(calorie):
    val = 0
    power = 0
    while len(calorie) != 0:
        val += pow(2, power) * max(calorie)
        calorie.remove(max(calorie))
        power+=1
    return val
