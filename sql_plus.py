from subprocess import Popen, PIPE

class SQLPlus():
    """ a simple sql plus object model """
    def __init__(self, database, user, password):
        """ initilize sql plus object """
        self.database = database
        self.user = user
        self.password = password
        self._session_ = Popen(
                ['sqlplus', '-S', self.user + "/" + self.password + "@" + self.database],
                stdin=PIPE, stdout=PIPE, stderr=PIPE)
    def run_query(self, query):
        self._session_.stdin.write(query)
        return self._session_.communicate()
