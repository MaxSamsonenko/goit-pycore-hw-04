
def add_contact(args, contacts):
    if len(args) <= 1:
        return "Not enough arguments, expecting name and phone"
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    if len(args) <= 1:
        return "Not enough arguments, expecting name and new phone number"
    name, phone = args
    contacts[name] = phone
    return f"Phone number for {name} has been changed."
   

def show_phone(args, contacts):
    name = args[0]
    return f"{name}'s phone is {contacts[name]}"

    
    
