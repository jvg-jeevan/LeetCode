class Solution:
    def interpret(self, command: str) -> str:
        # string replace works here
        return command.replace('()', 'o').replace('(al)', 'al')