'''
如果不想要自己造数据，可以尝试自己更换字符串，但是问题是可能替换不完全
ai生成的名字不确定性很大，只能自己试着去替换
'''
import json
import config
def replace_name(input_file, output_file1):
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.read().strip().splitlines()

    data = [line.replace(config.AUTHOR_NAME,config.AUTHOR_NAME_NEW) for line in lines]
    data = [line.replace(config.STUDENT_NAME,config.STUDENT_NAME_NEW) for line in data]
    data = [line.replace(config.STUDENT_SUBNAME,config.STUDENT_SUBNAME_NEW) for line in data]


    #接下来的替换凭借自己的想象
    data = [line.replace("俊俊","小三") for line in data]
    data = [line.replace("字节跳动","大王") for line in data]
    data = [line.replace("晓峰","大王") for line in data]


    data = [json.loads(line) for line in data]

    with open(output_file1, "a", encoding="utf-8") as f:
        f.write(json.dumps(data,ensure_ascii=False,indent=2))

    print("数据集处理完成")

if __name__ == '__main__':
    INPUT_FILE = config.PROCESSED_DATA_DIR / "processed_sft_all.json"
    OUTPUT_FILE1 = config.PROCESSED_DATA_DIR / "processed_sft_show.json"
    replace_name(INPUT_FILE,OUTPUT_FILE1)