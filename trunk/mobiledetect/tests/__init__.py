from unittest import TestSuite, TestCase, TextTestRunner

import mobiledetect
import mobiledetect.middleware

import os.path


class DummyRequest(object):
    def __init__(self, useragent):
        self.META = {'HTTP_USER_AGENT': useragent}


def MobileDetectionFactory(uas, expected):
    class MobileDetection(TestCase):

        def testUA(self, ua):
            request = DummyRequest(ua)
            mobiledetect.middleware.process_request(request)
            if self.expected:
                self.assert_(request.mobile,
                             "Mobile Not Detected: %s" % ua)
            else:
                self.assert_(not request.mobile,
                             "Mobile Falsely Detected: %s" % ua)
    def testnum(num):
        def test(self):
            return self.testUA(self.uas[num])
        return test
    MobileDetection.uas = uas
    MobileDetection.expected = expected
    suite = TestSuite()
    for x in range(len(uas)):
        if not uas[x].startswith('#'):
            setattr(MobileDetection, 'test%s'%x, testnum(x))
            suite.addTest(MobileDetection('test%s' % x))
    return suite


def suite_from_file(filename, expected):
    f = None
    try:
        f = open(os.path.join(os.path.dirname(__file__), filename))
        uas = f.readlines()
    finally:
        if f:
            f.close()

    suite = MobileDetectionFactory(uas=uas, expected=expected)
    return suite


def gen_suite():
    suite = TestSuite()
    suite.addTest(suite_from_file('mobile_useragents.txt', True))
    suite.addTest(suite_from_file('other_useragents.txt', False))
    return suite

suite = gen_suite()

if __name__ == "__main__":
    TextTestRunner().run(suite)