
class place:
  def __init__(self, name, country,priority,visited_status):
    self.name = name
    self.country = country
    self.priority = priority
    self.visited_status = visited_status
    
  def __str__(self, name, age):
    print("")
    
  def mark_visited(self):
    self.visited_status='Y'
    
  def mark_unvisited(self):
    self.visited_status='N'