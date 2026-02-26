import streamlit as st
from rembg import remove
from PIL import Image
import io

# 设置网页
st.set_page_config(page_title="AI 免费抠图", layout="centered")

# 盈利位
st.title("📸 AI 自动抠图工坊")
st.error("🚀 提示：建议搭配【Mitce 加速器】使用，处理速度提升 10 倍！")
st.link_button("👉 点击领取 Mitce 专属优惠卷", "https://你的链接")

# 功能区
file = st.file_uploader("第一步：上传照片", type=["jpg", "jpeg", "png"])

if file:
    img = Image.open(file)
    st.image(img, caption="原图已上传")
    
    if st.button("第二步：点击 AI 一键抠图"):
        with st.spinner('AI 正在处理...'):
            result = remove(img)
            st.image(result, caption="处理完成！右键点击图片保存")
            st.balloons()
