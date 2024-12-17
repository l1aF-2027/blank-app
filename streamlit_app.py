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
        html_code = """
        <style>
            table {
                width: 100%;
                border-collapse: collapse;
                font-family: Arial, sans-serif;
            }
            th, td {
                border: 1px solid black;
                text-align: center;
                padding: 8px;
            }
            th[colspan] {
                background-color: #f2f2f2;
                font-size: 18px;
            }
        </style>
        <table>
            <tr>
                <th colspan="4">Bảng giá</th>
            </tr>
            <tr>
                <th rowspan="5">ĐỒ ĂN VẶT</th>
                <td>Bánh tráng xike khô</td>
                <td>8k/ 1 bịch</td>
                <td>35k/ 5 bịch</td>
            </tr>
            <tr>
                <td>Bánh tráng trộn ớt rim muối tỏi</td>
                <td>12k/ bịch</td>
                <td>Mua 2 tặng 1 (Bánh tráng xike khô)</td>
            </tr>
            <tr>
                <td>Cơm cháy mỡ hành</td>
                <td>9k/ 1 bịch</td>
                <td>22k/ 3 bịch</td>
            </tr>
            <tr>
                <td>Cơm cháy chà bông</td>
                <td>20k/ bịch</td>
                <td>35k/ 2 bịch tặng 1 bịch cơm cháy mỡ hành</td>
            </tr>
            <tr>
                <td>Bánh gấu</td>
                <td>25k/ 1 túi</td>
                <td>Mua 2 tặng 1</td>
            </tr>
            <tr>
                <th rowspan="2">ĐỒ HANDMADE</th>
                <td>Vòng tay</td>
                <td>30k</td>
                <td></td>
            </tr>
            <tr>
                <td>Dây đeo điện thoại</td>
                <td>35k</td>
                <td></td>
            </tr>
        </table>
        """

        # Hiển thị bảng HTML trong Streamlit
        st.markdown(html_code, unsafe_allow_html=True)
    with st.expander("V/ NHÀ TÀI TRỢ:"):
        st.image("z6128027135817_c5b8af696cb09172df0158de876cbb7b.jpg")