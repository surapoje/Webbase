import cx_Oracle
# connection = cx.connect(user="AI_663380040_1", password="sitsak123",
#                                dsn="10.199.36.10/ORCLCDB")
# connStr = 'AI_663380040_1/sitsak123@10.199.36.10:1527/ORCLCDB'
# connection = None
# try:
#     connection = cx.connect("AI_663380297_4/sitsak123@10.199.36.10:1527/ORCLCDB")

#     cur = connection.cursor()
# except Exception as err:
#     print('error while connect to db')
#     print(err)
# finally:
#     if(connection):
#         cur.close()
#         connection.close()
# print('success')
# connection = cx.connect("AI_663380297_4/sitsak123@10.199.36.10:1527/ORCLCDB")
user = 'AI_663380297_4'
password = 'sitsak123'
host = '10.199.36.10'
port = '1527'
sid = 'ORCLCDB'

def selectData(table:str, column = "*", condition = '1=1') -> str:
    """
    what you want just tell me!!
    
    Args:
        table (str): table name like "student"
        column (str, optional): column name like (col1, col2, col3). Defaults is "*"
        condition (str, optional): where condition like stdid = '663380035-4' Defaults is always True
    Returns:
        data or error
    
    SELECT * FROM student WHERE 1=1;
    """
    try:
        con = cx_Oracle.connect(f'{user}/{password}@{host}:{port}/{sid}')
    except cx_Oracle.DatabaseError as er:
        print('There is an error in the Oracle database:' + str(er))
        return
    else:
        try:
            cursor = con.cursor()
            cursor.execute(f"select {column} from {table} where {condition}")
            rows = cursor.fetchall()
            return rows
        except cx_Oracle.DatabaseError as er:
            print('There is an error in the Oracle database:' + str(er))
            return
        except Exception as er:
            print('Error:' + str(er))
            return
        finally:
            if cursor:
                cursor.close()
    finally:
        if con:
            con.close()

def insertData(table:str, primary_key:str, values:str) -> bool:
    """
    Args:
        table (str): table name like "student"
        values (str): insert values like ('663380035-4', 'ธนรัตน์', 'แซ่เฮีย')
    """
    try:
        con = cx_Oracle.connect(f'{user}/{password}@{host}:{port}/{sid}')
        cursor = con.cursor()
        if not check_primary_key(table=table, primary_key=primary_key):
            print(f"Primary key '{primary_key}' already exist.")
            return False
        else:
            cursor.execute(f'insert into {table} values({primary_key}, {values})')
            con.commit()
            print(cursor.rowcount, "row inserted")
            return True
    except cx_Oracle.DatabaseError as e:
        print("There is a problem with Oracle" + str(e))
        return False
    except Exception as er:
        print("Error " + str(er))
        return False
    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()

def check_primary_key(table:str, primary_key:str) -> bool:
    """
    Args:
        table (str): table name like "student".
        primary_key (str): primary key to check.
    Returns:
        bool: return false when primary key already exist.
    """
    allData = selectData(table=table)
    for i in allData:
        if primary_key == str(i[0]):
            return False
    return True

def updateData(table:str, set:str, condition:str) -> bool:
    """
    Args:
        table (str): table name like "student"
        set (str): set values like stdfname = 'oil'
        condition (str): where condition like stdid = '663380035-4'
    Returns:
        bool: return true when everything's okey, if it false you gonna have big problem!
    """
    try:
        con = cx_Oracle.connect(f'{user}/{password}@{host}:{port}/{sid}')
        cursor = con.cursor()
        cursor.execute(f'update {table} set {set} where {condition}')
        con.commit()
        print(cursor.rowcount, "row updated")
        return True
    except cx_Oracle.DatabaseError as e:
        print("There is a problem with Oracle" + str(e))
        return False
    except Exception as er:
        print("Error " + str(er))
        return False
    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()

def deleteData(table:str, condition:str) -> bool:
    """
    Args:
        table (str): table name like "student"
        condition (str): where condition like stdid = "663380035-4"
    Returns:
        bool: return true when everything's okey, if it false you gonna have big problem!
    """
    try:
        con = cx_Oracle.connect(f'{user}/{password}@{host}:{port}/{sid}')
        cursor = con.cursor()
        cursor.execute(f'delete from {table} where {condition}')
        con.commit()
        print(cursor.rowcount, "row deleted")
        return True
    except cx_Oracle.DatabaseError as e:
        print("There is a problem with Oracle" + str(e))
        return False
    except Exception as er:
        print("Error " + str(er))
        return False
    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()

