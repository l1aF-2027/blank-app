import streamlit as st
import pandas as pd
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
    [data-testid="column"]:first-child {
        position: fixed;
        top: 0;
        left: 0;
        width: 33%;
        height: 100%;
        overflow: hidden;
    }
    [data-testid="column"]:last-child {
        margin-left: 33%;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Hiển thị hai cột
col1, col2 = st.columns([1, 2])

# Cột 1: Hiển thị hình ảnh
with col1:
    st.image("MÙA ĐÔNG ẤM ÁP (1).png", use_container_width=True)

# Cột 2: Hiển thị nội dung chữ
with col2.container(height=1000):
    with st.expander("I/ MỤC ĐÍCH CHƯƠNG TRÌNH:"):
        st.write("Là một chương trình thiện nguyện của Đoàn - Hội khoa Đô Thị học, lần đầu tiên được triển khai nhằm mong muốn được mang đến sự ấm áp của tình người qua những món quà nhỏ, đậm đà tình thân cho những người không may mắn bị mắc bệnh ung thư và ung bướu tại bệnh viện Ung Bướu thành phố Hồ Chí Minh.")
    with st.expander("II/ THỜI GIAN VÀ ĐỊA ĐIỂM:"):
        st.write("- Thời gian: ngày 21/12/2024")
        st.write("- Địa điểm: Hội trường C - tầng 3, Bệnh viện Ung Bướu, Quận 9, thành phố Hồ Chí Minh")

    with st.expander("III/ ĐỐI TƯỢNG THAM GIA:"):
        st.write("- Tình nguyện viên: Sinh viên trường đại học Khoa Học Xã hội và Nhân Văn")
        st.write("- Bệnh nhân: Khoảng 100 bệnh nhân ung thư máu có hoàn cảnh khó khăn")

    with st.expander("IV/ CHIẾN DỊCH BÁN ĐỒ HANDMADE, ĐỒ ĂN VẶT:"):
        data = {
            "SẢN PHẨM": [
                "Bánh tráng xike khô",
                "Bánh tráng trộn ớt rim muối tỏi",
                "Cơm cháy mỡ hành",
                "Cơm cháy chà bông",
                "Bánh gấu",
                "Vòng tay",
                "Dây đeo điện thoại",
            ],
            "GIÁ LẺ": [
                "8k/ 1 bịch",
                "12k/ bịch",
                "9k/ 1 bịch",
                "20k/ bịch",
                "25k/ 1 túi",
                "30k",
                "35k",
            ],
            "GIÁ COMBO": [
                "35k/ 5 bịch",
                "Mua 2 tặng 1 (Bánh tráng xike khô)",
                "22k/ 3 bịch",
                "35k/ 2 bịch tặng 1 bịch cơm cháy mỡ hành",
                "Mua 2 tặng 1",
                "",
                "",
            ],
        }

        # Tạo bảng dữ liệu từ DataFrame
        df = pd.DataFrame(data)

        # Thêm cột to chung "Bảng giá" bằng cách tạo dòng tiêu đề
        st.write("### Bảng giá")

        # Hiển thị bảng trong Streamlit
        st.table(df)
    with st.expander("V/ NHÀ TÀI TRỢ:"):
        st.image("z6128027135817_c5b8af696cb09172df0158de876cbb7b.jpg")