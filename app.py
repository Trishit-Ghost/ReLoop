import streamlit as st


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="Reloop",
    page_icon="🌱",
    layout="wide"
)


# ==================================================
# SESSION STATE
# ==================================================

if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"

if "uploaded_items" not in st.session_state:
    st.session_state.uploaded_items = []


# ==================================================
# NAVIGATION FUNCTION
# ==================================================

def go_to(page_name):
    st.session_state.current_page = page_name


# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.title("🌱 Reloop")

st.sidebar.write("Give your unwanted items a second life.")

st.sidebar.divider()

if st.sidebar.button("🏠 Home", use_container_width=True):
    go_to("Home")

if st.sidebar.button("📦 Upload Item", use_container_width=True):
    go_to("Upload Item")

if st.sidebar.button("📊 Dashboard", use_container_width=True):
    go_to("Dashboard")


# ==================================================
# HOME PAGE
# ==================================================

if st.session_state.current_page == "Home":

    st.title("🌱 Reloop")

    st.subheader("Give your unwanted items a second life.")

    st.write(
        """
        Reloop is a smart sustainability platform that helps reduce waste
        by giving unwanted items another purpose instead of throwing them away.
        """
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("📦 Upload")
        st.write(
            "List items that you no longer need."
        )

    with col2:
        st.subheader("🔄 Reuse")
        st.write(
            "Help your unwanted items find a new purpose."
        )

    with col3:
        st.subheader("🌍 Impact")
        st.write(
            "Reduce waste and track your sustainability impact."
        )

    st.divider()

    st.subheader("Ready to give something a second life?")

    if st.button(
        "➕ Upload an Item",
        use_container_width=True
    ):
        go_to("Upload Item")
        st.rerun()


# ==================================================
# UPLOAD ITEM PAGE
# ==================================================

elif st.session_state.current_page == "Upload Item":

    st.title("📦 Upload an Item")

    st.write(
        "Tell us about the item you want to give a second life."
    )

    st.divider()

    item_name = st.text_input(
        "Item Name",
        placeholder="Example: Old Laptop, Study Table, Mathematics Book"
    )

    category = st.selectbox(
        "Category",
        [
            "Books & Paper",
            "Electronics & Electrical",
            "Clothes, Footwear & Accessories",
            "Furniture & Home Items",
            "Toys & Sports Equipment",
            "Other"
        ]
    )

    condition = st.selectbox(
        "Condition",
        [
            "Excellent",
            "Good",
            "Fair",
            "Damaged",
            "Not Working"
        ]
    )

    description = st.text_area(
        "Item Description",
        placeholder=(
            "Describe the item, its condition, "
            "and any important details..."
        ),
        height=120
    )

    photo = st.file_uploader(
        "📷 Upload a Photo of the Item",
        type=["jpg", "jpeg", "png"]
    )

    if photo is not None:
        st.image(
            photo,
            caption="Item Preview",
            use_container_width=True
        )

    location = st.text_input(
        "Location",
        placeholder="Example: Kolkata"
    )

    action = st.selectbox(
        "What would you like to do?",
        [
            "Give Away",
            "Exchange",
            "Donate",
            "Sell"
        ]
    )

    st.divider()

    if st.button(
        "🌱 Submit Item",
        use_container_width=True
    ):

        if not item_name.strip():

            st.error("Please enter an item name.")

        else:

            new_item = {
                "name": item_name,
                "category": category,
                "condition": condition,
                "description": description,
                "location": location,
                "action": action
            }

            st.session_state.uploaded_items.append(new_item)

            st.success(
                "🎉 Your item has been successfully added to Reloop!"
            )

            st.balloons()


# ==================================================
# DASHBOARD PAGE
# ==================================================

elif st.session_state.current_page == "Dashboard":

    st.title("📊 My Dashboard")

    st.write(
        "Track your uploaded items and sustainability impact."
    )

    st.divider()

    total_items = len(st.session_state.uploaded_items)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "📦 My Items",
            total_items
        )

    with col2:
        st.metric(
            "🌱 Green Points",
            total_items * 20
        )

    with col3:
        st.metric(
            "♻️ Estimated Waste Avoided",
            f"{total_items * 2} kg"
        )

    st.divider()

    st.subheader("📦 My Uploaded Items")

    if total_items == 0:

        st.info(
            "You haven't uploaded any items yet. "
            "Go to Upload Item and add your first item!"
        )

    else:

        for index, item in enumerate(
            st.session_state.uploaded_items,
            start=1
        ):

            with st.expander(
                f"📦 {index}. {item['name']}"
            ):

                st.write(
                    f"**Category:** {item['category']}"
                )

                st.write(
                    f"**Condition:** {item['condition']}"
                )

                st.write(
                    f"**Location:** {item['location']}"
                )

                st.write(
                    f"**Preference:** {item['action']}"
                )

                if item["description"]:
                    st.write(
                        f"**Description:** {item['description']}"
                    )

                st.success("Status: Available 🌱")