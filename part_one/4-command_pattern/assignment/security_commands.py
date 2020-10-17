from actions.security import Security
from command_abc import AbsCommand

class SecurityArmCommand(AbsCommand):

    def __init__(self, security):
        if not isinstance(security, Security):
            raise TypeError('Expected a Security object, got %s instead' % security.__class__.__name__)
        self.security = security

    def execute(self):
        self.security.arm()

    def undo(self):
        self.security.disarm()


class SecurityDisarmCommand(AbsCommand):

    def __init__(self, security):
        if not isinstance(security, Security):
            raise TypeError('Expected a Security object, got %s instead' % security.__class__.__name__)
        self.security = security

    def execute(self):
        self.security.disarm()

    def undo(self):
        self.security.arm()