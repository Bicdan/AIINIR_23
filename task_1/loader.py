import re
import pandas as pd
import PyPDF2
from langchain.docstore.document import Document
from langchain.document_loaders.base import BaseLoader


class DocLoader(BaseLoader):
    def __init__(self, file_path):
            self.file_path = file_path

    def load(self):
        texts = []
        meta = {"source": self.file_path}
        file_extension = self.file_path.split('.')[-1]

        if file_extension == 'csv':
            return self.read_csv(texts, meta)
        elif file_extension == 'pdf':
            return self.read_pdf(meta)
        else:
             return texts
    
    def read_csv(self, texts, meta):
        df = pd.read_csv(self.file_path)
        for row in df.iterrows():
            text = f"Service: {row[1]['Service']}, Condition: {row[1]['Condition']}, Tariff: {row[1]['Tariff']}"
            texts.append(text)
        return [Document(page_content=text, metadata=meta) for text in texts]
    
    def read_pdf(self, meta):
        reader = PyPDF2.PdfReader(self.file_path)
        text = " ".join([page.extract_text() for page in reader.pages])
        text = text.replace('\xa0', ' ').replace('\n', ' ')
        pattern = r"\d+ из \d+"
        result = re.sub(pattern, "", text)
        texts = [row for row in result.split('.') if len(row) >= 10]
        return [Document(page_content=text, metadata=meta) for text in texts]