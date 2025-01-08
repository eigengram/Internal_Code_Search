import streamlit as st
import requests

# Backend API base URL
BASE_URL = "http://127.0.0.1:8000"

# Page Title
st.set_page_config(page_title="Code Repository", layout="wide")
st.title("Internal Code Repository")

# Sidebar Navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Go to", ["Search Code", "Add Code", "Edit/Delete Code"])

# 1. Search Code
if options == "Search Code":
    st.header("Search for Code Blocks")
    query = st.text_input("Enter keyword or tag to search:", "")
    if st.button("Search"):
        response = requests.get(f"{BASE_URL}/codeblocks", params={"query": query})
        if response.status_code == 200:
            code_blocks = response.json()
            if code_blocks:
                for code_block in code_blocks:
                    st.subheader(code_block["title"])
                    st.write(f"**Description:** {code_block['description']}")
                    st.write(f"**Tags:** {code_block['tags']}")
                    st.code(code_block["code"], language="python")
                    st.write("---")
            else:
                st.warning("No code blocks found for your query.")
        else:
            st.error("Error fetching code blocks. Please try again.")

# 2. Add Code
elif options == "Add Code":
    st.header("Add a New Code Block")
    title = st.text_input("Title", "")
    description = st.text_area("Description", "")
    tags = st.text_input("Tags (comma-separated)", "")
    code = st.text_area("Code Snippet", "")
    
    if st.button("Submit"):
        payload = {
            "title": title,
            "description": description,
            "tags": tags,
            "code": code
        }
        response = requests.post(f"{BASE_URL}/codeblocks", json=payload)
        if response.status_code == 200:
            st.success("Code block added successfully!")
        else:
            st.error("Failed to add code block. Please check your input.")

# 3. Edit/Delete Code
elif options == "Edit/Delete Code":
    st.header("Edit or Delete Code Blocks")

    # Fetch all code blocks
    response = requests.get(f"{BASE_URL}/codeblocks")
    if response.status_code == 200:
        code_blocks = response.json()
        if code_blocks:
            # Display code blocks in a dropdown
            code_block_map = {f"{cb['title']} (ID: {cb['id']})": cb['id'] for cb in code_blocks}
            selected_code = st.selectbox("Select Code Block", list(code_block_map.keys()))
            selected_id = code_block_map[selected_code]

            # Choose Action: Edit or Delete
            action = st.selectbox("Action", ["Edit", "Delete"])

            if action == "Edit":
                st.subheader("Edit Code Block")
                # Fetch selected code block details
                selected_code_block = next(cb for cb in code_blocks if cb['id'] == selected_id)
                title = st.text_input("Title", selected_code_block["title"])
                description = st.text_area("Description", selected_code_block["description"])
                tags = st.text_input("Tags", selected_code_block["tags"])
                code = st.text_area("Code Snippet", selected_code_block["code"])

                if st.button("Update"):
                    payload = {
                    "title": title,
                    "description": description,
                    "tags": tags,
                    "code": code
                    }
                    update_response = requests.put(f"{BASE_URL}/codeblocks/{selected_id}", json=payload)
                    if update_response.status_code == 200:
                        st.success("Code block updated successfully!")
                    elif update_response.status_code == 404:
                        st.warning("Code block not found. It may have been deleted.")
                    else:
                        st.error("Failed to update code block. Please check your input.")


            elif action == "Delete":
                if st.button("Delete"):
                    delete_response = requests.delete(f"{BASE_URL}/codeblocks/{selected_id}")
                    if delete_response.status_code == 200:
                        st.success("Code block deleted successfully!")
                    else:
                        st.error("Failed to delete code block. Please check the ID.")
        else:
            st.warning("No code blocks available.")
    else:
        st.error("Failed to fetch code blocks. Please check the backend server.")


