from nose.plugins import Plugin


'''
plugin should:
1. take command line args of 
    a. how many processes there are
    b. which process this one is
2. database should be fine due to transactions? otherwise choose which DB to use.
2. alter the redis connection to use a unique redis database.
3. select some random subset of tests to run.
'''


class SplitTests(Plugin):
    enabled = True

    def begin(self):
        print "BEGIN"
    
    def options(self, parser, env):
        super(Plugin, self).options(parser, env)
        parser.add_option("-c", "--total-cores", type="int")
        parser.add_option("-i", "--this-core", type="int")

    def configure(self, options, conf):
        print options
        print conf



