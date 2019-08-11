import sys

def add_line(func):
  """
    add lines before and after function
  """

  def wrapper(*args, **kwargs):
    print(line)
    func(*args, **kwargs)
    print(line)
  return wrapper

@add_line 
def register(books):
  """
  regist book
  """

  book = {}
  book["autor"] = input("Enter the autor: ")
  book["title"] = input("Enter the title: ")
  book["price"] = int(input("Enter the price: "))
  books.append(book)

@add_line
def show(books):
  """
    show registered books
  """

  if not books:
    print("You didn't registered any books yet. \n Please register before.")
    return

  average_price = 0
  sum = 0
  for book in books:
    sum += book["price"]
    average_price = sum / len(books)
  print("Average price: {0}円".format(average_price))

  print("---------registered books----------------")
  for i, book in enumerate(books):
    print("[{0}]: {1}".format(i, book["title"]))
  print("------------------------------------------")
  choose_num = int(input("Enter the book number: "))
  detail(choose_num, books)


def detail(choose_num, books):
  """
    show the book's detail
  """

  print("\n---------book's detail----------------")
  try:
    print("autor: {0}".format(books[choose_num]["autor"]))
    print("title: {0}".format(books[choose_num]["title"]))
    print("price: ¥{0}".format(books[choose_num]["price"]))
  except IndexError:
    print(INVALID_ERROR_MESSAGE)
  finally:
    print("------------------------------------------")

menus = ("Register a book","Show the book lists","exit this program")
books = []
line = "\n##############################################\n"
INVALID_ERROR_MESSAGE = "It's invalid value. Please enter again."

while True:
  print("Welcome to book register.\n")

  for i, menu in enumerate(menus):
    print("[{0}]: {1}".format(i, menu))

  try:
    num = int(input("Enter the menu number: "))
    if num == 0:
      register(books)
    elif num == 1:
      show(books)
    elif num == 2:
      print("Good bye")
      exit()
    else:
      print(INVALID_ERROR_MESSAGE)
  except ValueError:
    print(INVALID_ERROR_MESSAGE)