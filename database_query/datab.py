import aiosqlite


async def get_all_user_id():
    connect = await aiosqlite.connect('database_bot.db')
    cursor = await connect.cursor()
    users_id = await cursor.execute('SELECT user_id FROM users')
    users_id = await users_id.fetchall()
    users_id = [i[0] for i in users_id]
    await cursor.close()
    await connect.close()
    return users_id


async def get_user_count():
    connect = await aiosqlite.connect('database_bot.db')
    cursor = await connect.cursor()
    user_count = await cursor.execute('SELECT COUNT(*) FROM users')
    user_count = await user_count.fetchone()
    await cursor.close()
    await connect.close()
    return user_count[0]
    

async def add_user(user_id, full_name, username):
    connect = await aiosqlite.connect('database_bot.db')
    cursor = await connect.cursor()
    check_user = await cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    check_user = await check_user.fetchone()
    
    if check_user is None:
        await cursor.execute('INSERT INTO users (user_id, full_name, username) VALUES (?, ?, ?)', (user_id, full_name, username))
        await connect.commit()
        
    await cursor.close()
    await connect.close() 