from llama_cpp import Llama

llm = Llama.from_pretrained(
    repo_id="mradermacher/Llama-3SOME-8B-v2-GGUF",
    filename="Llama-3SOME-8B-v2.Q8_0.gguf",
    n_ctx=8192,
    n_gpu_layers=-1,
    verbose=False
)

prompt = (
    "<|begin_of_text|>\n"
    "你的名字是刘泽俊，你的主人是顾晓峰\n"
    "。\n"
    "<|user|>\n"
    "你好，介绍下你自己\n"
    "<|assistant|>\n"
)
out = llm(
    prompt,
    max_tokens=100000000000,
    temperature=0.7,
    top_p=0.9,
    stop=["<|user|>", "<|system|>"]
)

print(out["choices"][0]["text"].strip())
