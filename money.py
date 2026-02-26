import streamlit as st
from rembg import remove
from PIL import Image
import io

# 1. 设置网页标题
st.set_page_config(page_title="AI 免费证件照制作")
st.title("📸 AI 自动抠图工坊")

# 2. 你的赚钱收银台（一定要换成你真实的 Mitce 链接）
st.error("🚀 提示：处理高清图片较慢？建议配合【Mitce 加速器】使用：")
# 这里把引号里的链接换成你在 Mitce 后台拿到的那个推广链接
st.link_button("👉 点击领取 Mitce 专属优惠卷", "https://你的推广链接")

# 3. 核心功能：上传照片
file = st.file_uploader("第一步：上传你的照片", type=["jpg", "png", "jpeg"])

if file:
    img = Image.open(file)
    st.image(img, caption="原图已上传", use_container_width=True)
    
    if st.button("第二步：点击 AI 一键制作"):
        with st.spinner('AI 正在玩命处理中...'):
            # 执行抠图
            result = remove(img)
            st.image(result, caption="处理完成！右键点击图片保存", use_container_width=True)
            st.balloons() # 撒花特效
