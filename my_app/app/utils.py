from rasa.core.agent import Agent

def load_rasa_agent():
    return Agent.load("models")
