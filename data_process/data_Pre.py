import pandas as pd
import json
import torch
def changeData(dataPath):
    tmps = []
    with open(dataPath, encoding='utf-8') as f:
        for data in f:
            data = json.loads(data)
        for i in data:
            tmps.append(i)
    result = []
    for tmp in tmps:
        r = {}
        r["q"] = tmp['question']
        r["a"] = tmp['answer']
        r["video_id"] = tmp['video']
        result.append(r)
    with open("/datas/wanglin/learn_code/Video-ChatGPT-main/data_process/Train.json", 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False)


def main():
    trainQA = "/datas/wanglin/dataset/MSVD-QA/data_json/msvd_qa_train.json"
    changeData(trainQA)


main()


