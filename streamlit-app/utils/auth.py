import streamlit_authenticator as stauth
from db.db_handler import get_users

def get_authenticator():
    # 从数据库获取用户信息
    users = get_users()

    # 构建用户名、姓名和加密密码列表
    usernames = [user["username"] for user in users]
    names = [user["name"] for user in users]
    hashed_passwords = [user["password"] for user in users]

    # 创建 Authenticator 实例
    authenticator = stauth.Authenticate(
        credentials={"usernames": {usernames[i]: {"name": names[i], "password": hashed_passwords[i]} for i in range(len(users))}},
        cookie_name="streamlit_auth",
        key="auth",
        cookie_expiry_days=1,
    )

    # 登录验证
    name, authentication_status, username = authenticator.login("登录", "main")
    return authenticator, name, authentication_status, username