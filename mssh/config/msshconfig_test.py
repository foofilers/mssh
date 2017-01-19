import unittest
from os import remove

from mssh.config import SshHubConfig


class MyTestCase(unittest.TestCase):
	def test_loading(self):
		cnf = SshHubConfig("tests/test.yml");
		cnf.load()
		print(cnf)

		self.assertIsNotNone(cnf.environments.develop)
		print("environments")
		for env in cnf.environments.keys():
			print(env)
		print(cnf.environments.develop)
		for srv in cnf.environments.develop.product1.servers:
			print(srv)
		self.assertEqual(len(cnf.environments.develop.product1.servers), 2)
		self.assertIsNotNone(cnf.environments.develop.product1.servers.server1.host)
		print(cnf.environments.develop.product1.servers.server1.host)
		self.assertEquals(cnf.environments.develop.product1.servers.server1.host, 'server1.intra.company.com')
		self.assertAlmostEqual(cnf.environments.develop.product1.servers.server1.users, ['user1', 'user2'])

	def test_saving(self):
		tst_fname = "/tmp/test.yml"
		try:
			cnf_wr = SshHubConfig(tst_fname)
			cnf_wr.load()
			self.assertTrue(len(cnf_wr.environments) == 0)
			server1 = cnf_wr.environments.add('develop').add('servers').add('server1')
			server1['host'] = 'server1.intra.company.com'
			server1['users'] = ['user1', 'user2']
			cnf_wr.save()

			cnf = SshHubConfig(tst_fname)
			cnf.load()

			self.assertIsNotNone(cnf.environments.develop)
			print(cnf.environments.develop)
			for srv in cnf.environments.develop.servers:
				print(srv)
			self.assertEqual(len(cnf.environments.develop.servers), 1)
			self.assertIsNotNone(cnf.environments.develop.servers.server1.host)
			print(cnf.environments.develop.servers.server1.host)
			self.assertEquals(cnf.environments.develop.servers.server1.host, 'server1.intra.company.com')
			self.assertAlmostEqual(cnf.environments.develop.servers.server1.users, ['user1', 'user2'])
		finally:
			remove(tst_fname)


if __name__ == '__main__':
	unittest.main()
