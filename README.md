# ml23_fmri_group_20a

class ReadObject:
  attribute     type
  [subject]                 string

  [image_data]:
                            dataframe         (5000, 135)

  [fmri]:
    key                     value
    'l'                     ndarray, float32  (5000, 19004)
    'r'                     ndarray, float32  (5000, 20544)
  
  [mask]:
    key                     value
    'lh.fsaverage_space'    ndarray, int64    (163842,)
    'rh.fsaverage_space'    ndarray, int64    (163842,)
    'lh.space'              ndarray, int64    (19004,)
    'rh.space'              ndarray, int64    (20544,)
    'mapping'               dictionary, int64 -> str

  [sample_data(index_list, mode)]:
    returns (N, 425, 425) or (N, 425, 425, 3) ndarray, representing N images.
    The index_list is a list representing the indices of the pictures in the batch. To seperate training batch and validation batch, make two complementary lists and seperately pass them to this function
  
