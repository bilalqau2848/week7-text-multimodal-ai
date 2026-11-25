import streamlit as st
from PIL import Image

st.set_page_config(page_title="Week 7 - Text + Multimodal AI", layout="centered")
st.title("Week 7 - Text + Multimodal AI")
st.write("Text aur Image dono se AI jaisa response banayein.")

text = st.text_area("Apna text yahan likhein:")
image = st.file_uploader("Image upload karein", type=["jpg", "png", "jpeg"])

if st.button("Generate"):
    if text:
        st.subheader("Text Analysis:")
        st.write(f"Words: {len(text.split())}")
        st.write(f"Summary: {text[:200]}...")
    if image:
        st.subheader("Image Preview:")
        st.image(Image.open(image), use_container_width=True)
        st.write("Image successfully uploaded and processed.")
    if not text and not image:
        st.warning("Pehle text ya image dein.")
