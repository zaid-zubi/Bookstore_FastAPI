from pydantic import BaseModel,EmailStr,validator

class UserIn(BaseModel):
	username: str
	email: str
	password: str
	phone_first: str
	address: str
	birth_date: str
	gender: str
 
 
	@validator('username')
	def validate_username(cls,v: str):

		if v.isupper() or v.islower() or v.isnumeric() or v.isdigit():
			return ValueError("Username Error!")
		if " " in v:
			return ValueError('Wrong! Space in username')
		if len(v) < 8:
			return ValueError('Wrong! username length must be greater than 8 and has uppercase letter')
		return v
	@validator('email')
	def validate_email(cls, v:EmailStr):
		if v.isupper() or v.isdigit():
			return ValueError("Email Error!")
		return v

	@validator('password')
	def validate_password(cls,v: str):
		count_num = 0
		count_upper = 0
		for letter in v:
			if letter.isnumeric():
				count_num = count_num + 1
			if letter.isupper():
				count_upper = count_upper + 1
		if len(v) < 8  and count_num == 0 and count_upper < 1:
			if v.isupper() and v.islower() and v.isdigit():
				return ValueError("Password is invalid")
		return v
	@validator('phone_first')
	def validate_phone_first(cls,v: str):
		if len(v) != 10:
			return ValueError("Invalid Phone Number")
		if ("078" in v or "077" in v or "079" in v )and len(v) == 10:
			return v
		return ValueError("Invalid Phone Number")


class Login(BaseModel):
	email: str
	password: str
	@validator('email')
	def validate_email(cls, v:EmailStr):
		if v.isupper() or v.isdigit():
			return ValueError("Email Error!")
		return v
	
	@validator('password')
	def validate_password(cls,v: str):
		count_num = 0
		count_upper = 0
		for letter in v:
			if letter.isnumeric():
				count_num = count_num + 1
			if letter.isupper():
				count_upper = count_upper + 1
		if len(v) < 8  and count_num == 0 and count_upper < 1:
			if v.isupper() and v.islower() and v.isdigit():
				return ValueError("Password is invalid")
		return v
