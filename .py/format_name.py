def format_name(f_name, l_name):
    """Take a first and last name and format it to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "You didn\'t provide valid inputs." # 提早結束
    f_name = f_name.title()
    l_name = l_name.title()
    formatname = f_name+ " " + l_name
    return formatname
    # 或是 
    # return f"{f_name} {l_name}"

firstname = input("What\'s the first name?\n ")
lastname = input("What\'s the last name?\n ")

print(format_name(f_name = firstname, l_name = lastname))


