import csv
import pandas as pd


class Student():

    def write_in_file(self):
        count=int(input("Enter number of students: "))
        with open("student_list.csv", "w",newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['name','mark'])
            for i in range(count):
                name = input("Enter student name: ")
                mark = int(input("Enter student mark: "))
                writer.writerow([name, mark])
        print("data are store sucessfully")
        print("---------------------------------------")


    def funtion_student(self):
        data = pd.read_csv("student_list.csv")
        topper = data.loc[data['mark'].idxmax()]
        avg_mark = data['mark'].mean()
        print(f"The highest mark of {topper['name']} is: {topper['mark']}")
        print(f"The average mark of studnets is: {avg_mark}")

    def pass_percentage(self):
         data = pd.read_csv("student_list.csv")
         for _, row in data.iterrows():
             name=row['name']
             mark=row['mark']
             if mark<50:
                print(f"\n{name} have to improve : {mark}")
             elif mark<80:
               print(f"\n{name} try your best  : { mark}")
             elif mark<90:
               print(f"\n{name} good work : {mark}")
             elif mark<=100:
                 print(f"\n{name} toopers : {mark}")


manager=Student()
manager.write_in_file()

manager.funtion_student()
manager.pass_percentage()




