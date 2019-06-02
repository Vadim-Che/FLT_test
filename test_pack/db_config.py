from configparser import ConfigParser
 
 
def get_db_config(sets_file, sets_section):
    # Creating settings parser
    _parser = ConfigParser()
    # Reading config file
    _parser.read(sets_file)
 
    # Getting section
    _db_config = {}
    if _parser.has_section(sets_section):
        _params = _parser.items(sets_section)
        for _param in _params:
            _db_config[_param[0]] = _param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(sets_section, sets_file))
 
    return _db_config