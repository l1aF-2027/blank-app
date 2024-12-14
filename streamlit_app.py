import streamlit as st

st.set_page_config(
    page_title="Chương trình thiện nguyện",
    page_icon="	:page_with_curl:"
)
import base64

import streamlit as st
import base64

def set_bg_hack(main_bg):
    '''
    A function to unpack an image from root folder and set as bg with custom size and blur effect.
 
    Parameters
    ----------
    main_bg : str
        The path to the background image file.
    
    Returns
    -------
    Sets the background for the Streamlit app.
    '''
    # Set the image format (e.g., png or jpg)
    main_bg_ext = "png"

    # Encode the image file in base64
    with open(main_bg, "rb") as img_file:
        img_base64 = base64.b64encode(img_file.read()).decode()

    # Apply CSS for background with size and blur
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url(data:image/{main_bg_ext};base64,{img_base64});
            background-size: cover; /* Options: contain, cover, or specify in px/percent */
            background-repeat: no-repeat;
            background-position: center;
            filter: blur(1px); /* Adjust the blur effect (e.g., 0px for no blur, 8px for moderate blur) */
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg_hack(r'MÙA ĐÔNG ẤM ÁP (1).png')
st.markdown("<h1 style='text-align: center;'>Mùa đông ấm áp</h1>", unsafe_allow_html=True)

with st.expander("I/ MỤC ĐÍCH CHƯƠNG TRÌNH:"):
    st.write("- Là một chương trình thiện nguyện của Đoàn - Hội khoa Đô Thị học, lần đầu tiên được triển khai nhằm mong muốn được mang đến sự ấm áp của tình người qua những món quà nhỏ, đậm đà tình thân cho những người không may mắn bị mắc bệnh ung thư và ung bướu tại bệnh viện Ung Bướu thành phố Hồ Chí Minh.")

with st.expander("II/ THỜI GIAN VÀ ĐỊA ĐIỂM:"):
    st.write("- Thời gian: ngày 21/12/2024 ( dự trù: đầu tháng 1/2025)")
    st.write("- Địa điểm: Hội trường C - tầng 3, Bệnh viện Ung Bướu, Quận 9, thành phố Hồ Chí Minh")

with st.expander("III/ ĐỐI TƯỢNG THAM GIA:"):
    st.write("- Tình nguyện viên: Sinh viên trường đại học Khoa Học Xã hội và Nhân Văn")
    st.write("- Bệnh nhân: Khoảng 150 bệnh nhân ung thư máu có hoàn cảnh khó khăn")

with st.expander("IV/ KẾ HOẠCH CHƯƠNG TRÌNH:"):
    st.markdown("**4.1 Chuẩn bị trước chương trình:**")
    st.write("- Chiến dịch bán đồ Handmade, đồ ăn vặt:")
    st.table({
        "Sản phẩm": ["Vòng tay, vòng cổ", "Thú nhồi bông hoặc túi thơm", "Móc khóa"],
        "Miêu tả": [
            "Trang sức handmade bằng hạt cườm, dây len, hoặc dây da",
            "Thú nhồi bông hoặc túi thơm với hoa khô tinh dầu mang lại cảm giác ấm áp",
            "Móc khóa làm từ vải nỉ, gỗ, hoặc nhựa resin với hình dạng đáng yêu"
        ]
    })

    st.write("- Tuyển cộng tác viên thời vụ:")
    st.write("Thời gian: Ngày 10/12/2024 truyền thông sẽ lên bài điền form tuyển cộng tác viên. Phỏng vấn trực tiếp lúc 9 giờ sáng ngày 14/12/2024 tại Trường ĐH KHXH&NV.")
    st.write("Số lượng cần: 10-15 CTV chia làm 3 nhóm: Truyền thông, Hậu cần, Tổ chức và sự kiện.")

    st.markdown("**Kế hoạch chi tiết và kịch bản chương trình:**")
    st.write("- Chi tiết về phương tiện di chuyển, kịch bản buổi sáng và buổi chiều sẽ được thông báo qua các tài liệu bổ sung.")
with st.expander("V/ NHÀ TÀI TRỢ:"):
    st.image("z6128027135817_c5b8af696cb09172df0158de876cbb7b.jpg")