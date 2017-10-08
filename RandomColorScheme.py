# This package is greatly inspired from https://packagecontrol.io/packages/ColorSchemeSelector
import sublime
import sublime_plugin
from random import random

class RandomColorSchemeCommand(sublime_plugin.WindowCommand):
    def run(self, **kwargs):
        if int(sublime.version()) > 3000:
            color_schemes = sublime.find_resources("*.tmTheme")
        else:
            color_schemes = [
                "All Hallow's Eve",
                "Amy",
                "Blackboard",
                "Cobalt",
                "Dawn",
                "Eiffel",
                "Espresso Libre",
                "IDLE",
                "LAZY",
                "Mac Classic",
                "MagicWB (Amiga)",
                "Monokai Bright",
                "Monokai",
                "Pastels on Dark",
                "Slush & Poppies",
                "Solarized (Dark)",
                "Solarized (Light)",
                "SpaceCadet",
                "Sunburst",
                "Twilight",
                "Zenburnesque",
                "iPlastic"
            ]

        index = int(random() * len(color_schemes))

        self.set_color_scheme(color_schemes[index])

    def set_color_scheme(self, color_scheme_path):
        self.load_settings().set('color_scheme', color_scheme_path)
        sublime.save_settings('Preferences.sublime-settings')
        sublime.status_message('RandomColorScheme: ' + color_scheme_path)
        print('')
        print('RandomColorScheme: Set the following color scheme')
        print(color_scheme_path)
        print('')

    def load_settings(self):
        return sublime.load_settings('Preferences.sublime-settings')

