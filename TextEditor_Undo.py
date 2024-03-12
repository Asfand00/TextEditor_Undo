class TextOperation:
    def __init__(self, op_type, character=None):
        self.op_type = op_type
        self.character = character

class TextEditor:
    def __init__(self):
        self.text = ""
        self.operation_stack = []

    def add_text(self, character):
        self.text += character
        operation = TextOperation("add", character)
        self.operation_stack.append(operation)

    def delete_last_character(self):
        if self.text:
            deleted_character = self.text[-1]
            self.text = self.text[:-1]
            operation = TextOperation("delete", deleted_character)
            self.operation_stack.append(operation)

    def undo(self):
        if self.operation_stack:
            last_operation = self.operation_stack.pop()
            if last_operation.op_type == "add":
                self.text = self.text[:-1]
            elif last_operation.op_type == "delete":
                self.text += last_operation.character

    def display_text(self):
        print("Current Text:", self.text)

# Example usage
editor = TextEditor()

# Manual input of adding text (can modify to whatever text you want)
editor.add_text("H")
editor.add_text("e")
editor.add_text("l")
editor.add_text("l")
editor.add_text("o")
editor.display_text()  # Output: Current Text: Hello (if modified Current text is different)

editor.delete_last_character()
editor.display_text()  # Output: Current Text: Hell

editor.undo()
editor.display_text()  # Output: Current Text: Hello
print()

# Operation to delete two characters then undo last two operations 
editor.delete_last_character()
editor.delete_last_character()
editor.display_text() # Output: Current Text: Hel
editor.undo()
editor.undo()
editor.display_text() # Output: Current Text: Hello
print()

# Operation to delete last character, add new character "!", then undo last operation
editor.delete_last_character()
editor.add_text("!")
editor.display_text() # Output: Current Text: Hell!
editor.undo()
editor.display_text() # Output: Current Text: Hell
print()

# Edge Case 1: delete characters until theres nothing left to delete
editor.delete_last_character()
editor.delete_last_character()
editor.delete_last_character()
editor.delete_last_character()
editor.delete_last_character()
editor.display_text() # Current Text: 
print()

# Edge Case 2: Undos every operation so far until there is nothing left to undo 
editor.undo()
editor.undo()
editor.undo()
editor.undo()
editor.undo()
editor.undo()
editor.undo()
editor.undo()
editor.undo()
editor.undo()
editor.display_text() # Current Text: 
print()
