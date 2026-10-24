import itertools
from .common import identifier,integer,number,unique_ids

def run(data):
 a=data['before'];b=data['after'];k=integer(data.get('k',10),1,1000)
 for side in (a,b):
  identifier(side['bank_revision']);identifier(side['context_digest']);unique_ids(side['items'])
  if len(side['items'])>1000:raise ValueError('count')
  for item in side['items']:
   if'score'in item:number(item['score'])
 left=a['items'][:k];right=b['items'][:k];A={r['id']:i for i,r in enumerate(left)};B={r['id']:i for i,r in enumerate(right)};common=sorted(A.keys()&B.keys());inversions=[];tied=[]
 for x,y in itertools.combinations(common,2):
  def tie(rows,index):return'score'in rows[index[x]]and'score'in rows[index[y]]and rows[index[x]]['score']==rows[index[y]]['score']
  if tie(left,A)or tie(right,B):tied.append([x,y]);continue
  if(A[x]-A[y])*(B[x]-B[y])<0:inversions.append([x,y])
 comparable=a['bank_revision']==b['bank_revision']and a['context_digest']==b['context_digest']
 return {'same_declared_context':comparable,'common_ids':common,'only_before':sorted(A.keys()-B.keys()),'only_after':sorted(B.keys()-A.keys()),'jaccard':len(common)/len(A.keys()|B.keys())if A or B else 1,'strict_pair_inversions':inversions,'declared_score_ties_ignored':tied,'before_truncated':len(a['items'])>k,'after_truncated':len(b['items'])>k,'model':'captured_prefix_rank_stability_not_recall_accuracy_or_memory_truth'}
