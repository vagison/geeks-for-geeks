# Facing the sun
# https://practice.geeksforgeeks.org/problems/facing-the-sun2126/1

def countBuildings(h, n):
    currentHighestBuildingsHeight = 0
    amountOfBuildings = 0

    for buildingNumber in range(0, n):
        if h[buildingNumber] > currentHighestBuildingsHeight:
            amountOfBuildings += 1
            currentHighestBuildingsHeight = h[buildingNumber]

    return amountOfBuildings
