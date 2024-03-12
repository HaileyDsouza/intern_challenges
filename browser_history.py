# A class to represent a node in a doubly linked list
class Node:
  def __init__(self, url: str):
    # The previous and next nodes in the list
    self.prev = None
    self.next = None
    # The URL represented by this node
    self.url = url

# A class to represent a browser history
class BrowserHistory:
  def __init__(self, homepage: str):
    # Create a new node to represent the homepage
    self.curr = Node(homepage)

  # Method to add a new URL to the history
  def visit(self, url: str) -> None:
    # Create a new node to represent the new URL
    self.curr.next = Node(url)
    # Set the previous node for the new node to be the current node
    self.curr.next.prev = self.curr
    # Make the new node the current node
    self.curr = self.curr.next

  # Method to navigate back in the history by the given number of steps
  def back(self, steps: int) -> str:
    # While there are previous nodes and we haven't gone back enough steps yet
    while self.curr.prev and steps > 0:
      # Move back one node by setting the current node to the previous node
      self.curr = self.curr.prev
      steps -= 1
    # Return the URL represented by the current node
    return self.curr.url

  # Method to navigate forward in the history by the given number of steps
  def forward(self, steps: int) -> str:
    # While there are next nodes and we haven't gone forward enough steps yet
    while self.curr.next and steps > 0:
      # Move forward one node by setting the current node to the next node
      self.curr = self.curr.next
      steps -= 1
    # Return the URL represented by the current node
    return self.curr.url
  
  """ 
  You have a browser of one tab where you start on the homepage and you can visit another url, 
  get back in the history number of steps or move forward in the history number of steps.
Implement the BrowserHistory class:
- BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
- void visit(string url) Visits url from the current page. It clears up all the forward history.
- string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. 
Return the current url after moving back in history at most steps.
- string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps.
Return the current url after forwarding in history at most steps.
  """