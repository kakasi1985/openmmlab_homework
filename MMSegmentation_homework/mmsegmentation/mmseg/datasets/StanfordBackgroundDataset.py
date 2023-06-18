from mmseg.registry import DATASETS
from mmseg.datasets import BaseSegDataset

# 数据集图片和标注路径
data_root = 'data/Watermelon87_Semantic_Seg_Mask'

# 类别和对应的颜色
classes = ('background','watermelon_edge', 'watermelon_peel','Watermelon_pulp','watermelon_seed_white','watermelon_seed_black')
palette = [[0,0,0],[255,255,255],[0,255,0],[255,0,0],[0,0,255],[128,128,128]]

@DATASETS.register_module()
class StanfordBackgroundDataset(BaseSegDataset):
  METAINFO = dict(classes = classes, palette = palette)
  def __init__(self, **kwargs):
    super().__init__(img_suffix='.jpg', seg_map_suffix='.png', **kwargs)