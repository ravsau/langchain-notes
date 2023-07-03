Langchain Doc: https://python.langchain.com/docs/modules/model_io/models/llms/integrations/llamacpp



### Steps: 

1) Clone this repo or copy the llama.py file
    - `git clone https://github.com/ravsau/langchain-notes`

2) navigate into the lesson folder
    - `cd local-llama-langchain`
  
3) Install requirement package
 - `pip install langchain`
 - `pip install llama-cpp-python` FOR CPU Based inference 
   -  OR for GPU inference `CMAKE_ARGS="-DLLAMA_CUBLAS=on" FORCE_CMAKE=1 pip install llama-cpp-python`

4) Download a local LLaMa( or LLaMa compatible model) from https://gpt4all.io/index.html
5) Change the `model_path` in the `llama_langchain.py` file to reference the model file you you downloaded in previous step. 
6) Run the `llama_langchain.py` file( in this folder) 
   - ```python llama_langchain.py```

  
