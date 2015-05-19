# "tasks": {
# "linking"   : true,
# "homebrew"  : true,
# "brew_cask" : true,
# "git"       : true,
# "apm"       : true,
# "npm"       : true,
# "fish_shell": true,
# "osx"       : true,
# "apple_apps": true
# },


import json

import tasks.runner

print '###################################'
print '# CLIVE WANTS TO MAKE THINGS EASY #'
print '###################################'

config = {}

def ask(question):
    reply = raw_input(question + ' (y/n): ').lower().strip()
    if reply == 'y':
        return True
    if reply == 'n':
        return False
    else:
        return ask("please enter y/n ")


try:
    with open('clive.json') as packages:
        config = json.load(packages)

    goInteractive = ask('would you like to tell Clive what to do? (else rely on config.tasks)')

    if goInteractive:
        for task in config['tasks']:
            config['tasks'][task] = ask('Do you want to run ' + task + '?')

    tasks.runner.run(config)

except IOError:
    print '[ clive ] there is no config file in place :('
