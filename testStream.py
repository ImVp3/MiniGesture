import streamlit as st
import cv2

def main():
    st.title("ABCNSJS")

    # Hiển thị tiêu đề
    st.header("ABCNSJS")

    # Khởi tạo video capture từ webcam
    cap = cv2.VideoCapture(0)

    # Hiển thị video từ webcam
    while True:
        ret, frame = cap.read()
        # Hiển thị frame trong Streamlit
        st.image(frame, channels="BGR")

    # Giải phóng video capture và đóng Streamlit
    cap.release()

if __name__ == "__main__":
    main()
