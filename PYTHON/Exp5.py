class CustomException(Exception):
    def __init__(self, message = "WASSUP BUDDY"):
        self.message = message
        super().__init__(self.message)

try:
    a=5
    b=0
    if b==0: raise CustomException("Division by 0")
    result = a/b
except CustomException as ce:
    print(f"This is a custom exception: {ce}")
finally:
    print("oh hi there")
