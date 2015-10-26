from nose.plugins import Plugin
import os
from hashlib import md5

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
    
    def options(self, parser, env=os.environ):
        super(SplitTests, self).options(parser, env)
        parser.add_option("--total-cores", type="int", default=1)
        parser.add_option("--this-core", type="int", default=1)

    def configure(self, options, conf):
        super(SplitTests, self).configure(options, conf)
        if self.enabled:
            self.total_cores = options.total_cores
            self.this_core = options.this_core

    def wantMethod(self, method):
        if method.__name__[:5] == 'test_':
            h_int = int(md5(method.__name__).hexdigest(), 16)
            if h_int % self.total_cores == self.this_core - 1:
                return True
        return False
