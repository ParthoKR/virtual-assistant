from .actions import Actions
class Commands:
    def __init__(self):
        self.commands = {
                "open youtube": ["Opening youtube...", Actions.open_youtube, -1],
                "open explorer": ["Opening explorer...", Actions.open_explorer, -1],
                "open facebook": ["Opening facebook...", Actions.open_facebook, -1],
                "open chrome": ["Opening chrome...", Actions.open_chrome, -1],

                "messages": ["Checking messages...", lambda x: None, 0],

                "my ip": ["Fetching your ip...", lambda x: None, 1],
                "ip": ["Fetching your ip...", lambda x: None, 1],


                "covid update": ["Fetching covid update...", lambda x: None, 2],
                "covid": ["Fetching covid update...", lambda x: None, 2],

                "covid update global": ["Fetching covid update...", lambda x: None, 3],
                "covid global update": ["Fetching covid update...", lambda x: None, 3],

            }
    def get_commands(self):
        return self.commands