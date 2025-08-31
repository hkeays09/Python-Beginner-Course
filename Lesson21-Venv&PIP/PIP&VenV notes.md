# PIP - commands in the terminal that help you install packages


## Uninstall package
py -m pip uninstall

## Install package
py -m pip install 

## List of installed packages
py -m pip list

## Other functions
Can also download specific versions and update with specfic versions.

## Concrete example using requests package:

py -m pip install requests

# Virtual Environments (VenV)

Dont include in github or gitenvironement as not typically done. Allows you to have two versions of the same module at the same time.

You can create one with 'py -m venv .venv'

It is important that you activate the virtual environement each time you want to work on a proejct with  'source .venv/Scripts/activate'

You can deactivate with 'deactivate'.

Arrow keys to go through previous commands.

Some useful tools:
$ py -m pip freeze > requirements.txt

Must hide .env files as it contains our "secrets". Our API key is in there and it should not be shared.