from textual.app import App, ComposeResult
from textual.widgets import Button, Header, Footer, Static
from textual.containers import ScrollableContainer


class Plugin(Static):
    def compose(self) -> ComposeResult:
        yield Button("Start", id="start", variant="success")
        yield Button("Stop", id="stop", variant="error")
        yield Button("Reset", id="reset")


class BlyatApp(App):
    CSS_PATH = "main.tcss"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield ScrollableContainer(Plugin(), Plugin(), Plugin(), id="timers")

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark


if __name__ == "__main__":
    app = BlyatApp()
    app.run()
