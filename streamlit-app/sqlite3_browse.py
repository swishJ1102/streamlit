import sqlite3

# 连接到数据库
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# 查询所有表
# cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
# tables = cursor.fetchall()
# print("Tables:", tables)

# # 查询某个表的数据
# cursor.execute("SELECT * FROM menus;")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)


cursor.execute('''
DELETE FROM menus
WHERE 1=1
''')

# # 提交事务
# conn.commit()


# 插入三条数据到 menu 表
menu_items = [
    ("トップページ", "home"),
    ("任務一覧", "work"),
    ("ファイルアップロード", "upload"),
    ("エビデンスチェック", "compare"),
    ("WBS管理", "wbs"),
    ("ユーザー管理", "user"),
    ("テスト用", "test")
]

# 执行插入操作
cursor.executemany('INSERT INTO menus (name, route) VALUES (?, ?)', menu_items)

# 提交事务
conn.commit()

# 关闭连接
conn.close()
