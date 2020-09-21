import place
import placecollection

def main():
    choice=1
    place_collection=placecollection.PlaceCollection([])
    while (choice>0 and choice<6):
        print("\n**********Menu*****************\n")
        print("\n1. Load CSV file")    
        print("\n2. Save to CSV file")    
        print("\n3. Add Places")    
        print("\n4. Get number of unvisited places")    
        print("\n5. Sort the places by Priority")
        choice=int(input("\nEnter between 1-5 : "))
        

        if (choice==1):
            place_collection.load_places()
            print("File is uploaded successfully")
            
        
        if (choice==2):
            place_collection.save_places()
            print("The file downloaded successfully")
        if (choice==3):
            name=input("\nEnter the name of the place : ")        
            country=input("\nEnter the country : ")        
            priority=input("\nEnter the priority of place : ")        
            status=input("\nEnter the place visited status (Y or N) : ")
            p1 = place.place(name,country,priority,status)
            print("\nPlace entered is : ",p1.name)
            place_collection.add_place(p1)
            print("\nPlace Added Successfully")
        
        if (choice==4):
            print("\nThe Number of unvisited places are " + str(place_collection.get_visited_places()))

        if (choice==5):
            print("\nBelow are the places : ")
            place_collection.sort_values()
        
        
main()