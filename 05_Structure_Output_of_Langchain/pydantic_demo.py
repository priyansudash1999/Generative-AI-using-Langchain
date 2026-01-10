from pydantic import BaseModel, Field, EmailStr
from typing import Optional


class Student(BaseModel):
  name: str
  age: Optional[int] = None

new_student = {"name": "Priyansu",  "age": 27}

# new_student = {"name": 23}

student = Student(**new_student)

# print(student)








# Pydantic with field constraints
class Score(BaseModel):
    value: float = Field(ge=0)

res= Score(value=0)
ress = Score(value=0.5)
# resss = Score(value=-2)  --> Gives compile time error

print(res, ress)
# print(resss)

# greater or lesser both

class Scores(BaseModel):
   value: float = Field(ge=0, le=1)

result = Scores(value = 0.8)
resultt = Scores(value=1)

print(result, resultt)



class Students(BaseModel):
  name: str
  age: Optional[int] = None
  email: EmailStr

new_studnt = {"name": "Priyansu",  "age": 27, "email": "abc@gmail.com"}

# new_student = {"name": 23}

students = Students(**new_studnt)