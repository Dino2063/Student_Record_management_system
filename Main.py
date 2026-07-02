import pandas as pd
import os
import sys

#--------------------------------------------------------------------------------------

def gpa_checker(total_mark,max,scale):
    return total_mark/max * scale

#--------------------------------------------------------------------------------------
def create_func():
    dict={
        "Name":[],
        "Age":[],
        "Symbol_no":[]
    }
    num_of_sub=int(input("Enter the number of subjects u would like to include \n"))
    record_keeping_list=[]
    max_total=num_of_sub*100  #future
    scale=4

    for i in range(0,num_of_sub):
        sub_name=input("What's the name of ur"+" "+str(i+1)+" "+"subject \n")
        dict[sub_name]=[]
        record_keeping_list.append(sub_name)         # a new list inorder to find the name of subject while iterating. Since it cannot be done through a dict.I needed it to be stored in a seperate list

    dict["Total Marks"]=[]
    

        
    

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
            mark=int(input("Marks secured in"+" "+record_keeping_list[i]+"\n"))
            dict[record_keeping_list[i]].append(mark)     #here , the record keeping list comes to use. The individual marks is then stored ,respectively.
            total+=mark
        
        dict["Total Marks"].append(total)
    df=pd.DataFrame(dict)

    df["GPA"]=df["Total Marks"].apply(gpa_checker,args=(max_total,scale))  #here , im using gpa conversion pertaining to the total marks system.Well, its rather streamlined than the convulated ones.


    file_name=input("Enter a file name \n")
    df.to_csv(file_name+".csv",index=False)    #while storing the df , the default index is individually taken as a seperate column. And to omit that, i used the command index=False
    print(df)                                  #show the user their final output
    for i in range(0,num_of_sub):   #to show individul subject's average assessment
        print("Average marks of students in",record_keeping_list[i],"is",df[record_keeping_list[i]].mean())

    print("Average GPA of students is",df["GPA"].mean()) 

    return


#---------------------------------------------------------------------------------------------------------

def update_func(df,file_name):
    print(df)
    option=int(input("Here r the following options--> Note(u need to specify the exact symbol number of ur student):\n1)Delete an enitre column\n2)Update a specific element\n"))
    if option==1:
        while True:
            col_name=input("Enter a column u would like to drop\n") #advance dropping in the future, i don't hve a clue for now
            if col_name in df.columns:
                df=df.drop(columns=[col_name])
                print("Succeful", "Your new dataframe is envinced below")
                print(df)
                redo_choice=input("Would u like to continue updating file?\nIf yes,type (Y or y), otherwise press (N or n),which will end and save the file\n")
                if redo_choice=='Y' or redo_choice=='y':
                    update_func(df,file_name)
                else:
                    print("Ending opeation")

                    df.to_csv(file_name+".csv")
                    break

            else:
                print("No such column found ")
                redo_choice=input("To rewrite column:Type R or r\nTo go back to update menu:Type U or u\nTo end the program:Type Z or z \n")
                if redo_choice=='R' or redo_choice=='r':
                    pass
                elif redo_choice=='U' or redo_choice=='u':
                    update_func(df)
                elif redo_choice=='Z' or redo_choice=='z':
                    sys.exit()
                else:
                    sys.exit()
    elif option==2:
        while True:
            symbol_num=int(input("Enter the student's symbol number:\n"))
            df.index=df.index.astype(int)    #to ensure int input matches int indexes .U cant trust pandas on datatypes
            if symbol_num in df.index:
                col_name=input("Enter column name\n")
                if col_name in df.columns:
                    print("This is the current data")
                    print(df.loc[symbol_num,col_name])
                    inp=input("Enter ur new data\n")
                    if df[col_name].dtype=="int64":
                        df.loc[symbol_num,col_name]=int(inp)
                    
                        
                    elif df[col_name].dtype=="float64":
                        df.loc[symbol_num,col_name]=float(inp)
                    else:
                        df.loc[symbol_num,col_name]=inp


                    print("Ur new data is",df.loc[symbol_num,col_name],"\n")
                    print("New dataframe:")
                    print(df)
                    redo_choice=input("Would u like to continue updating your file?\nIf yes,type (Y or y), otherwise press (N or n),which will end and save the file\n")
                    if redo_choice=='Y' or redo_choice=='y':
                        update_func(df,file_name)
                    else:
                       print("Ending opeation")

                       df.to_csv(file_name+".csv")
                       break
                else:
                    print("No such column found ")
                    redo_choice=input("To rewrite column name:Type R or r\nTo go back to update menu:Type U or u\nTo end the program:Type Z or z \n")
                    if redo_choice=='R' or redo_choice=='r':
                        pass
                    elif redo_choice=='U' or redo_choice=='u':
                        update_func(df)
                    elif redo_choice=='Z' or redo_choice=='z':
                        sys.exit()
                    else:
                        sys.exit()

            else:
                print("No such symbol number found ")
                redo_choice=input("To rewrite Symbol number:Type R or r\nTo go back to update menu:Type U or u\nTo end the program:Type Z or z \n")
                if redo_choice=='R' or redo_choice=='r':
                    pass
                elif redo_choice=='U' or redo_choice=='u':
                    update_func(df,file_name)
                elif redo_choice=='Z' or redo_choice=='z':
                    sys.exit()
                else:
                    sys.exit()


        
#----------------------------------------------------------------------------------------------------------
def access_func(file_name,df):
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
            choice=input("Would u like to re-write the symbol number.If so, Enter Y or y.\nIf u want to end the operation press Z or z")
            if choice=='Y' or choice=='y':
                pass
            else:
                break
    return

            





    

#---------------------------------------------------------------------------------------------------------

def checkk():
    print("Would u like to create a new excel sheet,or access already pre-existing data.")
    inp=input("To access and ammend old data, type Y or y, and to create a new data press N or n. Lastly to only access data ,type A or a\nTo end the program press Z or z \n")

    return inp

#-------------------------------------------------------------------------------------------------------------
while True:
    choice=checkk()
    if choice=='Y'or choice=='y':
        print("Here , You can change ,update, add, or delete datas as per ur requirement")
    
        file_name=input("Enter ur excel's file name where ur data is archived \n")
        if os.path.exists(file_name+".csv"):   #a function to check if file exists within the os system. And to make sure its csv, i added ".csv". Last time, i found an error when i didn't incorporate ".csv" inside the function; it rather grabbed a txt file with similar name.
            print("File Found")
            df=pd.read_csv(file_name+".csv",index_col="Symbol_no")
            update_func(df,file_name)
            print("Operation Ended")
            break
        else:
            print("File couldn't be found")
    elif choice=='N'or choice=='n':
        create_func()
        print("Operation Ended")
        break
    elif choice=='A' or choice=='a':
        file_name=input("Enter the name of excel file where ur students' datas are stored\n")
        if os.path.exists(file_name+".csv"):
            print("File Found")
            df=pd.read_csv(file_name+".csv",index_col="Symbol_no")
            access_func(file_name,df)
            print("Operation Ended")
            break
        else:
            print("File_not found")
    elif choice=='Z' or choice=='z':

        print("Operation Ended")
        break
    else:
        print("Pls enter a valid choice")


    
    
    

    







