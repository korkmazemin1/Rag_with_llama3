from llama_index.core import SimpleDirectoryReader, Settings, VectorStoreIndex,PromptTemplate
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama


# Veri yükleme
# PDF dosyalarından oluşan bir klasörü alıyoruz ve verileri yüklüyoruz
loader = SimpleDirectoryReader(
    input_dir="database",
    required_exts=[".pdf"],
    recursive=True
)
docs = loader.load_data()

# Gömme işlemi - Embedding
# Bu aşamada metin verisini nümerik vektörlere çeviriyoruz
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-large-en-v1.5", trust_remote_code=True)

# Vector Database
# Bu işlemler, veriyi bellekte daha hızlı bulunabilir hale getirir
Settings.embed_model = embed_model
index = VectorStoreIndex.from_documents(docs)

# Dil modelinin hazırlanması 
llm_llama = Ollama(model="llama3", request_timeout=120.0)

Settings.llm = llm_llama  # hangi LLM'in kullanılacağı belirtiliyor

query_engine = index.as_query_engine(streaming=True, similarity_top_k=4)

# similarity parametresi ile sorguya yakın 4 parça alınır (ANN)
# streaming ise chatin anlık (yazıyormuş gibi) yanıt vermesini sağlar ve hızı da arttırır

# Prompt şablonunun oluşturulması
qa_prompt_tmpl_str = (
    "You are an expert in agriculture. "
    "Please provide a concise and clear explanation based on the context information below.\n"
    "---------------------\n"
    "{context_str}\n"
    "---------------------\n"
    "In case you don't know the answer, say 'I don't know!'.\n"
    "Query: {query_str}\n"
    "Answer: "
)

qa_prompt_tmpl = PromptTemplate(template=qa_prompt_tmpl_str)  # template parametresi ile oluşturma

# Prompt güncellenmesi
query_engine.update_prompts({"response_synthesizer:text_qa_template": qa_prompt_tmpl})

# Sorgulama yapılması
response = query_engine.query("can u tell me about agriculture? ")
print(response)
