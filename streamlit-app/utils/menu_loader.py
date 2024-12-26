import streamlit as st
from pages import Home, Upload

# 页面渲染函数映射表
PAGE_RENDERERS = {
    "home": Home.render,
    "upload": Upload.render,
}

# 从数据库加载菜单
def load_menus():
    from db.db_handler import get_menus
    return get_menus()

# 渲染选中的页面
def render_page(selected_menu, menus, authenticator):
    # 查找选中菜单对应的路由
    for menu in menus:
        if menu["name"] == selected_menu:
            route = menu["route"]
            break
    else:
        st.error("未找到对应页面！")
        return

    # 渲染页面内容
    if route == "logout":
        authenticator.logout("退出登录", "sidebar")
        st.success("已成功退出登录，请刷新页面重新登录！")
        st.stop()
    elif route in PAGE_RENDERERS:
        PAGE_RENDERERS[route]()
    else:
        st.error("页面路由未配置！")