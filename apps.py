from student import Student             # student class normal
from pickling import StudentPickler     # studentPickler class to make pickling of student obj
from unpickling import StudentUnpickler # StudentUnpickler for unpickling

pickler  = StudentPickler(file_name='folder/students.dat', file_mode='ab+', no_stud=5)

unpickler = StudentUnpickler(file_name='folder/students.dat',file_mode='rb')


student = (unpickler.unpicklers())

for stu in student:
    print(stu.detail())
    print(f'Name: {stu.name} Age: {stu.age}  Email: {stu.email}')
