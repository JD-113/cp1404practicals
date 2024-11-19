"""
CP1404 prac Dynamic labels
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabels(App):
    """Main program - Kivy app to show the names by name list"""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.name_list = ["Madi", "Kris", "James", "Leo"]

    def create_widgets(self):
        """Create buttons from data and add them to the GUI."""
        for name in self.name_list:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Name Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root


DynamicLabels().run()
