import Vaccination
def main_function():
    print("******CRUD******")
    print("1--->Public")
    print("2--->Admin")
    
    try:
        user=int(input("Enter a number:"))
        if user==1:
            print("1---insert data")
            user=int(input("Enter a number:"))
            if user==1:
                Vaccination.insert_data()
            else:
                print("***Pls check your number...***")
        elif user==2:
            print("1--->insert data")
            print("2--->view data")
            print("3--->update data")
            print("4--->delete data")
            user=int(input("Enter a number:"))
            if user==1:
                Vaccination.insert_data()
            elif user==2:
                Vaccination.view_data()
            elif user==3:
                Vaccination.update_data()
            elif user==4:
                Vaccination.delete_data()
            else:
                print("***Pls check your number...***")
        else:
            print("***Pls check your number...***")
    except:
        print("pls type number only")
main_function()