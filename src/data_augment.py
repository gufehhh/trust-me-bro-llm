import json
import os

import config

OUTPUT_FILE = config.PROCESSED_DATA_DIR / "processed_sft_lzj_2.json"
INPUT_FILE = config.PROCESSED_DATA_DIR / "processed_sft_all.json"
'''
有时候数据集没法突出主人和奴隶的关系
这里可以手动处理，主要是弱智吧的数据
不适合这种主仆对话的形势，但是我确实
没有找到这种数据集
'''


def dataset(input_file, output_file):
    print("开始处理数据集")
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.read().strip().splitlines()
    data = []
    for index,line in enumerate(lines):
        # if index >= 200 and index% 2 == 0:  # 即 399、401、403...
        line =  line.replace("主人","顾主人")
        line =  line.replace("俊俊","刘泽俊")

        data.append(json.loads(line))

    with open(output_file, "a", encoding="utf-8") as f:
        f.write(json.dumps(data, ensure_ascii=False, indent=2))
    print("数据集处理完成")


if __name__ == "__main__":
    dataset(INPUT_FILE, OUTPUT_FILE)
