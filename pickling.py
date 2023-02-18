import pickle,random,os
from student import Student

class StudentPickler:

    """This class will generate n of Student clas objects and after performing pickling it will save the into file"""

    def __init__(self,file_name:str, file_mode:str, no_stud:int,):
        self.no = no_stud
        self.file_name = file_name
        self.file_mode = file_mode
        
    def generate_stu_obj(self):
        if os.path.isfile(self.file_name):
            name = 'Krishna'
            stu_objs = [] # blank list to store student objs

            # making n number of objects of Student class
            for i in range(self.no):
                name += str(i)
                age   = random.randint(21,31)
                email = name+'@gmail.com'
                stu = Student(name=name, age=age, email=email)  # making obj
                stu_objs.append(stu) # append stu objs
            
            return stu_objs
        else:
            print("\nInvalid file Name!\nPlease Enter Valid File Name Ok")
              
    def student_pickling(self):
        student_objs = self.generate_stu_obj() # receving stu objs
        exists =  (os.path.isfile(self.file_name))
        
        if exists: # if file is exist
            with open(self.file_name, mode=self.file_mode) as stu_file:
                if stu_file.writable():
                    try:
                        pickle.dump(student_objs, stu_file) # pickling here
                    except:
                        print('\n Some Exception Occurs While Pickling')
                    else:
                        print('Congrats data save successfuly pickle is done')
                else:
                    print('Soorrrry Dont have write permissions')
        else:
            print("\nInvalid file Name!\nPlease Enter Valid File Name Ok")
                
# s1 = StudentPickler(no_stud=1, file_name='folder/students.dat', file_mode='wb')

# s1.student_pickling()
