from db_connection import get_db

def get_messages():
    connection = get_db()
    cur = connection.cursor()
    sql = """SELECT users.username, messages.message 
             FROM messages 
             INNER JOIN users ON messages.user_id = users.id"""
    result = cur.execute(sql)
    messages = result.fetchall()
    return messages

def send_message(sender_id, message):
    connection = get_db()
    cur = connection.cursor()
    try:
        sql = """INSERT INTO messages (user_id, message)
                VALUES (?, ?)"""
        cur.execute(
            sql, [sender_id, message])
        connection.commit()
    except:
        return False
    return True

def delete_message(message_id):
    connection = get_db()
    cur = connection.cursor()
    sql = "DELETE FROM messages WHERE id=?"
    cur.execute(sql, [message_id])
    connection.commit()
    return True
