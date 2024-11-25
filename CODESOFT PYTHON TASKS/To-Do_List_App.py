Tasks=[]
Unique_tasks=set()
task_status={}
def Add_Tasks(task):
    Tasks.append(task)
    Unique_tasks.add(task)
    task_status[task]="Incomplete"

def Edit_task(old_task,new_task):
    Tasks[Tasks.index(old_task)]=new_task
    Unique_tasks.add(new_task)
    task_status[new_task]=task_status.pop(old_task)

def Del_task(task):
    Tasks.remove(task)
    Unique_tasks.remove(task)
    del task_status[task]

while (1):
        print("")
        print("  *********************")
        print("      1.ADD TASK")
        print("      2.EDIT TASK")
        print("      3.DELETE TASK")
        print("      4.VIEW TASKS")
        print("      5.EXIT")
        print("  *********************")
        print("")
        choice=int(input("Enter your choice: "))
        if choice==1:
            task=input("Enter your task to add: ")
            Add_Tasks(task)
        elif choice==2:
            old_task=input("Enter the task to edit: ")
            new_task=input("Enter the new task : ")
            if old_task in Tasks:
                Edit_task(old_task,new_task)
            else:
                print("Invalid Task!!1")
            
        elif choice==3:
            task=input("Enter the task you want to delete: ")
            if task in Tasks:
                 Del_task(task)
            else:
                print("""Invlid task !! 
                      Task Not Available in Your List""")
           
        elif choice==4:
            print(Tasks)
            for task in Tasks:
                print(f"{task}-{task_status[task]}")
        elif choice==5:
            break
        else:
            print("""Invalid Choice!!
                  Please Try again!!""")
