def read_token(FILENAME):
    '''this function receives a filename to read A contains an API key'''

    MODE = "r"
    with open(FILENAME, MODE) as fp:
        lines = fp.readline()
        return lines

def write_plain_text_file(FILENAME, DATA):
    with open(FILENAME,"w") as fp:
        fp.write(DATA)

def read_plain_text_file(FILENAME):
    '''this function receives a plain text file and returns the contents'''

    with open(FILENAME, "r") as fp:
        r = fp.readlines()
        return r
    