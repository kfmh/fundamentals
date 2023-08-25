from textual.app import App, ComposeResult
from textual.widgets import Label, Button
from textual import events

class Fnds_math(App[str]):
    CSS_PATH = "math_app.css"
    
    def on_mount(self) -> None:
        self.screen.styles.background = 'gray'
    
    def compose(self) -> ComposeResult:
        yield Label("Do you love Textual?")
        yield Button("Yes", id="yes",  variant="primary")
        yield Button("No", id="no", variant="error")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.exit(event.button.id)


if __name__ == '__main__':
    app = Fnds_math()
    reply = app.run()
print(reply)