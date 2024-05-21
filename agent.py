import threading
import datetime
import time

class Agent():
    def __init__(self, name):
        self.name = name
        self.message_bus = []

    def send_message(self, message_list, message):
        message_list.append(message)
        return

    def receive_message(self, message_list):
        del_list = []
        for message in message_list:
            if message['receiver'] == self.name:
                self.message_bus.append(message)
                del_list.append(message)
        for message in del_list:
            message_list.remove(message)

    def generate_message(self, content, receiver):
        return {'content': content,
                'sender': self.name,
                'receiver': receiver,
                'create_time': datetime.datetime.now()}





def contineous_receive():
    while True:
        agent1.receive_message(global_list)
        agent2.receive_message(global_list)
        time.sleep(3)


def contineous_send():
    while True:
        ms1 = agent1.generate_message('current time is:' + str(datetime.datetime.now()), 'agent2')
        ms2 = agent2.generate_message('current time is:' + str(datetime.datetime.now()), 'agent1')
        agent1.send_message(global_list, ms1)
        agent2.send_message(global_list, ms2)
        time.sleep(3)


def contineous_print():
    while True:
        print('current global_list length:')
        print(len(global_list))
        print('current agent1_message:')
        print(agent1.message_bus)
        print('current agent2_message:')
        print(agent2.message_bus)
        time.sleep(3)

# global_list = []
#
# agent1 = Agent('agent1')
# agent2 = Agent('agent2')
# agent_list = [agent1, agent2]
# arglist = [True]
# receive_thread = threading.Thread(target=contineous_receive, daemon=True)
# send_thread = threading.Thread(target=contineous_send, daemon=True)
# print_thread = threading.Thread(target=contineous_print, daemon=True)
#
# receive_thread.start()
# send_thread.start()
# print_thread.start()



