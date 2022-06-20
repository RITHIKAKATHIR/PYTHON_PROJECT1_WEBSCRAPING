from bs4 import BeautifulSoup

# you are opening the file as an instance with name html_file
with open('webpage.html', 'r') as html_file:
    content = html_file.read()  # the contents of the instance of the file is read into contents
    # Prints the contents:  print(content)
    soup = BeautifulSoup(content, 'html.parser')  # Instance as a soup with html parser
    tags = soup.find_all('h5')  # Finds all the tags with h5 and prints. if we use only find instad of find_all,
    # only the first instance of h5 will be printed
    for courses in tags:
          print(courses.text)  # instead of the whole html line, only the text of those html lines are printed
          