
class place:
  def __init__(self, name, country,priority,visited_status):
    self.name = name
    self.country = country
    self.priority = priority
    self.visited_status = visited_status
    
  def __str__(self):
    print("\nPlace : " + self.name + " country : " + self.country + " Visited Status : " + self.visited_status + " Priority : " + self.is_important())
    
  def mark_visited(self):
    self.visited_status='Y'
    
  def mark_unvisited(self):
    self.visited_status='N'
    
  def is_important(self):
    if int(self.priority)<=2:
        return "Important"
    else:
        return "Not Important"