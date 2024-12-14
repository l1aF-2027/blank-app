import streamlit as st

st.set_page_config(
    page_title="Chương trình thiện nguyện",
    page_icon=":page_with_curl:",
    layout="wide"
)

st.markdown(
    f"""
    <style>
    /* Remove default header and manage app button */
    .stApp [data-testid="stHeader"]{{
        display:none;
    }}
    .stApp [data-testid="manage-app-button"]{{
        display:none;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    .fixed-column {
        position: fixed;
        top: 0;
        left: 0;
        width: 33%;
        height: 100vh;
        overflow: hidden;
    }
    .scrollable-column {
        margin-left: 33%;
        width: 67%;
        overflow-y: auto;
        height: 100vh;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Hiển thị hai cột
col1, col2 = st.columns([1, 2], gap="small")

# Cột 1: Hiển thị hình ảnh, cố định
with col1:
    st.markdown('<div class="fixed-column">', unsafe_allow_html=True)
    st.image("MÙA ĐÔNG ẤM ÁP (1).png", use_column_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Cột 2: Hiển thị nội dung chữ
with col2:
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