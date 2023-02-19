import sqlite3


def connect():
    conn = sqlite3.connect('cigar_shop.db')
    cur = conn.cursor()
    return conn, cur


def insert_into_cigars(cigar_name:str, size:str, price:float) -> int:
    try:
        conn, cur = connect()
        sql = '''INSERT INTO cigars(brand,size,cost) VALUES (?,?,?)'''
        val = (cigar_name, size, price)
        cur.execute(sql, val)
        conn.commit()
        conn.close()

        return cur.lastrowid
    except sqlite3.Error as er:
        print(er)


def query_cigars(id:int=None, brand:str=None, size:str=None) -> list:
    
    try:
        conn, cur = connect()
        if id == None and brand == None and size == None:

            sql = '''SELECT * FROM cigars'''
            result = cur.execute(sql)
        elif id is not None:
            result = cur.execute('SELECT * FROM cigars WHERE id=?', (id,))
        elif brand is not None and size is not None:
            result = cur.execute(
                'SELECT * FROM cigars WHERE brand=? and size=?', (brand, size))
        elif brand is not None:
            result = cur.execute(
                'SELECT * FROM cigars WHERE brand=?', (brand,))
        else:
            result = cur.execute('SELECT * FROM cigars WHERE size=?', (size,))

        return result.fetchall()
    except sqlite3.Error as er:
        print(er)


print(query_cigars(brand='My Father'))
print(query_cigars(brand='My Father', size="Toro"))
print(query_cigars(size='Toro'))
