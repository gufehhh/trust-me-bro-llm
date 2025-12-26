from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("merged_model")
model = AutoModelForCausalLM.from_pretrained(
    "merged_model",
    torch_dtype=torch.float16,
    device_map="auto",
)

