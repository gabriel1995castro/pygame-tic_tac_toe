class BaseState:
    def __init__(self, state_manager):
        self.state_manager = state_manager
    
    def enter(self):
        pass
    
    def exit(self):
        pass
    
    def handle_event(self, event):
        pass
    
    def update(self):
        pass
    
    def render(self, screen):
        pass
