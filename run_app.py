from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput

import warnings
import ruamel
warnings.simplefilter('ignore', ruamel.yaml.error.UnsafeLoaderWarning)


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/restaurantnlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-695878195878-682333010819-701551794229-9b98f2d08fb35ca60f01ce0f1a02d6ab', #app verification token
							'xoxb-695878195878-701551798405-8WAlomLKYEkBfDtkO43RvRCZ', # bot verification token
							'ugmoHkfyipe5pkZRjOfljUMi', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))