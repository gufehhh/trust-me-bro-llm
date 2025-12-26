import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel

# =========================
# 本地路径配置
# =========================

BASE_MODEL_DIR = "" #这里需要替换成自己在modelscope上下载的模型
LORA_DIR = "../models/llama_lora"

# =========================
# 加载 tokenizer
# =========================

tokenizer = AutoTokenizer.from_pretrained(
    BASE_MODEL_DIR,
    trust_remote_code=True,
)

# =========================
# 加载 base model
# =========================

model = AutoModelForCausalLM.from_pretrained(
    BASE_MODEL_DIR,
    torch_dtype=torch.float16,
    device_map="auto",
    trust_remote_code=True,
)

# =========================
# 挂载 LoRA
# =========================

model = PeftModel.from_pretrained(
    model,
    LORA_DIR,
)

model.eval()

# =========================
# 初始化对话历史
# =========================

messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]

print("💬 开始对话（输入 exit / quit 退出）")

# =========================
# 循环对话
# =========================

while True:
    user_input = input("\nUser: ").strip()
    if user_input.lower() in ["exit", "quit"]:
        print("👋 对话结束")
        break

    # 1. 追加用户输入
    messages.append({"role": "user", "content": user_input})

    # 2. 构造模型输入
    inputs = tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
        tokenize=True,
        return_dict=True,
        return_tensors="pt",
    ).to(model.device)

    # 3. 推理
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=256,
            temperature=0.7,
            top_p=0.9,
            do_sample=True,
        )

    # 4. 解码新增 token（只取 assistant 部分）
    response = tokenizer.decode(
        outputs[0][inputs["input_ids"].shape[-1]:],
        skip_special_tokens=True,
    )

    print(f"Assistant: {response}")

    # 5. 追加 assistant 回复到历史
    messages.append({"role": "assistant", "content": response})
