# -*- coding:utf-8 -*-
from uiautomator import device as d


#Register Watcher
#When a selector can not find a match, uiautomator will run all registered watchers.

#Click target when conditions match
d.watcher("AUTO_FC_WHEN_ANR").when(text="ANR").when(text="Wait") \
                             .click(text="Force Close")
# d.watcher(name) ## creates a new named watcher.
#  .when(condition)  ## the UiSelector condition of the watcher.
#  .click(target)  ## perform click action on the target UiSelector.

#Press key when conditions match
d.watcher("AUTO_FC_WHEN_ANR").when(text="ANR").when(text="Wait") \
                             .press.back.home()
# Alternative way to define it as below
d.watcher("AUTO_FC_WHEN_ANR").when(text="ANR").when(text="Wait") \
                             .press("back", "home")
# d.watcher(name) ## creates a new named watcher.
#  .when(condition)  ## the UiSelector condition of the watcher.
#  .press.<keyname>.....<keyname>.()  ## press keys one by one in sequence.
#  Alternavie way defining key sequence is press(<keybname>, ..., <keyname>)

#Check if the named watcher triggered
#A watcher is triggered, which means the watcher was run and all its conditions matched.
d.watcher("watcher_name").triggered
# true in case of the specified watcher triggered, else false

#Remove named watcher
# remove the watcher
d.watcher("watcher_name").remove()

#List all watchers
d.watchers
# a list of all registered wachers' names

#Check if there is any watcher triggered
d.watchers.triggered
#  true in case of any watcher triggered

#Reset all triggered watchers
# reset all triggered watchers, after that, d.watchers.triggered will be false.
d.watchers.reset()

#Remove watchers
# remove all registered watchers
d.watchers.remove()
# remove the named watcher, same as d.watcher("watcher_name").remove()
d.watchers.remove("watcher_name")

#Force to run all watchers
# force to run all registered watchers
d.watchers.run()
