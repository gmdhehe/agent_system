from datetime import datetime, timedelta
import os


class Config:
    BAICHUAN2_API_KEY = 'sk-59a84bf0e47f4262b51e16d7427a77fe'

    def __init__(self):
        self.BAICHUAN2_API_URL = 'https://api.openai.com/v1/engines/davinci-codex/completions'
        self.envirement_folder = r'envirement/'
        self.map_file = os.path.join(self.envirement_folder, 'map.json')

        self.reflctengine_prompt_folder = r'prompt/engine/reflctengine_prompt/v1/'
        self.planengine_prompt_folder = r'prompt/engine/planengine_prompt/v1'
        self.actiongine_prompt_folder = r'prompt/engine/actionengine_prompt/v1/'
        self.memorystore_prompt_folder = r'prompt/engine/memorystore_prompt/v1/'

        self.comunication_prompt_folder = r'prompt/engine/actionengine_prompt/v1/communication_action_prompt/v1'
        self.agent_listening_folder = os.path.join(self.envirement_folder, 'agent_listening')
        if not os.path.exists(self.agent_listening_folder):
            os.makedirs(self.agent_listening_folder)
        self.movementaction_prompt_folder = r'prompt/engine/actionengine_prompt/v1/movement_action_prompt/v1'
        self.moveaction_prompt_folder = r'prompt/engine/actionengine_prompt/v1/movement_action_prompt/v1'
        self.room_folder = os.path.join(self.envirement_folder, 'room')
        if not os.path.exists(self.room_folder):
            os.makedirs(self.room_folder)

        self.otheraction_prompt_folder = r'prompt/engine/actionengine_prompt/v1/other_action_prompt/v1'
        self.otheraction_takeplace_folder = os.path.join(self.envirement_folder, 'otheraction')
        if not os.path.exists(self.otheraction_takeplace_folder):
            os.makedirs(self.otheraction_takeplace_folder)

        self.llm_name = 'baichuan2'


CONFIG = Config()