import math

path = {
    "Bordeaux": {
        "Paris": 582,
        "Madrid": 687,
        "Pise": 1168,
        "Luxembourg": 931
    },
    "Paris": {
        "Bordeaux": 582,
        "Madrid": 1270,
        "Pise": 1080,
        "Luxembourg": 358
    },
    "Madrid": {
        "Bordeaux": 687,
        "Paris": 1270,
        "Pise": 1614,
        "Luxembourg": 1619
    },
    "Pise": {
        "Bordeaux": 1168,
        "Paris": 1080,
        "Madrid": 1614,
        "Luxembourg": 957
    },
    "Luxembourg": {
        "Bordeaux": 931,
        "Paris": 358,
        "Madrid": 1619,
        "Pise": 957
    }
}

bonChoix = False
villeStart = ""
villeEnd = ""

while bonChoix == False :

    print("\nVoici la liste des trajets entre villes possible :\n")
    for key, value in path.items():
        print("| "+ key +" |")

    print(" ")

    print("Partir de la ville :")
    villeStart = input();
    if villeStart in path :
        print("\nPour aller a la ville :")
        villeEnd = input()
        if villeEnd in path :
            print("\nC'est parti !")
            print("distance : " + str(path[villeStart][villeEnd]));
            bonChoix = True
        else :
            print("\nCette ville n'est pas dans le liste des trajet possibles");
    else :
        print("\nCette ville n'est pas dans le liste des trajet possibles");

pathToDo = path[villeStart][villeEnd]
pathDone = 0
speed = 90
maxSpeed = 90
time = 0
timePause = 0
minuteCount = 0

countPrint = 0

while pathToDo > pathDone :

    if timePause >= 2:
        minuteCount += 1
        if minuteCount == 60 and speed > 0 :
            speed -= 10
            minuteCount = 0
            print("decelere" + str(speed))
            if speed == 0 :
                time += (1*15*60) / 3600
                timePause = 0
                print("pause")

    else:

        if speed < 90 :
            minuteCount += 1
            if minuteCount == 60 :
                print("accelere" + str(speed))
                speed += 10
                minuteCount = 0


    pathDone = time * speed

    #Distance toute les 10 minutes
    if countPrint % 600 == 0 :
        print(pathDone)

    time += 1 / 3600
    countPrint += 1
    timePause += 1 / 3600

heure = math.trunc(time)
min = math.ceil((time - heure) * 60)

print("\n\nLe trajet entre " + villeStart + " et " + villeEnd + " est fini.")
print("\nLa distance parcourue à été de " + str(round(pathDone, 2)) + " km.")
print("\nle trajet à été fait en "+ str(heure) +":"+ str(min) +" (\"(heures):(minutes)\"")