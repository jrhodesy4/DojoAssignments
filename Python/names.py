students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def names(students):
    for i in students:
        print i['first_name'] + ' ' + i['last_name']

names(students)

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def studentTeach(dict):

    print 'Students:'
    for i in users['Students']:
        x = str(users['Students'].index(i)+1) + ' ' + i['first_name'] + ' ' + i['last_name']
        print x + ' ' + str(len(x)-3)
    print 'Instructors:'
    for i in users['Instructors']:
        x = str(users['Instructors'].index(i)+1) + ' ' + i['first_name'] + ' ' + i['last_name']
        print x + ' ' + str(len(x)-3)

studentTeach(users)
