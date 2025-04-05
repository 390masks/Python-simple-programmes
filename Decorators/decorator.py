def my_decorator(func):
  def my_wrapper():
    print("print before Function")
    func()
    print("print after function")
  return my_wrapper

@my_decorator
def greeting():
  print("I am the middile peace....!")

greeting()
