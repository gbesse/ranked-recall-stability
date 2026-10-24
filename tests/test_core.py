import unittest
from ranked_recall_stability import run
class Tests(unittest.TestCase):
 def side(self,ids,**kw):return {'bank_revision':'r','context_digest':'q','items':[{'id':x}for x in ids],**kw}
 def test_reversed_prefix_has_all_pair_inversions(self):
  r=run({'before':self.side('abc'),'after':self.side('cba'),'k':3});self.assertEqual(len(r['strict_pair_inversions']),3);self.assertEqual(r['jaccard'],1)
 def test_explicit_score_ties_are_not_unstable_preferences(self):
  a=self.side('ab');b=self.side('ba')
  for side in (a,b):
   for x in side['items']:x['score']=.5
  r=run({'before':a,'after':b});self.assertEqual(r['strict_pair_inversions'],[]);self.assertEqual(len(r['declared_score_ties_ignored']),1)
 def test_context_change_is_not_hidden(self):self.assertFalse(run({'before':self.side('a'),'after':self.side('a',bank_revision='changed')})['same_declared_context'])
 def test_topk_omission_not_called_recall_failure(self):
  r=run({'before':self.side('abc'),'after':self.side('bca'),'k':2});self.assertTrue(r['before_truncated']);self.assertEqual(r['only_before'],['a']);self.assertNotIn('recall',r)
