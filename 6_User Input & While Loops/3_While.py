# while loops until the condition is satisfied

days = {
    1 : 'mon',
    2 : 'tue',
    3 : 'wed',
    4 : 'thu',
    5 : 'fri'
}
mood = {}

day = 1
while day <= 5:
    cur_mood = input('how is your mood today( ' + days[day] + ' ): ')
    mood[day] = cur_mood
    day += 1

print('your mood during the week : ')

day = 1
while day <= 5:
    print('\ton ' + days[day] + ' you were ' + mood[day])
    day += 1