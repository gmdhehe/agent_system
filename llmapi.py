import dashscope
from typing import Callable, List, Dict, Any, Union
dashscope.api_key = 'sk-7c9a9c96c16a4bdc8c1c98e1609887cf'


class LLMApi():
    def __init__(self, model) -> None:
        """
        Initializes the Baichuan2 API with the specified API key.
        """
        self.model = model

        self.api_key = dashscope.api_key
        self.max_number_of_tries = 3

    def llm_generate(self, prompt: str, check_function: Callable[[str], bool] = None,
                     load_function: Callable[[str], Union[dict, list, str]] = None,
                     max_number_of_tries: int = 3) -> str:
        counter = 0
        result = ""
        while counter < self.max_number_of_tries:
            try:
                messages = [{'role': 'user', 'content': prompt}]
                response = dashscope.Generation.call(
                    model='baichuan2-7b-chat-v1',
                    messages=messages,
                    result_format='message',  # set the result to be "message" format.
                )
                result = response['output']["choices"][0]["message"]["content"]
                if check_function is not None:
                    if check_function(result) == False:
                        raise Exception("reponde format is not correct")
                if load_function is not None:
                    assert check_function is not None, '''check function is required for load function'''
                    result = load_function(result)
                return result
            except Exception as e:
                print(e)
                counter += 1
        return result


if __name__ == "__main__":
    baichuan2_api = LLMApi("baichuan2-7b-chat-v1")
    prompt = "What is the meaning of life?"
    result = baichuan2_api.llm_generate(prompt)
    print(result)