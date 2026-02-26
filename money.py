import streamlit as st
from rembg import remove
from PIL import Image
from streamlit_image_comparison import image_comparison
import io

# 1. 网页精美配置
st.set_page_config(page_title="AI 极客抠图 - 免费高清版", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 20px; height: 3em; background-color: #FF4B4B; color: white; }
    </style>
    """, unsafe_allow_html=True)

# 2. 招财位：Mitce 推广
st.title("🎨 AI 智能高清抠图")
st.info("💡 提示：本工具完全免费。如果您的网络环境较慢，推荐使用【Mitce 极速加速器】提升 10 倍处理效率！")
st.link_button("🚀 领取 Mitce 专属优惠（点击即领）", "https://你的Mitce链接") 

# 3. 核心功能区
uploaded_file = st.file_uploader("✨ 第一步：选择照片上传 (支持 JPG/PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # 加载图片
    image = Image.open(uploaded_file)
    
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        st.write("📸 已成功上传")
        
    if st.button("🌟 第二步：立即开始 AI 智能处理"):
        with st.spinner('AI 正在精细化处理边缘，请稍候...'):
            # 处理图片
            output = remove(image)
            
            # 转换为字节流供下载
            buf = io.BytesIO()
            output.save(buf, format="PNG")
            byte_im = buf.getvalue()

            # 4. 精美交互：对比显示
            st.success("✅ 处理完成！请左右滑动查看效果")
            image_comparison(
                img1=image,
                img2=output,
                label1="原图",
                label2="AI 抠图"
            )
            
            # 下载按钮
            st.download_button(
                label="💾 点击保存无背景高清图",
                data=byte_im,
                file_name="ai_remove_bg.png",
                mime="image/png"
            )
            st.balloons()
