import streamlit as st

from rag import (
    load_pdf,
    split_documents,
    get_embeddings,
    create_vectorstore,
    get_retriever,
    get_llm
)
from memory import (
    init_db,
    save_message,
    load_memory
)
init_db()
if "chat_history" not in st.session_state:

    st.session_state.chat_history = load_memory()

st.title("📚 PDF RAG Chatbot")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type="pdf"
)

if uploaded_file:

    with open(
        f"data/{uploaded_file.name}",
        "wb"
    ) as f:
        f.write(uploaded_file.getbuffer())

    docs = load_pdf(
        f"data/{uploaded_file.name}"
    )

    chunks = split_documents(docs)

    st.success(
        f"Loaded {len(docs)} pages"
    )

    st.info(
        f"Created {len(chunks)} chunks"
    )

    embeddings = get_embeddings()

    st.success(
        "Embedding Model Loaded"
    )

    db = create_vectorstore(chunks)

    st.success(
        "Vector Database Created"
    )
    question = st.text_input(
        "Ask a question about the PDF"
    )
    if question:
        retriever = get_retriever(db)

        docs = retriever.invoke(question)

        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        llm = get_llm()
        history = ""

        for role, message in st.session_state.chat_history:
            history += f"{role}: {message}\n"

        prompt = f"""
        Previous Conversation:

        {history}

        Context:

        {context}

        Current Question:

        {question}

        Answer using both the conversation
        and the PDF context.
        """
        answer = llm.invoke(prompt)

        st.session_state.chat_history.append(
            ("user", question)
        )

        st.session_state.chat_history.append(
            ("assistant", answer)
        )
        save_message(
            "user",
            question
        )

        save_message(
            "assistant",
            answer
        )

        st.subheader("Chat")

        for role, message in st.session_state.chat_history:

            if role == "user":
                st.markdown(f"🧑 **You:** {message}")

            else:
                st.markdown(f"🤖 **Bot:** {message}")