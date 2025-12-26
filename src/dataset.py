import json
import os

import config
OUTPUT_FILE = config.PROCESSED_DATA_DIR / "processed_sft_lzj.json"
INPUT_FILE = config.PROCESSED_DATA_DIR / "processed_sft_all.json"
'''
这个文件用于将jsonl格式的文件转化为标注json格式文件
'''
def dataset(input_file, output_file):
    print("开始处理数据集")
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.read().strip().splitlines()

    data = [json.loads(line) for line in lines]

    with open(output_file, "a", encoding="utf-8") as f:
        f.write(json.dumps(data,ensure_ascii=False,indent=2))
    print("数据集处理完成")

if __name__ == "__main__":
    dataset(INPUT_FILE,OUTPUT_FILE)
