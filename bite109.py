#workout_schedule = {'Friday': 'Shoulders',
#                    'Monday': 'Chest+biceps',
#                    'Saturday': 'Rest',
#                    'Sunday': 'Rest',
#                    'Thursday': 'Legs',
#                    'Tuesday': 'Back+triceps',
#                    'Wednesday': 'Core'}
#rest, chill, go_train = 'Rest', 'Chill out!', 'Go train {}'
#
#day = input("Dag: ")
#
#try:
#    if day in workout_schedule.keys():
#        if workout_schedule[day] == "Rest":
#            print(f"{rest}. {chill}")
#        else:
#            print(f"{go_train}".format(workout_schedule[day]))
#except Exception:
#    KeyError
    
workout_schedule = {'Friday': 'Shoulders',
                    'Monday': 'Chest+biceps',
                    'Saturday': 'Rest',
                    'Sunday': 'Rest',
                    'Thursday': 'Legs',
                    'Tuesday': 'Back+triceps',
                    'Wednesday': 'Core'}
rest, chill, go_train = 'Rest', 'Chill out!', 'Go train {}'


def get_workout_motd(day):
    """Title case passed in day argument (monday or MONDAY -> Monday)
       and check if it is in the given workout_schedule dict.

       If it is there retrieve the workout, if not raise a KeyError.

       Return the chill or go_train variable depending the retrieved
       workout value ('Rest' or workout bla)

       Trivia: /etc/motd is a file on Unix-like systems that contains
       a 'message of the day'"""
    try:
        training = workout_schedule[day]
        if training == "Rest":
            return chill
        else:
            return go_train.format(training)
    except KeyError:
        print(f"\nGo fix input!:")
        raise

print(get_workout_motd("Tuesday"))
print(get_workout_motd("Sunday"))
print(get_workout_motd("Tusday"))
