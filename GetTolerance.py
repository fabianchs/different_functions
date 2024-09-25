def GetTolerance(thickness,concentricity):

    upper_thick, lower_thick = thickness, thickness
    percentage=int((lower_thick/upper_thick)*100)

    while(percentage!=concentricity-1):
        upper_thick+=1
        lower_thick-=1
        percentage=int((lower_thick/upper_thick)*100)

    return("Lower thickness:",lower_thick,"Upper thickness:",upper_thick, "Concentricity:",round((lower_thick/upper_thick)*100,2),"Tolerance:", upper_thick-lower_thick)

print(GetTolerance(1465,85))