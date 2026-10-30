import unittest
from evidence import search_evidence, get_source, check_comparability, get_hypothesis

class EvidenceTests(unittest.TestCase):
    def test_traceable_search(self):
        results=search_evidence('seguimiento')['results']
        self.assertEqual([x['source_id'] for x in results], ['S5'])
        self.assertTrue(all(x['locator'] and x['synthetic'] for x in search_evidence('')['results']))
    def test_project_isolation(self):
        for fn,args in [(get_source,('S1','other-client')),(search_evidence,('','other-client')),
                        (get_hypothesis,('H1','other-client')),
                        (check_comparability,('S1','S2','other-client'))]:
            with self.assertRaises(ValueError): fn(*args)
    def test_no_arbitrary_file_read(self):
        with self.assertRaises(ValueError): get_source('../../secrets')
    def test_incompatible_annual_indicator(self):
        r=check_comparability('S1','S4')
        self.assertEqual(r['status'],'incompatible')
        self.assertFalse(r['can_pool'])
    def test_partial_period_requires_review(self):
        self.assertEqual(check_comparability('S1','S2')['status'],'partial')
    def test_aligned_not_autoapproved(self):
        r=check_comparability('S2','S5')
        self.assertEqual(r['status'],'metadata_aligned')
        self.assertTrue(r['requires_human_review'])
        self.assertFalse(r['can_pool'])
    def test_h3_traceability(self):
        h=get_hypothesis('H3')
        self.assertEqual(h['supporting'],['S5'])
        self.assertEqual(h['status'],'provisional_not_human_approved')
    def test_returned_data_not_mutable_store(self):
        get_source('S1')['source']['authorized']=False
        self.assertTrue(get_source('S1')['source']['authorized'])

if __name__=='__main__': unittest.main()
