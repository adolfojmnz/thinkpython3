import os

def get_dirlist(path):
    """
    Return a sorted list of aññ entries in path.
    This returns just the names, not the full path to the names.
    """
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist

def print_files(path, prefix = ""):
    """
    Print recursive listing of contents of path.
    """
    if prefix == "":        # detect outer most call, print a heading.
        print(f'Folder listing for: {path}')
        prefix = "|"

    dirlist = get_dirlist(path)
    for f in dirlist:
        print(prefix+f)                     # print the line
        fullname = os.path.join(path, f)    # turn name into a full pathname
        if os.path.isdir(fullname):         # if a directory, recurse.
            print_files(fullname, prefix + "|")
        
print_files("/home/adolfoj/Dev/thinkpython3/")

