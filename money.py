import streamlit as st

# 1. 页面基本配置
st.set_page_config(page_title="Mitce 官方特惠通道", page_icon="🚀")

# 你的专属推广链接
MY_AFF_LINK = "https://mitce.net/aff.php?aff=31164"

# 2. 这里的逻辑改了：直接用 HTML 伪装一个大按钮，点击必带参数
st.title("🚀 Mitce 全球极速网络加速器")
st.subheader("稳定、安全、秒开 4K，您的跨境办公首选")

st.markdown(f"""
    <div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; border: 1px solid #dcdfe6;">
        <p style="color: #606266;">🎁 <b>检测到专属优惠：</b>通过此页面注册可激活 8 折内部码并获赠高级会员试用。</p>
        <a href="{MY_AFF_LINK}" target="_blank" style="text-decoration: none;">
            <div style="background-color: #ff4b4b; color: white; padding: 15px; text-align: center; border-radius: 8px; font-size: 20px; font-weight: bold; cursor: pointer; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                🔥 点击前往 Mitce 官网领优惠
            </div>
        </a>
        <p style="text-align: center; font-size: 12px; color: #909399; margin-top: 10px;">(点击后请确认地址栏带有 aff=31164 即可享受优惠)</p>
    </div>
""", unsafe_allow_html=True)

st.write("---")
st.markdown("### 📋 简单两步，开启极速体验")
st.write("1. **点击上方红色按钮** 在官网注册账号。")
st.write("2. **下载对应客户端** (支持 Win/Mac/安卓/iOS) 登录即可使用。")

# 强制检测（如果用户没点按钮，下面这个也是保险）
st.sidebar.link_button("🔗 备用备用跳转链接", MY_AFF_LINK)
