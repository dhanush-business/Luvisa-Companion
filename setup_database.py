import sqlite3

def setup():
    """Creates a clean database without the theme_color column."""
    conn = sqlite3.connect('aura.db')
    cursor = conn.cursor()
    
    # Drop old tables to ensure a fresh start
    cursor.execute("DROP TABLE IF EXISTS profiles")
    cursor.execute("DROP TABLE IF EXISTS users")
    cursor.execute("DROP TABLE IF EXISTS chat_history")
    
    # Create the users table (unchanged)
    cursor.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL
    )
    ''')
    
    # Create the new profiles table WITHOUT theme_color
    cursor.execute('''
    CREATE TABLE profiles (
        user_id INTEGER PRIMARY KEY,
        display_name TEXT DEFAULT 'User',
        avatar_path TEXT DEFAULT 'avatars/default_avatar.png',
        status_message TEXT DEFAULT 'Hey there! I’m using Luvisa 💗',
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    ''')
    
    # Re-create chat_history table (unchanged)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS chat_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        sender TEXT,
        message TEXT,
        timestamp TEXT,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    ''')
    
    conn.commit()
    conn.close()
    print("✅ Database has been reset and configured successfully without theme color.")

if __name__ == '__main__':
    setup()