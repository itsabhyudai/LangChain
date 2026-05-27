from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):

    name : str

new_student = {
    "name" : "Abhi"  # if we pass integer here, it will throw error!
}

student = Student(**new_student)

print(student)


#~~~~~~~~~~~~~~~~~~~~~~~~code to set default values~~~~~~~~~~~~~~~~~~~~~

class Student(BaseModel):

    name : str = "Abhi"

new_student = {}

student = Student(**new_student)

print(student.name)


#~~~~~~~~~~~~~~~~~~~~~~~~code to set optional fields~~~~~~~~~~~~~~~~~~~~~

class Student(BaseModel):

    name : str = "Abhi"
    age : Optional[int] = None

new_student = {}  # we can pass | "age" : 22 | here!

student = Student(**new_student)

print(student)


#~~~~~~~~~~code to check built-in validation, example: email~~~~~~~~~~

class Student(BaseModel):

    name : str = "Abhi"
    age : Optional[int] = None
    email : EmailStr

new_student = {"age" : 22, "email" : "abc@email.com"}   #wrong format will throw error   

student = Student(**new_student)

print(student)


#~~~~~~~~~~~~~~~~~~~~~~~~code to set field functions~~~~~~~~~~~~~~~~~~~~~

class Student(BaseModel):

    name : str = "Abhi"
    age : Optional[int] = None
    email : EmailStr
    cgpa : float = Field(gt=0, lt=10)   #0 < cgpa > 10

new_student = {"age" : 22, "email" : "abc@email.com", "cgpa" : 7}   # cgpa > 10 will throw error

student = Student(**new_student)

print(student)



#~~~~~~~~~~~~~~~~different validations in field functions~~~~~~~~~~~~~~~~

class Student(BaseModel):

    name : str = "Abhi"
    age : Optional[int] = None
    email : EmailStr
    cgpa : float = Field(gt=0, lt=10, default=5, description="A decimal value representing the cgpa of the student")

new_student = {"age" : 22, "email" : "abc@email.com"}   

student = Student(**new_student)

print(student)



#~~~~~~~~~~~~~~~~conversion to dict and json~~~~~~~~~~~~~~~~~


class Student(BaseModel):

    name : str = "Abhi"
    age : Optional[int] = None
    email : EmailStr
    cgpa : float = Field(gt=0, lt=10, default=5, description="A decimal value representing the cgpa of the student")

new_student = {"age" : 22, "email" : "abc@email.com"}   

student = Student(**new_student)

student_dict = dict(student)

print(student_dict["age"])   # can fetch any specific thing after making dict


#~~~~~~~~~~~~~~~~~~~making json~~~~~~~~~~~~~~~~~

student_json = student.model_dump_json()
print(student_json)

