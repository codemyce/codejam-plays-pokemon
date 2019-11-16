import math


def read_definitions(defs):
    wristLindex = defs.index('LWRIST')
    wristRindex = defs.index('RWRIST')
    return {'LWRIST':wristLindex, 'RWRIST':wristRindex}

def steering(wristCoords, n):

    turn_left = False
    turn_right = False
    
    #Angle variables
    angle = 0
    thresholdAngle = 5
    left_wristX = n[2*wristCoords['LWRIST']]
    left_wristY = n[2*wristCoords['LWRIST']+1]

    right_wristX = n[wristCoords['RWRIST']]
    right_wristY = n[wristCoords['RWRIST']+1]

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