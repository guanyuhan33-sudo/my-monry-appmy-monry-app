import streamlit as st

# 1. 网页标题与高端图标
st.set_page_config(page_title="Mitce Global - 极速专线接入", page_icon="💎", layout="centered")

# 你的专属推广链接
MY_AFF_LINK = "https://mitce.net/aff.php?aff=31164"

# 2. 注入高级 CSS 样式
st.markdown(f"""
    <style>
    .stApp {{ background-color: #0e1117; color: white; }}
    .promo-card {{
        background: linear-gradient(135deg, #1e1e2f 0%, #2d2d44 100%);
        padding: 30px;
        border-radius: 20px;
        border: 1px solid #3e3e5e;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }}
    .price-tag {{ color: #ff4b4b; font-size: 24px; font-weight: bold; margin: 10px 0; }}
    .btn-main {{
        display: inline-block;
        background: linear-gradient(90deg, #ff4b4b 0%, #ff7575 100%);
        color: white !important;
        padding: 15px 40px;
        border-radius: 50px;
        text-decoration: none;
        font-size: 22px;
        font-weight: bold;
        transition: transform 0.3s;
        margin-top: 20px;
    }}
    .btn-main:hover {{ transform: scale(1.05); box-shadow: 0 0 20px rgba(255,75,75,0.4); }}
    .feature-text {{ color: #a0a0c0; font-size: 14px; margin-top: 10px; }}
    </style>
    """, unsafe_allow_html=True)

# 3. 页面核心内容
st.markdown("""
    <div style='text-align: center; padding-bottom: 20px;'>
        <h1 style='color: white; font-size: 40px;'>💎 Mitce 全球专线</h1>
        <p style='color: #8080a0;'>2026 企业级跨界网络解决方案</p>
    </div>
    """, unsafe_allow_html=True)

# 动态倒计时效果（模拟紧迫感）
st.warning("⏳ 专属 8 折内部优惠名额仅剩最后 7 个，申领后 24 小时内有效")

# 核心卡片
st.markdown(f"""
    <div class="promo-card">
        <h2 style="color: white; margin-bottom: 0;">专属合作伙伴特惠</h2>
        <div class="price-tag">限时折扣：立减 20% + 送 3 天试用</div>
        <p style="color: #ccccff;">支持 8K 视频 / ChatGPT 优化 / 全球 200+ 节点</p>
        <a href="{MY_AFF_LINK}" class="btn-main" target="_blank">🚀 立即激活专属权限</a>
        <div class="feature-text">
            <span>✅ 军工级加密</span> | <span>✅ 晚高峰零延迟</span> | <span>✅ 全平台支持</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# 增加信任背书
col1, col2, col3 = st.columns(3)
col1.metric("全球用户", "500k+", "+12%")
col2.metric("平均延迟", "45ms", "-15%")
col3.metric("服务可用率", "99.9%", "Stable")

st.markdown("---")
st.caption("注：本页面由 Mitce 官方合作伙伴提供，点击跳转后请认准官方域名 mitce.net。")
