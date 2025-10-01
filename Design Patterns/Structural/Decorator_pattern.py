class TextEditor:
    def write(self):
        return "Writing text"

class SpellCheckDecorator:
    def __init__(self,editor):
        self.editor = editor
    
    def write(self):
        return f"{self.editor.write()} + Spell Check enabled"

class AutoSaveDecorator:
    def __init__(self,editor):
        self.editor = editor
    
    def write(self):
        return f"{self.editor.write()} + Auto Save enabled"

editor = TextEditor()
editor = SpellCheckDecorator(editor)
editor = AutoSaveDecorator(editor)
print(editor.write())