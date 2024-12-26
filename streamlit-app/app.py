import streamlit as st
from streamlit_option_menu import option_menu
from utils.auth import get_authenticator
from utils.menu_loader import load_menus, render_page
from db.db_handler import init_db

# 初始化数据库
init_db()

# Streamlit 应用配置
st.set_page_config(page_title="Dynamic Menu with Auth", layout="wide")

# 获取 Authenticator 实例
authenticator, name, authentication_status, username = get_authenticator()

if authentication_status:
    # 显示登录状态
    st.sidebar.success(f"欢迎，{name} 👋")

    # 动态加载菜单
    menus = load_menus()

    # 使用 OptionMenu 创建侧边栏导航
    with st.sidebar:
        selected_menu = option_menu(
            "导航",  # 菜单标题
            [menu["name"] for menu in menus],  # 菜单名称列表
            icons=["house", "cloud-upload", "door-closed"],  # 可自定义图标
            menu_icon="cast",  # 菜单图标
            default_index=0,  # 默认选中第一个菜单
        )

    # 根据选中菜单渲染页面
    render_page(selected_menu, menus, authenticator)
elif authentication_status == False:
    st.error("用户名或密码错误，请重试！")
else:
    st.warning("请输入您的登录信息！")