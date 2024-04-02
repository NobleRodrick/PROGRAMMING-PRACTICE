def main():
    student = get_student()
    if student["name"] == "padma":
        student["house"] = "Ravenclaw"
    print(f"{student["name"]} from {student["house"]}")

def get_student():
   name = input("name: ")
   house = input("house: ")
   return{
       "name": name,
       "house": house
   }

if __name__ == "__main__":
    main()