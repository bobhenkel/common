# Common Bolt Module
Bolt module that contains common tasks and plans that are widely and don't have a better home.

To experiment with running a python based task:

```
Install Bolt https://puppet.com/docs/bolt/latest/bolt_installing.html
git clone git@github.com:bobhenkel/common.git
cd common
bolt puppetfile install --boltdir .
bolt task run common::pytask -n localhost name='Bob' --module-path .
```
