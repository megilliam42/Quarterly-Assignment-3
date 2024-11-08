###creates database for  GUI window2 to read and readfromdatabase can also edit the data base

import sqlite3 

# Create a connection to the SQLite database (it will create the file if it doesn't exist)
conn = sqlite3.connect('solar_system_questions.db')  # Adjusted to use your existing 'questions.db' file

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create the solar_systems table to store space-related questions and answers (if not already created)
cursor.execute('''
CREATE TABLE IF NOT EXISTS solar_systems (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT,
    answer_a TEXT,
    answer_b TEXT,
    answer_c TEXT,
    answer_d TEXT,
    correct_answer TEXT
)
''')

# Create the geography table to store geography-related questions and answers (if not already created)
cursor.execute('''
CREATE TABLE IF NOT EXISTS geography (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT,
    answer_a TEXT,
    answer_b TEXT,
    answer_c TEXT,
    answer_d TEXT,
    correct_answer TEXT
)
''')

# Create the literature table to store literature-related questions and answers (if not already created)
cursor.execute('''
CREATE TABLE IF NOT EXISTS literature (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT,
    answer_a TEXT,
    answer_b TEXT,
    answer_c TEXT,
    answer_d TEXT,
    correct_answer TEXT
)
''')

# Create the python table to store Python-related questions and answers (if not already created)
cursor.execute('''
CREATE TABLE IF NOT EXISTS python (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT,
    answer_a TEXT,
    answer_b TEXT,
    answer_c TEXT,
    answer_d TEXT,
    correct_answer TEXT
)
''')

# Create the art table to store art-related questions and answers (if not already created)
cursor.execute('''
CREATE TABLE IF NOT EXISTS art (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT,
    answer_a TEXT,
    answer_b TEXT,
    answer_c TEXT,
    answer_d TEXT,
    correct_answer TEXT
)
''')

# List of Solar System questions, answers, and correct answers for the solar_systems table
solar_system_questions_data = [
    ("Which planet is known as the 'Red Planet'?", "Venus", "Mars", "Jupiter", "Saturn", "Mars"),
    ("What is the largest planet in the solar system?", "Earth", "Jupiter", "Saturn", "Neptune", "Jupiter"),
    ("Which planet has the longest day?", "Venus", "Mercury", "Earth", "Mars", "Venus"),
    ("Which planet is closest to the Sun?", "Earth", "Mercury", "Venus", "Mars", "Mercury"),
    ("Which planet has the most moons?", "Jupiter", "Saturn", "Uranus", "Neptune", "Saturn"),
    ("What is the name of the fifth planet from the Sun?", "Mars", "Jupiter", "Venus", "Earth", "Jupiter"),
    ("Which planet is known for its prominent ring system?", "Uranus", "Saturn", "Neptune", "Mars", "Saturn"),
    ("Which planet has the strongest winds in the solar system?", "Neptune", "Jupiter", "Uranus", "Venus", "Neptune"),
    ("Which dwarf planet is located in the Kuiper Belt?", "Pluto", "Eris", "Ceres", "Haumea", "Pluto"),
    ("What is the largest moon of Saturn?", "Titan", "Ganymede", "Callisto", "Europa", "Titan"),
    ("Which planet has a tilted axis that causes extreme seasons?", "Uranus", "Mars", "Earth", "Neptune", "Uranus")
]

# List of Geography questions, answers, and correct answers for the geography table
geography_questions_data = [
    ("What is the capital of France?", "Berlin", "Madrid", "Paris", "Rome", "Paris"),
    ("Which country has the largest land area?", "China", "Russia", "Canada", "United States", "Russia"),
    ("What is the longest river in the world?", "Amazon River", "Nile River", "Yangtze River", "Mississippi River", "Nile River"),
    ("Which is the smallest country in the world by land area?", "Monaco", "San Marino", "Vatican City", "Liechtenstein", "Vatican City"),
    ("Which ocean is the largest?", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean", "Pacific Ocean"),
    ("Mount Everest is located in which country?", "China", "India", "Nepal", "Pakistan", "Nepal"),
    ("Which continent is known as the 'Dark Continent'?", "Asia", "Africa", "Europe", "Australia", "Africa"),
    ("Which desert is the largest in the world?", "Kalahari Desert", "Sahara Desert", "Gobi Desert", "Atacama Desert", "Sahara Desert"),
    ("What is the largest island in the world?", "Australia", "Greenland", "New Guinea", "Borneo", "Greenland"),
    ("Which country is known as the 'Land of the Rising Sun'?", "China", "Japan", "South Korea", "Thailand", "Japan"),
    ("Which river is the longest in Europe?", "Rhine River", "Danube River", "Volga River", "Seine River", "Volga River")
]

# List of Literature questions, answers, and correct answers for the literature table
literature_questions_data = [
    ("Who wrote 'Pride and Prejudice'?", "Charlotte Brontë", "Jane Austen", "Mary Shelley", "Emily Brontë", "Jane Austen"),
    ("In which novel does the character 'Atticus Finch' appear?", "1984", "To Kill a Mockingbird", "The Great Gatsby", "Moby Dick", "To Kill a Mockingbird"),
    ("What is the name of the wizard in 'The Hobbit'?", "Saruman", "Gandalf", "Dumbledore", "Merlin", "Gandalf"),
    ("Who is the author of 'The Catcher in the Rye'?", "F. Scott Fitzgerald", "J.D. Salinger", "Ernest Hemingway", "Mark Twain", "J.D. Salinger"),
    ("Which Shakespeare play features the character 'Prospero'?", "Macbeth", "Hamlet", "The Tempest", "Othello", "The Tempest"),
    ("In '1984,' what is the name of the Party's leader?", "Big Brother", "The Chairman", "The Leader", "The Watcher", "Big Brother"),
    ("Which book begins with 'Call me Ishmael'?", "Moby Dick", "The Odyssey", "War and Peace", "Frankenstein", "Moby Dick"),
    ("Who wrote 'One Hundred Years of Solitude'?", "Gabriel Garcia Marquez", "Pablo Neruda", "Isabel Allende", "Jorge Luis Borges", "Gabriel Garcia Marquez"),
    ("In 'The Great Gatsby,' what is Gatsby's first name?", "James", "Nick", "Jay", "Tom", "Jay"),
    ("Who is the author of 'Frankenstein'?", "Mary Shelley", "Percy Shelley", "Bram Stoker", "Robert Louis Stevenson", "Mary Shelley")
]

# List of Python questions, answers, and correct answers for the python table
python_questions_data = [
    ("What keyword is used to define a function in Python?", "func", "define", "def", "function", "def"),
    ("What data type is returned by the input() function?", "int", "str", "float", "bool", "str"),
    ("How do you start a comment in Python?", "//", "/*", "#", "<!--", "#"),
    ("Which of the following is a mutable data type?", "tuple", "int", "str", "list", "list"),
    ("What does 'PEP' stand for in Python?", "Python Enhancement Proposal", "Python Enterprise Project", "Programming Efficiently in Python", "Python Essential Package", "Python Enhancement Proposal"),
    ("Which function is used to output data in Python?", "output()", "print()", "display()", "write()", "print()"),
    ("What is the output of 3**2 in Python?", "6", "9", "12", "None of the above", "9"),
    ("Which module is used to generate random numbers in Python?", "math", "random", "os", "sys", "random"),
    ("How do you create a list in Python?", "{}", "[]", "()", "<>", "[]"),
    ("What is the correct file extension for Python files?", ".py", ".python", ".pt", ".pyt", ".py")
]

# List of Art questions, answers, and correct answers for the art table
art_questions_data = [
    ("Who painted the 'Mona Lisa'?", "Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet", "Leonardo da Vinci"),
    ("What art movement is Salvador Dalí associated with?", "Cubism", "Surrealism", "Impressionism", "Expressionism", "Surrealism"),
    ("Which artist is famous for the painting 'Starry Night'?", "Michelangelo", "Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh"),
    ("Where is the Louvre Museum located?", "London", "Paris", "Rome", "New York", "Paris"),
    ("Which art movement focused on capturing light and natural forms?", "Cubism", "Realism", "Impressionism", "Surrealism", "Impressionism"),
    ("Who sculpted 'David'?", "Donatello", "Raphael", "Michelangelo", "Leonardo da Vinci", "Michelangelo"),
    ("In which country was Pablo Picasso born?", "Italy", "Spain", "France", "Portugal", "Spain"),
    ("What is the main characteristic of Cubism?", "Realistic detail", "Distorted forms", "Geometric shapes", "Use of light", "Geometric shapes"),
    ("Which artist is known for 'The Persistence of Memory'?", "Salvador Dalí", "Henri Matisse", "Andy Warhol", "Frida Kahlo", "Salvador Dalí"),
    ("What technique did Georges Seurat use to create his paintings?", "Watercolor", "Pointillism", "Cubism", "Surrealism", "Pointillism")
]

# Insert Solar System questions and answers into the solar_systems table
cursor.executemany('''
INSERT INTO solar_systems (question, answer_a, answer_b, answer_c, answer_d, correct_answer)
VALUES (?, ?, ?, ?, ?, ?)
''', solar_system_questions_data)

# Insert Geography questions and answers into the geography table
cursor.executemany('''
INSERT INTO geography (question, answer_a, answer_b, answer_c, answer_d, correct_answer)
VALUES (?, ?, ?, ?, ?, ?)
''', geography_questions_data)

# Insert Literature questions and answers into the literature table
cursor.executemany('''
INSERT INTO literature (question, answer_a, answer_b, answer_c, answer_d, correct_answer)
VALUES (?, ?, ?, ?, ?, ?)
''', literature_questions_data)

cursor.executemany('''
INSERT INTO python (question, answer_a, answer_b, answer_c, answer_d, correct_answer)
VALUES (?, ?, ?, ?, ?, ?)
''', python_questions_data)

cursor.executemany('''
INSERT INTO art (question, answer_a, answer_b, answer_c, answer_d, correct_answer)
VALUES (?, ?, ?, ?, ?, ?)
''', art_questions_data)

# Commit the changes to save data
conn.commit()

# Confirm that the data was added
print("Questions and answers added to 'solar_systems', 'geography', 'literature', 'python', and 'art' tables.")
# Close the connection
conn.close()
