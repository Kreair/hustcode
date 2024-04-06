def toggle_theme(self):
    if self.light_mode:
        self.setStyleSheet(open("./src/styles/style_dark.qss", "r").read())
        self.light_mode = False
    else:
        self.setStyleSheet(open("./src/styles/style_light.qss", "r").read())
        self.light_mode = True