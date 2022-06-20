from bs4 import BeautifulSoup

# you are opening the file as an instance with name html_file
with open('webpage.html', 'r') as html_file:
    content = html_file.read()  # the contents of the instance of the file is read into contents
    # Prints the contents:  print(content)
    soup = BeautifulSoup(content, 'html.parser')  # Instance as a soup with html parser
    course_cards = soup.find_all('div', class_='card')  # fetching div cards with class names as card
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]

        print(f'{course_name} costs {course_price}')




