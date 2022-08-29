categories = """
CREATE TABLE categories(
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category varchar(255)
)"""

fakes = """
CREATE TABLE fakes(
    fakes_id INT AUTO_INCREMENT PRIMARY KEY,
    fake1 TEXT,
    fake2 TEXT,
    fake3 TEXT
)"""

flash_cards = """
CREATE TABLE flash_cards(
    flash_id INT AUTO_INCREMENT PRIMARY KEY,
    category_id int,
    answer TEXT,
    question TEXT,
    fakes_id INT,
    FOREIGN KEY (category_id) REFERENCES categories(category_id),
    FOREIGN KEY (fakes_id) REFERENCES fakes(fakes_id)
)"""

projects = """
CREATE TABLE projects(
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    mistakes BLOB,
    enjoyed BLOB,
    changes BLOB,
    leadership BLOB DEFAULT NULL,
    conflicts BLOB DEFAULT NULL
)"""

questions = """
CREATE TABLE questions(
    question_id INT AUTO_INCREMENT PRIMARY KEY,
    question BLOB
)"""
