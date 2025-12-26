import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel

base_model = "meta-llama/Meta-Llama-3-8B-Instruct"
lora_path = "../models/llama_lora"          # 你的 adapter_model.safetensors 所在目录
save_path = "../models/merged_model"       # 合并后模型保存目录

# tokenizer
tokenizer = AutoTokenizer.from_pretrained(base_model)

# base model
model = AutoModelForCausalLM.from_pretrained(
    base_model,
    torch_dtype=torch.float16,
    device_map="auto",
)

# load lora
model = PeftModel.from_pretrained(model, lora_path)

# merge
model = model.merge_and_unload()

# save
model.save_pretrained(save_path, safe_serialization=True)
tokenizer.save_pretrained(save_path)

print("✅ LoRA merged and saved.")
