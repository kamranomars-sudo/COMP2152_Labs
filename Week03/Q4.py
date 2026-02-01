monday_class ={"Alice", "Bob", "Charlie", "Diana"}
wednesday_class ={ "Bob","Diana","Eve","Frank"}
monday_class.add("Grace")
print(f"Monday Class: {monday_class}")
print(f"Wednesday Class: {wednesday_class}")
print(f"Both classes: {monday_class & wednesday_class}") #Shift+7
print (f"Attended Either classes: {monday_class | wednesday_class}")
print(f"Only Monday: {monday_class - wednesday_class}")
print(f"Only one class: {monday_class ^ wednesday_class}")
all_students = monday_class | wednesday_class
print(f"Is monday subset of all students: ", monday_class <= all_students)