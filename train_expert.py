from agent import Agent
from llmapi import LLMApi
def train(role, data_path):
    w = open(data_path, 'r')
    a = w.readlines()
    print(len(a))
    return
    baichuanapi = LLMApi("baichuan2-7b-chat-v1")
    for i in range(len(a)):
        if i == 0:
            continue
        else:
            prompt = "You will now face a stance detection problem and provide some suggestions that may help resolve the issue. In this problem, a tweet and a target will be given, and the objective is to determine the relationship between the tweet and the target. The relationship is provided in the form of options, including the following three choices: (A) Favor (B) Against (C) None."
            prompt += "Here is an example:\nTweet: He who exalts himself shall      be humbled; and he who humbles himself shall be exalted.Matt 23:12.\nTarget: Atheism\nAnswer: (A)"
            prompt += "As a politician and base on the example given above, give one advice on what political feature should we focus on, which will help for solving this question. Please keep the given advice as concise as possible."
            result = baichuanapi.llm_generate(prompt)
            print(prompt)
            print(result)
            break


train('politician', r'E:\临时下载\stance-data-all-annotations\data-all-annotations\testdata-taskA-all-annotations.txt')