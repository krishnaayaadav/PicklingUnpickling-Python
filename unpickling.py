import pickle,os
from student import Student

class StudentUnpickler:
    """This class will perform unpickling"""

    def __init__(self, file_name:str, file_mode:str):
        self.file_name  = file_name
        self.file_mode  = file_mode
    
    def unpicklers(self):

        exist = os.path.isfile(self.file_name)
        if exist:

            with open(self.file_name, mode=self.file_mode) as stu:
                
                try:
                    student_objs = pickle.load(stu)
                except:
                    print('Having Exception While Unpickling ')
                else:
                    print('\n Congrats Unpickling done successfuly')
                    return student_objs
        print('Invalid file! Enter Valid file Name  ')

s1 = StudentUnpickler(file_name= 'folder/students.dat', file_mode='rb')
print(s1.unpicklers())