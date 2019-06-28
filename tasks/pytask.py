#!/usr/bin/env python

import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'python_task_helper', 'files'))
from task_helper import TaskHelper

class PyTask(TaskHelper):
    def task(self, args):
        return {'result': 'Hi, this is a python task and my name is '+args['name']}

if __name__ == '__main__':
    PyTask().run()

#https://github.com/puppetlabs/puppetlabs-python_task_helper
#cd into this directory
#bolt puppetfile install --boltdir .
#bolt task run common::pytask -n localhost name='Bob' --module-path .
