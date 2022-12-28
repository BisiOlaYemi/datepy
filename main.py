from helper import validate_and_execute, user_input_message


user_input = ""
while user_input != "exit":
    user_input = input(user_input_message)
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_dictonary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dictonary)
    print(type(days_and_unit_dictonary))
    validate_and_execute()

"" """"# Datatype in python#
message = "enter some values"   # string#
days = 20  # integer#
price = 9.99  #
valid_number = True # boolean#
exit_input = False  # boolean#
list_of_days = [20, 30, 100]  # list as int#
list_of_months = ["January, February, March"]  # list as string#
set_of_days = [20, 30, 100]  # Data type set which can accept integer#
days_and_unit = {"days": 24, "unit": "hours"}  # dictionary# """
