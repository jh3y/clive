
def run_task(task):
    myClass = __import__('tasks.' + task)
    mod = getattr(myClass, task)
    mod.run()


def run(config):
    print 'thanks for the chewy config yummm'
    for task in config['tasks']:
        if config['tasks'][task] == True:
            run_task(task)
