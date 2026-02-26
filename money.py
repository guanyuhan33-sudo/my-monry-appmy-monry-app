import streamlit as st

# 1. 页面设置
st.set_page_config(page_title="Mitce Privilege | 尊享接入", page_icon="🌐", layout="wide")

# 你的专属推广链接
MY_AFF_LINK = "https://mitce.net/aff.php?aff=31164"

# 2. 注入顶级视觉样式（CSS）
st.markdown(f"""
    <style>
    /* 全局背景：极夜黑 */
    .stApp {{
        background-color: #050505;
        color: #ffffff;
    }}
    
    /* 渐变流光文字 */
    .shiny-text {{
        background: linear-gradient(120deg, #ffffff 0%, #a0a0a0 50%, #ffffff 100%);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: shine 3s linear infinite;
        font-weight: 800;
        font-size: 3.5rem;
        letter-spacing: -1px;
    }}
    
    @keyframes shine {{
        to {{ background-position: 200% center; }}
    }}

    /* 毛玻璃卡片 */
    .glass-card {{
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 30px;
        padding: 50px;
        text-align: center;
        margin: 20px 0;
    }}

    /* 苹果式动态按钮 */
    .apple-btn {{
        display: inline-block;
        background: #ffffff;
        color: #000000 !important;
        padding: 18px 45px;
        border-radius: 40px;
        font-size: 20px;
        font-weight: 600;
        text-decoration: none;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 4px 20px rgba(255,255,255,0.2);
    }}
    
    .apple-btn:hover {{
        transform: translateY(-3px);
        box-shadow: 0 10px 40px rgba(255,255,255,0.4);
        background: #f0f0f0;
    }}

    /* 隐藏默认元素 */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)

# 3. 页面布局
st.write("") # 间距
st.write("")

# 居中标题
st.markdown("<div style='text-align: center;'><h1 class='shiny-text'>Mitce Ultra</h1></div>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888; font-size: 1.2rem; letter-spacing: 2px;'>BEYOND SPEED. REIMAGINE CONNECTIVITY.</p>", unsafe_allow_html=True)

st.write("")

# 核心橱窗区
st.markdown(f"""
    <div class="glass-card">
        <p style="color: #007aff; font-weight: 600; margin-bottom: 10px;">PREMIUM PARTNER ACCESS</p>
        <h2 style="font-size: 2.5rem; margin-bottom: 20px;">下一代全球专线网络</h2>
        <p style="color: #aaa; max-width: 600px; margin: 0 auto 30px auto; line-height: 1.6;">
            专为 8K 流媒体、大规模数据传输及 AI 开发优化。
            通过合作伙伴协议，您将获得全网最低 80% 准入费率及极速通道权限。
        </p>
        <a href="{MY_AFF_LINK}" class="apple-btn" target="_blank">立即激活专属特惠</a>
        <p style="margin-top: 25px; font-size: 0.9rem; color: #555;">
            — 仅限受邀用户 —
        </p>
    </div>
""", unsafe_allow_html=True)

# 四列核心参数（极简风格）
st.write("")
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown("<p style='color:#555; text-align:center;'>LATENCY</p><h3 style='text-align:center;'>28ms</h3>", unsafe_allow_html=True)
with c2:
    st.markdown("<p style='color:#555; text-align:center;'>BANDWIDTH</p><h3 style='text-align:center;'>10Gbps</h3>", unsafe_allow_html=True)
with c3:
    st.markdown("<p style='color:#555; text-align:center;'>SLA</p><h3 style='text-align:center;'>99.99%</h3>", unsafe_allow_html=True)
with c4:
    st.markdown("<p style='color:#555; text-align:center;'>UPTIME</p><h3 style='text-align:center;'>∞</h3>", unsafe_allow_html=True)

st.write("")
st.write("")

# 底部信息
st.markdown("<div style='text-align: center; color: #333; font-size: 0.8rem;'>Designed by Mitce Ultra Labs. All Rights Reserved.</div>", unsafe_allow_html=True)
