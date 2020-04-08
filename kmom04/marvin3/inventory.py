"""
This document contains the code of the different functions used in inventory management.
"""

filename = "inv.data"

def readfile():
    """
    Reads the inventory list.
    """
    with open(filename) as filehandle:
        content = filehandle.read()
    return content

def write_to_file(content, mode="a"):
    """
    Write to file.
    """
    with open(filename, mode) as filehandle:
        filehandle.write(content)

def remove_item(remove):
    """
    Removes item from list.
    """
    content = readfile()
    if remove in content:
        if content.index(remove) == 0:
            modified_content = content.replace(remove, "")
        else:
            modified_content = content.replace("\n" + remove, "")
        write_to_file(modified_content.strip(), "w")
        return content

def remove_content(mode="w"):
    """
    This function will delete the whole inventory.
    """
    item = ""
    result = ""
    result += item + "\n"
    write_to_file(result.strip(), mode)

def add(content):
    """
    Adds content to inventory.
    """
    if readfile() == "":
        write_to_file(content, "a")
    else:
        write_to_file("\n" + content, "a")
    return content
