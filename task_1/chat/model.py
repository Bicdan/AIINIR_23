from langchain.document_loaders import DirectoryLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import LlamaCpp
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from chat.loader import DocLoader

class ChatModel:
    def __init__(self, temperature=0.75, max_tokens=2000, top_p=1,
                 hf_model_name='sentence-transformers/all-MiniLM-L6-v2'):
        llm = LlamaCpp(
            model_path='../model/llama-2-7b-chat.Q4_K_M.gguf',
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            verbose=False,
        )

        template = """Ответь на вопрос, используя следующий контекст.
        Постарайся сделать так, чтобы ответ был ёмким.
        Не пытайся придумать ответ, если не знаешь его.
        Контекст: {context}
        Вопрос: {question}
        Ответ:
        """

        prompt = PromptTemplate(
            template=template,
            input_variables=['context', 'question'])
        loader = DirectoryLoader('./tinkoff-terms/', glob='*.csv', loader_cls=DocLoader)
        texts = loader.load()

        embeddings = HuggingFaceEmbeddings(
            model_name=hf_model_name,
            model_kwargs={'device': 'cpu'},
            cache_folder='./cache')
        db = FAISS.from_documents(texts, embeddings)
        retriever = db.as_retriever(search_kwargs={'k': 2})

        self.qa_llm = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type='stuff',
            retriever=retriever,
            return_source_documents=True,
            chain_type_kwargs={'prompt': prompt})

    def __call__(self, question):
        return self.qa_llm({'query': question})