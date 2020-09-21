import place

class PlaceCollection:
  def __init__(self):
    self.places = []

  def add_place(self,placeObject):
    self.places.append(placeObject)
    
  def load_places(self):
    filename=input("Please provide the file to load : ")
    fh=open(filename,"r")
    for i in fh:
        fields=i.split(",")
        p1=place(fields[0],fields[1],fields[3],fields[2])
        self.places.append(p1)
        

  def save_places(self):
    fh=open("TravelDetails.csv","w")
    for pl in self.places:
        fh.write(pl.name + "," + pl.country + "," + pl.visited_status + "," + pl.priority() + "\n")

    fh.close()    
    
  def get_visited_places(self):
    count=0
    for pl in self.places:
       if p1.visited_status.lower()=='y':
            count+=1
    return count
    
  def sort_values(self):
    for pl in self.places:
        print("\nPlace : "+pl.name + " country : " + pl.country + " Visited Status : " + pl.visited_status + " Priority : " + pl.is_important())
        print("\n")