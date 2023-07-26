def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    previous_meal = None
    for meal in meals:
        if meal == previous_meal:
            return True
        previous_meal = meal
    return False

# def menu_is_boring(meals):
#     # Iterate over all indices of the list, except the last one
#     for i in range(len(meals)-1):
#         if meals[i] == meals[i+1]:
#             return True
#     return False