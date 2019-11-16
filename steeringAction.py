import json
import pprint
import math

def json_r (filename):
    with open(filename) as f_in:
        return (json.load(f_in))

def steering(n):
    pose_estimation = json_r(n)
    man_pose = pose_estimation['frames'][0]['persons'][0]

    turn_left = False
    turn_right = False
    angle = 0

    left_wristX = man_pose['pose2d']['joints'][30]
    left_wristY = man_pose['pose2d']['joints'][31]

    right_wristX = man_pose['pose2d']['joints'][20]
    right_wristY = man_pose['pose2d']['joints'][21]

    #Calculate the distane between two hands for calculating angle
    vectorOfHand = (left_wristX - right_wristX, left_wristY - right_wristY)
    distanceOfHands = math.sqrt(vectorOfHand[0]**2 + vectorOfHand[1]**2)
    #Underhand Assessment
    if vectorOfHand[0] > 0:
        angle = (math.acos(vectorOfHand[0]/distanceOfHands) * (180/math.pi))
        if vectorOfHand[1] > 0 and angle >= 10:
            turn_left = True
        elif vectorOfHand[1] < 0 and angle >= 10:
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
            
    return(turn_left, turn_right)