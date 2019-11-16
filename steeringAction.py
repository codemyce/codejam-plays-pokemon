import math

wristCoords = dict()

def read_definitions(defs):
    wristLindex = defs.index('WRISTL')
    wristRindex = defs.index('WRISTR')
    global wristCoords = {'WRISTL':wristLindex, 'WRISTR':wristRindex}

def steering(defs, n):

    turn_left = False
    turn_right = False
    
    #Angle variables
    angle = 0
    thresholdAngle = 5
    left_wristX = n[2*wristCoords['WRISTL']]
    left_wristY = n[2*wristCoords['WRISTL']+1]

    right_wristX = n[wristCoords['WRISTR']]
    right_wristY = n[wristCoords['WRISTR']+1]

    #Calculate the distane between two hands for calculating angle
    vectorOfHand = (left_wristX - right_wristX, left_wristY - right_wristY)
    distanceOfHands = math.sqrt(vectorOfHand[0]**2 + vectorOfHand[1]**2)
    #Underhand Assessment
    if vectorOfHand[0] > 0:
        angle = (math.acos(vectorOfHand[0]/distanceOfHands) * (180/math.pi))
        if vectorOfHand[1] > 0 and angle >= thresholdAngle:
            turn_left = True
        elif vectorOfHand[1] < 0 and angle >= thresholdAngle:
            turn_right = True
    #Overhand Asssessment
    elif vectorOfHand[0] < 0:
        angle = math.acos(-vectorOfHand[0]/distanceOfHands) * (180/math.pi)
        if vectorOfHand[1] > 0 and angle < 90 and angle > 60:
            turn_left = True
        if vectorOfHand[1] < 0 and angle < 90 and angle > 60:
            turn_right = True
    else:
        if vectorOfHand[1] > 0:
            turn_left = True
        elif vectorOfHand[1] < 0:
            turn_right = True
            
    return(turn_right, turn_left)