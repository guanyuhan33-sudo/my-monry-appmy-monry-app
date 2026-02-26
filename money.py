import streamlit as st

# 1. 页面配置：高端、简洁
st.set_page_config(page_title="Mitce 官方合作伙伴 - 专属特惠", page_icon="🚀")

# 自定义样式：让按钮更大更红
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        height: 3em;
        background-color: #FF4B4B;
        color: white;
        font-size: 20px;
        font-weight: bold;
        border-radius: 10px;
    }
    .main { background-color: #fafafa; }
    </style>
    """, unsafe_allow_html=True)

# 2. 网页内容
st.title("🚀 Mitce 全球极速网络加速器")
st.subheader("稳定、安全、秒开 4K，您的跨境办公首选")

st.info("💡 提示：通过本页面注册可激活 [专属 8 折优惠码] 并获赠 3 天高级会员试用。")

# 列出优势
col1, col2, col3 = st.columns(3)
with col1:
    st.write("🔒 **隐私加密**\n无日志记录")
with col2:
    st.write("⚡ **极速专线**\n秒开 YouTube/TG")
with col3:
    st.write("🌍 **全球覆盖**\n100+ 优质节点")

st.write("---")

# 3. 核心赚钱按钮 (已填入你的推广链接)
my_link = "https://mitce.net/aff.php?aff=31164"

st.markdown(f"### ✨ 第一步：点击下方链接注册账号")
if st.button("🔥 立即跳转 Mitce 官网领优惠"):
    st.write(f"正在为您跳转至安全连接... [点击这里手动跳转]({my_link})")
    # 自动重定向提示
    st.markdown(f'<meta http-equiv="refresh" content="0;url={my_link}">', unsafe_allow_html=True)

st.write("---")
st.markdown("### 📱 第二步：下载客户端并登录")
st.write("支持 Windows, Android, iOS, macOS 全平台使用。")

# 底部声明
st.caption("© 2026 Mitce Official Partner. All rights reserved.")
