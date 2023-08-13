import random
from textual.app import App, ComposeResult
from textual.widgets import RadioButton, RadioSet

one = str(random.randint(1, 9) + random.randint(1, 9))
two = str(random.randint(1, 9) + random.randint(1, 9))
three = str(random.randint(1, 9) + random.randint(1, 9))

class RadioChoicesApp(App[None]):
    CSS_PATH = "radio_button.css"

    def compose(self) -> ComposeResult:
        with RadioSet():
            yield RadioButton(one)
            yield RadioButton(two)
            yield RadioButton(three)

    def on_mount(self) -> None:
        self.query_one(RadioSet).focus()


if __name__ == "__main__":
    RadioChoicesApp().run()