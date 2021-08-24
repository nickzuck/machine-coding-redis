class Database():
    def __init__(self):
        # TODO: Create connection over here
        pass

    def save(self, table_name, **values):
        # TODO: Implement save for given values
        pass

    def update(self, table_name, values : dict):
        # TODO : Implement update here based on old and new values
        # values dict will contain the values like {"old_<field1>" : "value1", "new_<field2>" : "value2"}
        # The query corresponding to this will be
        # update table_name set new_<field2>  = "value2" where old_<field1> = "value1"
        pass

    def delete(self, table_name, **values):
        # TODO : Implement delete here
        pass

    def get(self, table_name, **values):
        # TODO : Implement get here
        pass