import sys

name = input("Enter Your Name:  " )
FName = input("Enter Your Father Name : ")
Ads = input("Enter Your Adress: ")
Con = input("Enter Your Contact: ")
Email = input("Enter Your Email: ")



data = {
     "Name" : name , 
     "Father-Name" : FName , 
     "adresss" : Ads , 
     "Contact" : Con ,
     "E-mail" : Email 

}


print("\n---Your Data---")
# for key,value in data.items():
#     print(f" { key} : {value}")
#     print(f"length (len) : { len(value) } characters")
#     print(f" Memory Size (sys.getsizeoof) : {sys.getsizeof(value)} bytes ")
for key ,value in data.items():
    print(f"{key} {value}")
    print(f"LENGTH {len(value)} Characters")
    print(f"MEmory Size {sys.getsizeof(value)} bytes")

