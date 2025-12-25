import os
import json
import time
from openai import OpenAI
from volcenginesdkarkruntime import Ark
from config import AUTHOR_NAME, STUDENT_NAME, STUDENT_SUBNAME
'''
根据弱智吧的数据重写回答
让模型生成不一样的回答
这里使用串行去实现
案例：
    "instruction": "俊俊，我那条泳裤还潮着呢，你打算让我光着屁股去游泳馆？",
    "input": "",
    "output": "{{好兄弟的小名或者名字}}（小声嘟囔，尾巴一甩）：主人您别发火呀～俊俊这就给您拿吹风机！三分钟速干，保证让您体面出征游泳馆，绝不走光！"
'''
def chat(question,client,client_name="doubao"):
    completion_question = client.chat.completions.create(
        model="doubao-seed-1-6-251015" if client_name == "doubao" else "kimi-k2-thinking-turbo",
        messages=[
            {"role": "system",
             "content": "我们现在在玩扮演游戏，你的名字是{}，你的小名是{}，你主人的名字是{},随机的一句话：{}，把上面这段话改为符合主人语气的问题".format(STUDENT_NAME,STUDENT_SUBNAME ,AUTHOR_NAME,question)},
        ],
        temperature=1,
    )
    question_new = completion_question.choices[0].message.content
    time.sleep(2)
    completion_answer = client.chat.completions.create(
        model="doubao-seed-1-6-251015" if client_name == "doubao" else "kimi-k2-thinking-turbo",
        messages=[
            {"role": "system",
             "content": "我们现在在玩扮演游戏，你的名字是{}，你的小名是{}，你主人的名字是{},你需要回答主人的问题".format(STUDENT_NAME,STUDENT_SUBNAME ,AUTHOR_NAME)},
            {"role": "user",
             "content": "主人的话：{}".format(question_new)},
        ],
        temperature=1,
    )
    answer_new = completion_answer.choices[0].message.content
    time.sleep(2)
    return question_new,answer_new

def get_client(model_name = "doubao"):
    if model_name == "doubao":
        client = Ark(
            # 此为默认路径，您可根据业务所在地域进行配置
            base_url="https://ark.cn-beijing.volces.com/api/v3",
            # 从环境变量中获取您的 API Key。此为默认方式，您可根据需要进行修改
            api_key="",
        )
        return client
    else:
        client = OpenAI(
            api_key="",
            base_url="https://api.moonshot.cn/v1",
        )
        return client


def process_raw_data(client_name,input_file,output_file):
    print(f"{client_name}开始处理数据")
    os.makedirs(os.path.dirname(output_file), exist_ok=True)


    #读取文件
    with open(input_file,"r",encoding="utf-8") as f:
        raw_data = json.load(f)

    client = get_client(client_name)
    for index,item in enumerate(raw_data):
        question = item.get("instruction")
        instruction,answer = chat(question,client,client_name)
        result = {
            "instruction": instruction,
            "input": "",
            "output": answer,
        }
        print(f"处理到了第{index+1}条数据")
        with open(output_file, "a", encoding="utf-8") as fw:
            fw.write(json.dumps(result, ensure_ascii=False) + "\n")


    print(f"{client_name}处理完成")

