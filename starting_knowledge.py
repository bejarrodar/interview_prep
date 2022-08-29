knowledge = [
"""INSERT INTO fakes(fake1,fake2,fake3) 
VALUES(
'Join takes 2 bool conditions requiring both',
'Join bring data from two columns together',
'Join groups columns together')""",
"""INSERT INTO flash_cards(category_id,question,answer,fakes_id) 
VALUES(1,'What is a join?','Join bring data from two tables together',1)""",

"""INSERT INTO fakes(fake1,fake2,fake3)
VALUES(
'Where filters on groups, and having filters on rows',
'Where and Having are the same thing',
'Having can be used without groups, Where requires groups')""",
"""INSERT INTO flash_cards(category_id,question,answer,fakes_id) 
VALUES(1,'What is the difference between a Where and a Having','Having filters on groups, and where filters on rows',2)""",

"""INSERT INTO fakes(fake1,fake2,fake3) 
VALUES(
'SELECT * GROUP BY * WHERE * HAVING *',
'SELECT * WHERE * HAVING * GROUP BY *',
'GROUP BY * HAVING * SELECT * WHERE *')""",
"""INSERT INTO flash_cards(category_id,question,answer,fakes_id) 
VALUES(1,'What is the correct order of SELECT,WHERE,GROUP BY,HAVING','SELECT * WHERE * GROUP BY * HAVING *',3)""",

"""INSERT INTO fakes(fake1,fake2,fake3) 
VALUES(
'UNIQUE',
'EACH',
'EXPLICIT')""",
"""INSERT INTO flash_cards(category_id,question,answer,fakes_id) 
VALUES(1,'How do you do selections to eliminate any duplicate records in a column?','DISTINCT',4)""",

"""INSERT INTO fakes(fake1,fake2,fake3) 
VALUES(
'None',
'break',
'except')""",
"""INSERT INTO flash_cards(category_id,question,answer,fakes_id) 
VALUES(2,'Which of the following is not a reserved word in Python','iterate',5)""",

"""INSERT INTO fakes(fake1,fake2,fake3) 
VALUES(
'A set of curly brackets',
'The end of one semicolin to the next',
'A set of angle brackets')""",
"""INSERT INTO flash_cards(category_id,question,answer,fakes_id) 
VALUES(2,'A code block is defined by:','Indentation and whitespace',6)""",

"""INSERT INTO fakes(fake1,fake2,fake3) 
VALUES(
'Yes, an empty code block will be ignored',
'Yes, an empty code block is the same as return None',
'No, however the Nothing keyword can be used to make the code block do nothing')""",
"""INSERT INTO flash_cards(category_id,question,answer,fakes_id) 
VALUES(2,'Can you have an empty code block?','No, however the pass keyword can be used to make the code block do nothing',7)""",

"""INSERT INTO fakes(fake1,fake2,fake3) 
VALUES(
'A list is ordered a tuple is not',
'A list is indexed a tuple is not',
'A list can have duplicates a tuple can not')""",
"""INSERT INTO flash_cards(category_id,question,answer,fakes_id) 
VALUES(2,'The difference between a list and a tuple is:','A list is mutable a tuple is not',8)"""
]
