from configparser import ConfigParser

def config(filename = "E:\PFCsystem2\PFCsystem\database.ini", section="postgresql"):
    #create parser
    parser = ConfigParser()
    #read config file
    parser.read(filename)
    db = {}
    if parser.has_section(section):

        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
        
    else:
        raise Exception('Section {0} is not found in the {1} file.'.format(section, filename))
    return db



    