# !pip install llama-cpp-python

from llama_cpp import Llama

llm = Llama.from_pretrained(
	repo_id="tastypear/CausalLM-14B-DPO-alpha-GGUF",
	filename="causallm_14b-dpo-alpha.Q8_0.gguf",
)
output = llm(
	"Once upon a time,",
	max_tokens=512,
	echo=True
)
print(output)