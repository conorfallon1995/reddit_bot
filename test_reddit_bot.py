import unittest
import config



class Test(unittest.TestCase):
    def test_bot_login(self):

    # See here on how to finish:
    # https://www.jetbrains.com/help/pycharm/testing-your-first-python-application.html#run-test
        self.assertEqual(config.username, "WiSe2122")

        self.assertEqual(config.password, "berlinertest")

        self.assertEqual(config.client_id, "D2jBA2btVjFmpQrV1_cqlg")

        self.assertEqual(config.client_secret, "EpLZqMZvNh9SvbNbPMC-SN48s3xt3g")




    #def test_run_bot(self):
        #self.assertNotEqual(self.film, "")
