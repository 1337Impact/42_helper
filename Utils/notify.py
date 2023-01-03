import os

class bc:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def notify(arg):
    # os.system("""osascript -e 'display notification "{}" with title "{}"'""".format(text, title))
    # os.system("""osascript -e 'say "post {} has been freed" using "Victoria"'""".format(arg))
    os.system("""osascript -e 'display alert "post {} has been freed"'""".format(arg))