#c.bindings.default = {}
c.auto_save.session = True

config.unbind('b')

config.bind("t", "set-cmd-text -s :open -t")
config.bind('b', 'set-cmd-text -s :tab-select')
config.bind('h', 'tab-prev')
config.bind('l', 'tab-next')
config.load_autoconfig()
