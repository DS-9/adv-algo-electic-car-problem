# TravelGraph: A Class which helps in building a linked list to represent the Travel Map/Input Graph.
class TravelGraph():
    def __init__(self):
        self.city = None # current city/node
        self.next = None # points to next city/node
        self.previous = None # points to previous city/node
        self.nextCost = None # cost to travel next vertice
        self.prevCost = None # cost to travel previous vertice

carMaxCharge = int(input("Enter the car mileage in one charge: ")) # Total charge capacity of car in miles
cityNo = int(input("How many cities are there on the map: ")) # Total number of cities/nodes
cityList = [] # stores list of cities
costList = [] # stores list of vertex costs
current = TravelGraph() # current will always point to curent node/city
graphStartRef = current # graphStartRef is a reference to the start of the linked list

# for loop to build the travel map/input graph: Time Complexity O(number of nodes/cities)
for i in range(cityNo):
    cityList.append(input(f"Enter the {i+1} city name: "))
    current.city = cityList[i]
    if i < cityNo - 1:
        current.next = TravelGraph()
    if i > 0:
        costList.append(int(input(f"Enter cost of travelling from {cityList[i-1]} to {cityList[i]}: ")))
        previous.nextCost = costList[i-1]
        current.previous = previous
        current.prevCost = costList[i-1]
    previous, current = current, current.next
    if i == 0:
        currentMap = f"{cityList[i]}"
    elif i < cityNo:
        currentMap = currentMap + f" <- {costList[i-1]} -> {cityList[i]}"
    print(currentMap)

current = graphStartRef # pointing current back to start of linked list
currentCharge = carMaxCharge # creating variable to keep track of current charge
stopsList = [] # list of stops i.e. our desired output 
stopsList.append(cityList[0]) # appending first node/city to mark our start

# while loop to iterate/travel until we reach the final node/city: Time Complexity O(number of nodes/cities)
while(current.city != cityList[-1]):
    if currentCharge >= current.nextCost * 2: #travel ahead if enough fuel to backtrack to same city.
        currentCharge -= current.nextCost
        current = current.next
    else: #take a stop and charge if not enough fuel to backtrack to same city.
        currentCharge = carMaxCharge
        stopsList.append(current.city)
        currentCharge -= current.nextCost
        current = current.next
        
stopsList.append(cityList[-1]) # adding our destination/final stop into the stop list
print("Output-> Here are the suggested stops: " + str(stopsList)) # our final desired output i.e. list of stops

# Time Complexity = O(n) wherein n = No of Nodes/Cities.
# Space Complexity can be improved by using just 2 lists for input and 1 for output.



    
    
    











