# Electic Car Problem

## Problem statement
Electric cars do not have as large a range as gas cars, so they need periodic recharge. Assume
that one needs to travel a large distance, that cannot be done in one charge, so one needs to
stop to recharge and continue. But some of the chargers may not function, in case you need to
drive back to the previous city and re-charge there. Given a capacity C in miles that represents
the maximum number of miles your electric car can drive, n cities and (n-1) distances between
two consecutive cities, design an algorithm that outputs the list L of cities where one need to
stop and charge the car such that:
L is if minimum length among all possible list of cities
the starting city, which is the first city, is the first element of L
The destination city, which is the last city, is the last element of L
If j and k are two consecutive cities in L, then when the car is in city j, the car is able to drive to
city k and back to the city before city k, in case the charge station in city k is broken.
The capacity C in miles is not fixed, but one can assume that is a positive integer between 250
and 350. The number of cities n is not fixed, but you can assume that it is greater than 3 and
less than 20. The distance between cities is a positive integer and always less than C/2 and
greater than 10.
## Solution
The above problem has been solved using Python language. We first used linked list as the
data structure for solving the problem. But upon further analysis we found that the space
complexity of the problem can be further improved if we use lists instead of a linked list.
Therefore, we again solved the problem using list data structure.
## Pseudocode 1:
Data structure - Linked List
```
TravelGraph():
city = current city/node
next = next city/node
previous = previous city/node
nextCost = cost for travelling to next city
prevCost = cost for travelling to previous city
carMaxCharge = Total charge capacity of car in miles
cityNo = Total number of cities/nodes
cityList = list of cities
costList = list of vertex costs
current = TravelGraph()
graphStartRef = current
for i->0 to cityNo:
cityList.append(“Enter the {i+1} city name”)
current.city = cityList[i]
If i < cityNo -1:
current.next = TravelGraph()
If i > 0:
costList.append(“Enter cost of travelling from {cityList[i-1]} to {cityList[i]}: ")
previous.nextCost = costList[i-1]
current.previous = previous
current.prevCost = costList[i-1]
previous, current = current, current.next
if i == 0:
currentMap = f"{cityList[i]}"
elif i < cityNo:
currentMap = currentMap + f" <- {costList[i-1]} -> {cityList[i]}"
print(currentMap)
current = current back to start of linked list
currentCharge = carMaxCharge #creating variable to keep track of current charge
stopsList = list of stops
stopsList.append(cityList[0])
while(current.city is not equal to cityList[-1]):
If currentCharge >= current.nextCost *2
currentCharge -= current.nextCost
current = current.next
Else:
currentCharge = carMaxCharge
stopsList.append(current.city)
currentCharge -= current.nextCost
current = current.next
stopsList.append(cityList[-1])
print("Output-> Here are the suggested stops: " + str(stopsList))
```
The time complexity for the above code is linear that is O(n) where n is the number of cities.

## Pseudocode 2:
Data Structure - List. Here we have used two lists for the input and one list for the output.
```
maxCharge = max mileage that car gives per charge
cityList = list of cities/nodes
vertexCostList = Enter the list of costs
if len(vertexCostList) != len(cityList) - 1:
print("Error: The number of vertices/costs should be equal to number of nodes - 1")
else:
vertexCostList = [int(cost) for cost in vertexCostList]
currentCarCharge = maxCharge # variable to keep track of current car charge as it travels
stopsList + output list with suggested stops
stopsList.append(cityList[0])
for i in range(len(vertexCostList)):
if currentCarCharge >= vertexCostList[i] * 2:
currentCarCharge -= vertexCostList[i]
Else:
currentCarCharge = maxCharge
currentCarCharge -= vertexCostList[i]
stopsList.append(cityList[i])
stopsList.append(cityList[-1])
print("Output-> Here are the suggested stops: " + str(stopsList))
```
The time complexity for the above code is linear that is O(n) again, where n is the number of
cities.
The space complexity is however optimized using list data structure.
