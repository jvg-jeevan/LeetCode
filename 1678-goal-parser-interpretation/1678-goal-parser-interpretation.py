class Solution:
    def interpret(self, command: str) -> str:
        # string replace() '()' with 'o' and '(al)' with 'al
        return command.replace('()', 'o').replace('(al)', 'al')