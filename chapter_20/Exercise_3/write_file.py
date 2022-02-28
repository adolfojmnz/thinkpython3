def write_file(filename, write_list):
    ''' 
        Writes the strings in the list to the file
        erasing all existent content. 
    '''
    open(filename, 'w').write('')

    for string in write_list:
            open(filename, 'a').write(string)
