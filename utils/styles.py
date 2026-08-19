import streamlit as st


def inject_styles() -> None:
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&family=Inter:wght@400;500&display=swap');

        /* ── Global reset ── */
        html, body, [data-testid="stAppViewContainer"] {
            background-color: #0D0D1A !important;
            color: #F0EAF8;
            font-family: 'Inter', sans-serif;
        }

        /* ── Main content area ── */
        [data-testid="stMain"] {
            background-color: #0D0D1A !important;
        }

        /* ── Sidebar ── */
        [data-testid="stSidebar"] {
            background-color: #1A1A2E !important;
            border-right: 2px solid #7530BF;
        }
        [data-testid="stSidebar"] * {
            color: #F0EAF8 !important;
            font-family: 'Space Grotesk', sans-serif !important;
        }
        [data-testid="stSidebarNav"] a {
            border-radius: 8px;
            padding: 6px 12px;
            margin: 2px 0;
            display: block;
            transition: background 0.2s;
        }
        [data-testid="stSidebarNav"] a:hover {
            background: rgba(229, 112, 40, 0.15) !important;
        }
        [data-testid="stSidebarNav"] a[aria-current="page"] {
            background: rgba(229, 112, 40, 0.25) !important;
            box-shadow: 0 0 8px rgba(229, 112, 40, 0.4);
            color: #E47028 !important;
        }

        /* ── Headings ── */
        h1, h2, h3 {
            font-family: 'Space Grotesk', sans-serif !important;
            color: #E47028 !important;
        }

        /* ── Buttons ── */
        [data-testid="stBaseButton-primary"], .stButton > button {
            background-color: #E47028 !important;
            color: #ffffff !important;
            border: none !important;
            border-radius: 8px !important;
            font-family: 'Space Grotesk', sans-serif !important;
            font-weight: 600 !important;
        }
        .stButton > button:hover {
            background-color: #F0924A !important;
            box-shadow: 0 0 12px rgba(229, 112, 40, 0.5);
        }

        /* ── Expanders ── */
        [data-testid="stExpander"] {
            background-color: #1A1A2E !important;
            border: 1px solid #7530BF !important;
            border-radius: 8px !important;
        }

        /* ── Info / warning boxes ── */
        [data-testid="stAlert"] {
            background-color: #1A1A2E !important;
            border-left: 4px solid #7530BF !important;
        }

        /* ── File uploader ── */
        [data-testid="stFileUploader"] {
            background-color: #1A1A2E !important;
            border: 2px dashed #7530BF !important;
            border-radius: 8px !important;
        }

        /* ── Muted text helper class ── */
        .muted {
            color: #9B8BB4 !important;
            font-size: 0.9em;
        }

        /* ── Feature card ── */
        .feature-card {
            background: #1A1A2E;
            border: 1px solid #2A2A4A;
            border-radius: 12px;
            padding: 1.25rem;
            text-align: center;
        }
        .feature-card h3 {
            margin-bottom: 0.4rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
