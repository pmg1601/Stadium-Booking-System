# This file is a module which actually deals with all dataBase related operations


import mysql.connector as sql

# --------------------------------------------------------------------------------------------------------

# CONNECTION ESTABLISHMENT

database = sql.connect(
    host = 'localhost',
    user = 'aspirine',
    password = 'aspirine@mysql',
    auth_plugin='mysql_native_password')

cur = database.cursor()

cur.execute("USE Stadium")

# --------------------------------------------------------------------------------------------------------

def book_ticket(show, email, date, attendees, tier):
    """
        Add book entry in `Book` database and also reflect the transaction in `Transactions` DataBase
    """

    cmd = "SELECT price FROM Stadiums WHERE name = %s AND tier = %s"
    cur.execute(cmd, (show, tier))

    price = cur.fetchall()[0][0] * int(attendees)

    cmd = """
        INSERT INTO Book(show_name, email, event_date, attendees, tier, price)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    val = (show, email, date, attendees, tier, price)
    cur.execute(cmd, val)
    database.commit()

    last_id = cur.lastrowid

    transactions(last_id, email, 0, show, tier, date, price)            # Update Transactions table
    if update_stadiums(show, tier, -int(attendees))  == 1:                        # Update Stadiums info i.e. seats remaining
        return last_id, price                                               # Return Ticket ID and total price for ticket generation
    else:
        return 0,0
# --------------------------------------------------------------------------------------------------------

def cancel_ticket(tid):
    """ This function modifies respective databases after a ticket cancellation """

    cmd = f"SELECT show_name, tier, price FROM Book WHERE tid={tid}"
    cur.execute(cmd)
    x = cur.fetchall()[0]

    cmd = f"SELECT email, event_date, attendees FROM Book WHERE tid={tid}"
    cur.execute(cmd)
    email, date, attendees = cur.fetchall()[0]

    cmd = f"DELETE FROM Book where tid = {tid}"                 # Delete ticket from Book database

    cur.execute(cmd)
    database.commit()

    transactions(tid, email, 1, x[0], x[1], date, x[2])         # Update Transactions table
    if update_stadiums(x[0], x[1], attendees):                      # Update Stadiums info i.e. seats remaining
        return x                                                    # Return necessary information for Cancellation report
    else:
        return 0,0,0
# --------------------------------------------------------------------------------------------------------

def transactions(tid, email, refund, show, tier, date, amount):
    """ This function updates Transactions database """

    cmd = """
        INSERT INTO Transactions
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    val = (tid, email, refund, show, tier, date, amount)

    cur.execute(cmd, val)
    database.commit()

# --------------------------------------------------------------------------------------------------------

def update_stadiums(show, tier, val):
    """ Update Seat Count after booking or cancellation """

    x = get_curr_seats(show, tier)[0]
    y = get_def_seats(show, tier)[0]

    cmd = """
        UPDATE Stadiums
        SET seats = %s+%s
        WHERE name = %s AND tier = %s
    """

    if x+val >= 0 and x+val <= y:
        cur.execute(cmd, (x, val, show, tier))
        database.commit()
        return 1
    else:
        return 0

# --------------------------------------------------------------------------------------------------------

def get_curr_seats(show, tier):
    """ Return current number of seats """

    cmd = "SELECT seats from stadiums WHERE name = %s AND tier = %s"
    val = (show, tier)
    cur.execute(cmd, val)

    return cur.fetchall()[0]

# --------------------------------------------------------------------------------------------------------

def get_def_seats(show, tier):
    """ Return default number of seats """

    cmd = "SELECT def_no from stadiums WHERE name = %s AND tier = %s"
    val = (show, tier)
    cur.execute(cmd, val)

    return cur.fetchall()[0]

# --------------------------------------------------------------------------------------------------------

def get_seats(show):
    """ Return number of remaining seats and their prices for context for prior bookig information """

    tiers = ['Upper', 'Lower', 'Terrace', 'Hospitality', 'Ground']

    x = []
    y = []

    for tier in tiers:
        cmd = "SELECT price FROM Stadiums WHERE name=%s AND tier=%s"
        val = (show, tier)
        cur.execute(cmd, val)
        x.append(cur.fetchall()[:])
    
    for tier in tiers:
        cmd = "SELECT seats FROM Stadiums WHERE name=%s AND tier=%s"
        val = (show, tier)
        cur.execute(cmd, val)
        y.append(cur.fetchall()[:])

    return x,y

# --------------------------------------------------------------------------------------------------------
