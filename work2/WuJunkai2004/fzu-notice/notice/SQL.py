import sqlite3

debug   = False
defined = [':memory:', 'debug.db'][debug]


def _unsupport(*args, **kwargs):
    raise RuntimeError('不支持此方法')


class CONLUMN(list):
    append = _unsupport
    clear  = _unsupport
    extend = _unsupport
    pop    = _unsupport
    remove = _unsupport
    reverse= _unsupport
    sort   = _unsupport
    def __init__(self, cursor, table, conlumn):
        self.cursor = cursor
        self.table  = table
        self.name   = conlumn
        list.__init__(self)

        self.cursor.execute("SELECT {} FROM {}".format( self.name, self.table))
        for i in [item[0] for item in self.cursor.fetchall()] :
            list.append(self, i)

    def __setitem__(self, __id, __value):
        self.insert(__id, __value)
        list.insert(self, __id-1, __value)

    def __getitem__(self, __id):
        if(__id == 0):
            raise RuntimeError("下标错误")
        if(__id<0):
            return list.__getitem__(self, __id)
        return list.__getitem__(self, __id-1)

    def update(self, __id, __value):
        self.insert(__id, __value)
        list.insert(self, __id-1, __value)

    def insert(self, __id, __value):
        self.cursor.execute('UPDATE {} set "{}"="{}" WHERE oid={}'.format(self.table, self.name, __value, __id))
        list.insert(self, __id-1, __value)

    def index(self, __value, __start = 0, __stop = 0x7fffffffffffffff):
        return list.index(self, __value, __start, __stop) + 1


class TABLE:
    def __init__(self, cursor, table) -> None:
        self.cursor = cursor
        self.name   = table

    def __getitem__(self, __name):
        return CONLUMN(self.cursor, self.name, __name)

    def create(self, __conlumns):
        if(type(__conlumns)!=list and type(__conlumns)!=tuple):
            __conlumns = [__conlumns]
        self.cursor.execute( 'CREATE TABLE {}\n({});'.format(self.name, ',\n'.join(['"{}" TEXT'.format(item) for item in __conlumns]) ) )

    def insert(self, __value) -> None:
        if(type(__value)!=list and type(__value)!=tuple):
            __value = [__value]
        self.cursor.execute("INSERT INTO {} VALUES({})".format(self.name, ",".join(['"{}"'.format(item) for item in __value]) ) )



class SQL:
    def __init__(self, file = defined) -> None: 
        self.connect = sqlite3.connect(file)
        self.cursor  = self.connect.cursor()

    def __setitem__(self, __name, __value) -> None:
        if(type(__value)!=list and type(__value)!=tuple):
            __value = [__value]
        try:
            self.cursor.execute( 'CREATE TABLE {}\n({});'.format(__name, ',\n'.join(['{} TEXT'.format(item) for item in __value]) ) )
        except sqlite3.OperationalError:
            pass

    def __getitem__(self, __name) -> TABLE:
        return TABLE(self.cursor, __name)
        
    def __del__(self) -> None:
        self.connect.commit()
        self.cursor .close()
        self.connect.close()

    def commit(self):
        self.connect.commit()


def _shell():
    while(True):
        cmmd = ''
        line = input('>>>').rstrip()
        cmmd += line
        while(line and (line[0] == ' ' or line[-1] == ':')):
            line = input('...').rstrip()
            cmmd += '\n' + line
        try:
            result = eval(cmmd)
        except Exception as e1:
            try:
                exec(cmmd)
            except Exception as e2:
                print("ERROR ! : {}".format(e2))
        else:
            print(result)


if(__name__ == "__main__"):
    _shell()
