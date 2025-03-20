def is_weekeend(day):
    match day:
        case "Thursday" | "Friday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Saturday" | "Sunday":
            return False
        case _:
            return "Error"
        

print(is_weekeend("Sunday"))  