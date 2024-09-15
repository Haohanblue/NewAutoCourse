import sys

class test_interface(ScrollArea):
    """ test interface """

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.scrollWidget = QWidget()
        self.expandLayout = ExpandLayout(self.scrollWidget)

        # test label
        self.testLabel = QLabel(self.tr("test"), self)

        # test
        self.testGroup = SettingCardGroup(
            self.tr('test'), self.scrollWidget)
        self.testCard = SwitchSettingCard(
            FIF.TRANSPARENT,
            self.tr('test'),
            self.tr('test'),
            cfg.testEnabled,
            self.testGroup
        )
        self.testCard = ComboBoxSettingCard(
            cfg.testMode,
            FIF.BRUSH,
            self.tr('test'),
            self.tr("test"),
            texts=[
                self.tr('test'), self.tr('test'),
                self.tr('test')
            ],
            parent=self.testGroup
        )
        self.testCard = ComboBoxSettingCard(
            cfg.testScale,
            FIF.ZOOM,
            self.tr("test"),
            self.tr("test"),
            texts=[
                "test", "test", "test", "test", "test",
                self.tr("test")
            ],
            parent=self.testGroup
        )
        self.testCard = ComboBoxSettingCard(
            cfg.test,
            FIF.LANGUAGE,
            self.tr('test'),
            self.tr('test'),
            texts=['test', 'test', 'test', self.tr('test')],
            parent=self.testGroup
        )

        # test
        self.testGroup = SettingCardGroup(
            self.tr("test"), self.scrollWidget)
        self.testCard = SwitchSettingCard(
            FIF.UPDATE, 