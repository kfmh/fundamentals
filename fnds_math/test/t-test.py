from textual import events
from textual.app import App, ComposeResult
from textual.widgets import Label, Button, Header, RichLog

class Fnds_math(App[str]):
    CSS_PATH = "math_app.css"

    def on_mount(self) -> None:
        self.screen.styles.background = 'gray'

    TITLE = "A Question App"
    SUB_TITLE = "The most important question"

    def compose(self) -> ComposeResult:
        yield RichLog()
        yield Header()
        yield Label("Do you love Textual?", id="question")
        yield Button("Yes", id="yes",  variant="primary")
        yield Button("No", id="no", variant="error")

    def on_key(self, event: events.Key) -> None:
        self.query_one(RichLog).write(event) 

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.exit(event.button.id)


if __name__ == '__main__':
    app = Fnds_math()
    reply = app.run()
    print(reply)