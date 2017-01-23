import unittest
from os import remove

from mssh.config import MsshConfig

tst_fname = "/tmp/test.yml"

class MyTestCase(unittest.TestCase):
	
	def test_a_saving(self):
		cnf_wr = MsshConfig(tst_fname)
		cnf_wr.load()
		server1 = cnf_wr.environments.add('develop').add('product1').add('servers').add('server1')
		server1['host'] = 'server1.intra.company.com'
		server1['users'] = ['user1', 'user2']
		cnf_wr.save()

		cnf = MsshConfig(tst_fname)
		cnf.load()

		self.assertIsNotNone(cnf.environments.develop)
		self.assertEqual(len(cnf.environments.develop.product1.servers), 1)
		self.assertIsNotNone(cnf.environments.develop.product1.servers.server1.host)
		self.assertEqual(cnf.environments.develop.product1.servers.server1.host, 'server1.intra.company.com')
		self.assertAlmostEqual(cnf.environments.develop.product1.servers.server1.users, ['user1', 'user2'])
	
	def test_b_loading(self):
		cnf = MsshConfig(tst_fname);
		cnf.load()

		self.assertIsNotNone(cnf.environments.develop)
		self.assertEqual(len(cnf.environments.develop.product1.servers), 1)
		self.assertIsNotNone(cnf.environments.develop.product1.servers.server1.host)
		self.assertEqual(cnf.environments.develop.product1.servers.server1.host, 'server1.intra.company.com')
		self.assertAlmostEqual(cnf.environments.develop.product1.servers.server1.users, ['user1', 'user2'])

	@classmethod
	def tearDownClass(cls):
		remove(tst_fname)

