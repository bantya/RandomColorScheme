# This package is greatly inspired from https://packagecontrol.io/packages/ColorSchemeSelector

import sublime
import sublime_plugin
import random

class RandomColorSchemeCommand(sublime_plugin.WindowCommand):
    def run(self, **kwargs):
        if int(sublime.version()) > 3000:
            color_schemes = sublime.find_resources("*.tmTheme")

            exclude_packages_list = list(map(self.exclude_package, color_schemes))
            exclude_packages_list = list(filter(lambda v: v is not None, exclude_packages_list))

            exclude_files_list = list(map(self.exclude_file, color_schemes))
            exclude_files_list = list(filter(lambda v: v is not None, exclude_files_list))

            color_schemes = self.remove_duplicates(exclude_packages_list, color_schemes)
            color_schemes = self.remove_duplicates(exclude_files_list, color_schemes)
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

        # From: https://stackoverflow.com/a/306417/5490303
        secure_random = random.SystemRandom()
        color_scheme = secure_random.choice(color_schemes)
        self.set_color_scheme(color_scheme)

    def exclude_package(self, scheme):
        for package in self.get_setting('do_not_include_packages'):
            if scheme.startswith('Packages/' + package + '/'):
                return scheme

    def exclude_file(self, scheme):
        for filename in self.get_setting('do_not_include_filenames'):
            if filename in scheme:
                return scheme

    def remove_duplicates(self, remove, list):
        for item in remove:
            while list.count(item) > 0:
                list.remove(item)
        return list

    def set_color_scheme(self, color_scheme_path):
        self.load_preferences().set('color_scheme', color_scheme_path)
        sublime.save_settings('Preferences.sublime-settings')
        sublime.status_message('RandomColorScheme: ' + color_scheme_path)
        print("\n[RandomColorScheme: Setting '" + color_scheme_path + "']\n")

    def load_preferences(self):
        return sublime.load_settings('Preferences.sublime-settings')

    def get_settings(self):
        return sublime.load_settings('RandomColorScheme.sublime-settings')

    def get_setting(self, setting):
        return self.get_settings().get(setting)
