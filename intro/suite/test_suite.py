import unittest

import HtmlTestRunner

from suite.test_alerts import TestAlerts
from suite.test_keys import TestKeys
from suite.test_waits import WaitWhenElementIsPresentTests
from suite.test_waits_2 import WaitWhenElementIsNotPresentTests


class TestSuite(unittest.TestCase):

    def test_suite(self):

        teste_de_rulat = unittest.TestSuite()

        # teste_de_rulat.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestAlerts))
        # teste_de_rulat.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestKeys))
        # teste_de_rulat.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(WaitWhenElementIsPresentTests))
        # teste_de_rulat.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(WaitWhenElementIsNotPresentTests))

        teste_de_rulat.addTests(
            [
                unittest.defaultTestLoader.loadTestsFromTestCase(TestAlerts),
                unittest.defaultTestLoader.loadTestsFromTestCase(TestKeys),
                unittest.defaultTestLoader.loadTestsFromTestCase(WaitWhenElementIsPresentTests),
                unittest.defaultTestLoader.loadTestsFromTestCase(WaitWhenElementIsNotPresentTests),
            ]
        )

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title='Raport PYTA9',
            report_name="test_result"
        )

        runner.run(teste_de_rulat)