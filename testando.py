import streamlit as st

st.markdown('## Relatório Power BI - Consultoria SULMINAS')

# Embutir o relatório Power BI usando um iframe
st.markdown(
    """
    <iframe title="Degustação Consultoria" width="1320" height="800" src="https://app.powerbi.com/reportEmbed?reportId=649e9077-71ed-47f5-b5a7-6cd451a8fe7a&autoAuth=true&ctid=32341a06-b690-4834-94a3-d0b2f7bda7e0" frameborder="0" allowFullScreen="true"></iframe>
    """,
    unsafe_allow_html=True
)


