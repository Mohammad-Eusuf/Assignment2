import place

class PlaceCollection:
  def __init__(self):
    self.places = []

  def add_place(self,placeObject):
    self.places.append(placeObject)
    
  def load_places(self):
    print( "")

  def save_places(self):
    print( "")
    
  def get_visited_places(self):
    count=0
    for pl in self.places:
       if p1.visited_status.lower()=='y':
            count+=1
    return count
    
  def sort_values(self):
    print( "")