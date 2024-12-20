import streamlit as st
import xarray as xr
import matplotlib.pyplot as plt

# 設定頁面標題
st.title("NetCDF Viewer with Streamlit")

# 上傳 .nc 文件
uploaded_file = st.file_uploader("Upload a NetCDF (.nc) file", type=["nc"])

if uploaded_file:
    # 打開 .nc 文件
    ds = xr.open_dataset(uploaded_file)
    
    # 顯示文件信息
    st.subheader("Dataset Information")
    st.text(ds)

    # 提供變數選擇
    variables = list(ds.data_vars.keys())
    selected_var = st.selectbox("Select a variable to visualize", variables)

    if selected_var:
        # 繪製數據
        st.subheader(f"Visualization of {selected_var}")
        data = ds[selected_var]

        # 只支持 2D 數據的簡單可視化
        if len(data.dims) == 2:
            fig, ax = plt.subplots()
            data.plot(ax=ax)
            st.pyplot(fig)
        else:
            st.warning("Currently only 2D data is supported for visualization.")
