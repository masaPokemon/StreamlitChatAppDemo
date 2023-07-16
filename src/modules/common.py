import streamlit as st
from st_pages import Page, show_pages, add_page_title, hide_pages
import const
from modules import common


def set_pages():
    # Set the pages
    default_pages = [
        Page("src/01_login.py", "Login/Logout", "🏠"),
        Page("src/other_pages/02_register_user.py", "Register user", "📝"),
    ]
    after_login_pages = [
        Page("src/other_pages/03_reset_password.py", "Reset password", "🔑"),
        Page("src/other_pages/04_change_icon.py", "Change icon", "👤"),
        Page("src/other_pages/05_set_character.py", "Set character", "🤖"),
        Page("src/other_pages/06_chat.py", "Chat", "💬"),
        Page("src/other_pages/07_settings.py", "Settings", "⚙️"),
    ]
    pages = default_pages
    if (
        common.check_if_exists_in_session(const.SESSION_INFO_AUTH_STATUS)
        and st.session_state[const.SESSION_INFO_AUTH_STATUS]
    ):
        pages += after_login_pages
    show_pages(pages)


def check_if_exists_in_session(key: str) -> bool:
    """Check if key exists in session state

    Args:
        key (str): key to check.

    Returns:
        bool : True if key exists in session state, False otherwise.
    """
    if key in st.session_state:
        return True
    else:
        return False
