import pandas as pd
import os
import sys
from pathlib import Path
#--------------------------------------------------------------------------------------

def gpa_checker(total_mark,max,scale):
    return total_mark/max * scale

#--------------------------------------------------------------------------------------
def create_func():
    dict={
        "Name":[],
        "Age":[],
        "Symbol_no":[],
        "Total Marks":[]
    }
    num_of_sub=int(input("Enter the number of subjects u would like to include \n"))
    record_keeping_list=[]
    max_total=num_of_sub*100 
    scale=4

    for i in range(0,num_of_sub):
        sub_name=input("What's the name of ur"+" "+str(i+1)+" "+"subject \n")
        dict[sub_name]=[]
        record_keeping_list.append(sub_name)         # a new list inorder to find the name of subject while iterating. Since it cannot be done through a dict.I needed it to be stored in a seperate list

    

        
    

    num_stud=int(input("How many students would u archieve datas of:\n"))
    print("Its gonna be a lenghty process.But ya , its worth it at the end")
    for i in range(0,num_stud):    # default intake 
        
        stud_name=input("Enter the name of student no"+" "+str(i+1)+"\n")
        stud_id=input("His/Her symbol no\n")
        stud_age=int(input("His/her age \n"))

        dict["Name"].append(stud_name)
        dict["Age"].append(stud_age)
        dict["Symbol_no"].append(stud_id)
        total=0

        for i in range(0,num_of_sub):   #to store the marks of every student in every particular subject
            print("Now, to enter his/her marks in the following subjects")
            mark=int(input("Marks secured in"+" "+record_keeping_list[i]+"\n"))# i cant use the dictionery through indexing, so record_keeping list stores the required info orderly
            dict[record_keeping_list[i]].append(mark)     #here , the record keeping list comes to use. The individual marks is then stored ,respectively.
            total+=mark
        
        dict["Total Marks"].append(total)
    df=pd.DataFrame(dict)

    df["GPA"]=df["Total Marks"].apply(gpa_checker,args=(max_total,scale))  #here , im using gpa conversion pertaining to the total marks system.Well, its rather streamlined than the convulated ones.


    while True:
      file_name=Path(input("Enter a file name\n")+".csv")
      if file_name.exists():
          print("A file with similar name exists")
          retry_choice=retry_function()
          if not retry_choice:
              return
      else:
          break
    df.to_csv(file_name,index=False)    #while storing the df , the default index is individually taken as a seperate column. And to omit that, i used the command index=False
    print(df)                                  #show the user their final output
    for i in range(0,num_of_sub):   #to show individul subject's average assessment
        print("Average marks of students in",record_keeping_list[i],"is",df[record_keeping_list[i]].mean())

    print("Average GPA of students is",df["GPA"].mean()) 

    return


#---------------------------------------------------------------------------------------------------------


def consistent_func(df,symbol_num):
    total=0
    scale=4
    num_of_subject=0
    df.columns=df.columns.astype(str)
    bounce=True
    for column in df.columns:
        if column not in ["Symbol_no","Name","Age","Total Marks","GPA"] and symbol_num is not None:
            if symbol_num is not None:
               total+=int(df[column].loc[symbol_num])
               num_of_subject+=1
            else:
                num_of_subject+=1
                if bounce:
                    df.drop(columns=["Total Marks"],inplace=True)
                    df["Total Marks"]=0
                    bounce=False
                
                df["Total Marks"]+=df[column]
                
    if symbol_num is not None:
        df.loc[symbol_num,"Total Marks"]=total
    
    
    
    max_total_marks=num_of_subject *100
    
    if num_of_subject==0:
        df["GPA"]=0
        

    else:
        df["GPA"]=df["Total Marks"].apply(gpa_checker,args=(max_total_marks,scale))

    return df











#-----------------------------------------------------------------------------------------------------------

def update_func(df,file_path):
    print(df)
    option=int(input("Here r the following options--> Note(u need to specify the exact symbol number of ur student):\n1)Delete an enitre column\n2)Update a specific element\n3)Delete the data of a student\n"))
    if option==1:
        while True:
            col_name=input("Enter a column u would like to drop\n") #advance dropping in the future, i don't hve a clue for now
            if col_name in df.columns:
                df.drop(columns=[col_name],inplace=True)
                print("Succeful", "Your new dataframe is envinced below")
                consistent_func(df=df,symbol_num=None)
                print(df)
                redo_choice=input("Would u like to continue updating file?\nIf yes,type (Y or y), otherwise press (N or n),which will end and save the file\n")
                if redo_choice=='Y' or redo_choice=='y':
                    continue
                else:
                    print("Ending opeation")

                    df.to_csv(file_path)
                    break

            else:
                print("No such column found ")
                redo_choice=input("To rewrite column:Type R or r\nTo go back to update menu:Type U or u\nTo end the program:Type Z or z \n")
                if redo_choice.lower()=='r':
                    pass
                elif redo_choice.lower()=='u':
                    update_func(df,file_path)
                elif redo_choice.lower()=='z':
                    sys.exit()
                else:
                    sys.exit()
    elif option==2:
        while True:
            symbol_num=int(input("Enter the student's symbol number:\n"))
            df.index=df.index.astype(int)    #to ensure int input matches int indexes .U cant trust pandas on datatypes
            if symbol_num in df.index:
                col_name=input("Enter column name\n")
                df.columns=df.columns.astype(str)  #to ensure str input matches column names. U cant trust pandas on dtypes
                if col_name in df.columns:
                    print("This is the current data")
                    print(df.loc[symbol_num,col_name])
                    inp=input("Enter ur new data\n")
                    df[col_name]=df[col_name].astype(str) #same validation like above
                    df.loc[symbol_num,col_name]=inp
                    df=consistent_func(df=df,symbol_num=symbol_num)  #maintaining consistency


                    print("Ur new data is",df.loc[symbol_num,col_name],"\n")
                    print("New dataframe:")
                    print(df)
                    redo_choice=input("Would u like to continue updating your file?\nIf yes,type (Y or y), otherwise press (N or n),which will end and save the file\n")
                    if redo_choice.lower()=='y':
                        continue
                    else:
                       print("Ending opeation")

                       df.to_csv(file_path)
                       break
                else:
                    print("No such column found ")
                    redo_choice=input("To rewrite column name:Type R or r\nTo go back to update menu:Type U or u\nTo end the program:Type Z or z \n")
                    if redo_choice.lower()=='r':
                        pass
                    elif redo_choice.lower()=='u':
                        update_func(df,file_path)
                    elif redo_choice.lower()=='z':
                        sys.exit()
                    else:
                        sys.exit()

            else:
                print("No such symbol number found ")
                redo_choice=input("To rewrite Symbol number:Type R or r\nTo go back to update menu:Type U or u\nTo end the program:Type Z or z \n")
                if redo_choice.lower()=='r':
                    pass
                elif redo_choice.lower()=='u':
                    update_func(df,file_path)
                elif redo_choice.lower()=='z':
                    sys.exit()
                else:
                    sys.exit()
                    
    elif option==3:
        while True:
            symbol_num=int(input("Enter the students symbol numberr\n"))
            df.index=df.index.astype(int)
            if symbol_num in df.index:
                print(df.loc[symbol_num])
                final_verdict=input("Are you sure you want to delete the entire data of this student? Type CONFIRM if u want to proceed\n")
                if final_verdict.lower()=="confirm":
                    df.drop(symbol_num,inplace=True)
                    print("Deleted successfuly")
                    redo_choice=input("Would u like to delete data of more student ,Type Y or y to redo or type N or N to save and end operation?\n")
                    if redo_choice.lower()=='y':
                        continue
                        
                    else:
                        df.to_csv(file_path)
                        break
                    
                else:
                    print("Stoppeed...........")
                    break
            else:
                print("No such symbol number found ")
                redo_choice=input("To rewrite Symbol number:Type R or r\nTo go back to update menu:Type U or u\nTo end the program:Type Z or z \n")
                if redo_choice.lower()=='r':
                     pass
                elif redo_choice.lower()=='u':
                    update_func(df,file_path)
                elif redo_choice.lower()=='z':
                    sys.exit()
                else:
                    sys.exit()


        
#----------------------------------------------------------------------------------------------------------
def access_func(df):
    print("Heres ur current data")
    print(df)
    
    while True:
        sym_num=int(input("Which student's data would u like to access?.Enter his/her symbol number\n"))
        df.index=df.index.astype(int)

        if sym_num in df.index:
            print("\n")
            print("Heres the archived data of this student")
            print(df.loc[sym_num])
            print("\n")
            choice=input("Would u like to re-check another students data then press Y or y\nPress Z or z in order to end the program\n")
            if choice=='Y' or choice=='y':
                pass
            elif choice=='Z' or choice=='z':
                break
            else:
                break
        else:
            print("Sorry, there aint no data with symbol_number:",sym_num)
            retry_choice=retry_function()
            if retry_choice:
                pass
            else:
                break
    return

#-----------------------------

def retry_function():
    retry_choice=input("Would u like to retry ?, Type Y or y to retry\n")
    if retry_choice.lower()=='y':
        return True
    else:
        return False


#------------------------------

    

#---------------------------------------------------------------------------------------------------------

def choice_check():
    print("------------------------------------------------------")
    print("Would u like to create a new excel sheet,or access already pre-existing data.")
    inp=input(" To modify existing records, enter Y \n To create a new record file, enter N.\n To view existing records without making changes, enter A.\n To exit the program, enter Z\n ")
    return inp

#-------------------------------------------------------------------------------------------------------------

    
def main():
    while True:
        choice = choice_check()

        if choice.lower()=='y':
            print("------------------------------------------------------")
            print(
                "Here, You can change, update, add, or delete datas as per ur requirement\n"
                "Make sure the file ur searching is inside the same folder this file is running in "
                "else u might wanna pass the whole path"
            )

            file_path = Path(input("Enter ur file_path \n"))

            if file_path.exists():
                # A function to check if file exists within the OS system.
                # And to make sure it's CSV, I added ".csv".
                print("File Found")

                df = pd.read_csv(file_path, index_col="Symbol_no")
                update_func(df, file_path)

                print("Operation Ended")
                break

            else:
                print("File couldn't be found")

                retry_choice = retry_function()

                if not retry_choice:
                    print("Operation Ended")
                    break

        elif choice.lower()=='n':
            print("------------------------------------------------------")
            create_func()

            print("Operation Ended")
            break

        elif choice.lower() =='a':
            print("------------------------------------------------------")
            file_path = Path(input("Enter the file_path where ur data is stored\n"))
            if file_path.exists():
                print("File Found")

                df = pd.read_csv(file_path, index_col="Symbol_no")
                access_func(df)

                print("Operation Ended")
                break

            else:
                print("File_not found")

                retry_choice = retry_function()

                if not retry_choice:
                    print("Operation Ended")
                    break

        elif choice.lower()=='z':
            print("------------------------------------------------------")
            print("Operation Ended")
            break

        else:
            print("Pls enter a valid choice")


if __name__=="__main__":
    main()
    







