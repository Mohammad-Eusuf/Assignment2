import place
import placeollection

def main():
	print("\nMenu")
    print("\n1. Load CSV file")    
    print("\n2. Save to CSV file")    
    print("\n3. Add Places")    
    print("\n4. Get number of unvisited places")    
    print("\n5. Sort the places by Priority")
    choice=int(input("\nEnter between 1-5"))
    place_collection=PlaceCollection()
    
    if (choice==3):
        name=input("\nEnter the name of the place")        
        country=input("\nEnter the country")        
        priority=input("\nEnter the priority of place")        
        status=input("\nEnter the place visited status (Y or N)")
        p1 = place(name,country,priority,status)
        place_collection.add_place(p1)
        print("\nPlace Added Successfully")
        
    if (choice==4):
        print("\nThe Number of unvisited places are " + str(place_collection.get_visited_places))