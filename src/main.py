import threading
from dataset import dataset
from config import RAW_DATA_DIR, PROCESSED_DATA_DIR
from process import process_raw_data

#这里一晚上大概处理到5000条数据
#定义需要处理的数据,第一个是弱智吧
INPUT_FILE_RUO_ZI = RAW_DATA_DIR / "ruozhiba_qa.json"
#第二个是自我认知的数据集
INPUT_FILE_SELF = RAW_DATA_DIR / "identity.json"
#定义两个的输出路径(直接放在一起即可)
OUTPUT_FILE = PROCESSED_DATA_DIR / "processed_sft.json"
#定义jsonl转为json文件后的的存放地址
OUTPUT_FILE_JSON = PROCESSED_DATA_DIR / "processed_sft_json.json"

if __name__ == '__main__':
    #这里需要注意跑的时间，大概需要一整个晚上
    t1 = threading.Thread(
        target=process_raw_data,
        args=("doubao", INPUT_FILE_RUO_ZI, OUTPUT_FILE)
    )

    t2 = threading.Thread(
        target=process_raw_data,
        args=("kimi", INPUT_FILE_SELF, OUTPUT_FILE)
    )

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    #因为之前append的是jsonl格式，这里转为json格式
    dataset(OUTPUT_FILE,OUTPUT_FILE_JSON)
    print("两个数据源都处理完成")

