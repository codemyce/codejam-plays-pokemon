import math

def steering(definitionArray, n):
    LWristIndex = 0
    RWristIndex = 0
    for k in definitionArray:
        if definitionArray[k] == 'LWRIST':
            LWristIndex = k
        elif definitionArray[k] == 'RWRIST':
            RWristIndex = k
        else:
            continue
    
    #Return variables
    turn_left = False
    turn_right = False
    
    #Angle variables
    angle = 0
    thresholdAngle = 5
    
    #Position variable
    left_wristX = n[(2*LWristIndex)]
    left_wristY = n[(2*LWristIndex + 1)]
    right_wristX = n[(2*RWristIndex)]
    right_wristY = n[(2*RWristIndex + 1)]

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