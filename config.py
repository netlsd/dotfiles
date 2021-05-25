#c.bindings.default = {}
c.auto_save.session = True
c.scrolling.smooth = True

config.unbind('b')
config.unbind('PP')
config.unbind('pp')
config.unbind('D')
config.unbind('m')
config.unbind('M')
config.unbind('j')
config.unbind('k')

config.bind('pP', 'open -t -- {primary}')
config.bind('pp', 'open -t -- {clipboard}')
config.bind('PP', 'open -- {clipboard}')
config.bind('Pp', 'open -- {clipboard}')
config.bind('D', 'quit --save')
config.bind('m', 'bookmark-add')
config.bind('M', 'set-mark')
config.bind('gh', 'open -t qute://history/')
config.bind('th', 'open -t https://bbs.hupu.com/all-nba')
config.bind('j', 'run-with-count 50 scroll down')
config.bind('k', 'run-with-count 50 scroll up')

config.bind("tt", "set-cmd-text -s :open -t")
config.bind('b', 'set-cmd-text -s :tab-select')
config.bind('h', 'tab-prev')
config.bind('l', 'tab-next')
config.load_autoconfig()
