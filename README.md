Bookmarks App on OpenShift
===================

This sample Bookmarks App shows how to deploy a typical Django App on OpenShift in a minute.

Before We Start
---------------

### You need an account on OpenShift

You don't have an account yet? Sign-up and create your account for free : http://www.openshift.com

### Some preparations

Then you need to install 'rhc' client tools following the quickstart on OpenShift website.

Also, make sure that you have 'git' and 'django' installed on your machine.

The last step: create a namespace within your account:

    $ rhc domain create -n ${your_namespace} -l ${your_account}

Let's Rock
----------

### Create a python application called "bookmarks" first:

    $ rhc app create -a bookmarks -t python-2.6

And let's add files in this repo into your Bookmarks app:

    $ cd bookmarks
    $ git remote add upstream -m master git://github.com/lulinqing/openshift-bookmarks.git
    $ git pull -s recursive -X theirs upstream master

Then we need mysql database for your app:

    $ rhc app cartridge add -a bookmarks -c mysql-5.1

### Update for mysql database:

    $ cd wsgi/Bookmarks
    $ vi settings.py

Then update following lines:
Remember to export the OPENSHIFT_* vars into local env if you are using them locally:

    import os.environ           # import if you are using OPENSHIFT_* vars
    'ENGINE': 'mysqlite3',
    'NAME' = 'bookmarks'        # change it according to your database name, or use os.environ['OPENSHIFT_APP_NAME'].
    'USER' = 'admin'            # change it according to your Root Username, or use os.environ['OPENSHIFT_DB_USERNAME'].
    'PASSWORD' = 'xxxxxxxxxx'   # change it according to your Root Password, or use os.environ['OPENSHIFT_DB_PASSWORD'].
    'HOST' = 'xx.xx.xx.xx'      # change it according to your Connection URL, or use os.environ['OPENSHIFT_DB_HOST'].
    'PORT': '3306',             # change it according to your Connection URL, or use os.environ['OPENSHIFT_DB_PORT'].

Done. Let's save it:

    $ git commit -a -m 'update settings.py'
    $ git push

Forward the remote mysql service port to your local machine

    $ rhc-port-forward -a bookmarks

Prepare your mysql database for app, you can create an user now or choose 'no' to do it later.

    $ ./manage.py syncdb


### Enjoy your Bookmarks App at:

    http://bookmarks-${your_namespace}.rhcloud.com

Here goes mine:

    http://bookmarks-linqing.rhcloud.com/
