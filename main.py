import mediapipe as mp

def agecalculation(y,m,d):
    import datetime
    today =datetime.datetime.now().date()
    dob =datetime.date(y, m, d)
    age = int((today-dob).days/365.25)
    print(age)

agecalculation(1989,4,24)

