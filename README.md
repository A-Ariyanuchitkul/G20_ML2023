# ml23_fmri_group_20a

class ReadObject:
  attribute     type (value if dict)    size                        description
  subject       string                                              indicating which subject is being tested
  images        ndarray, uint8          (5000: (425, 425, 3))       pictures stored as RGB. the key is image name
  image_data    dataframe               (5000, 135)                 indicate what is in the picture.
  fmri          dictionary              (2: (5000, -))              fmri result. the key is "l" or "r". the - dimensions matches spaces masks
  masks         dictionary              depending on the key        masks. The keys are 'lh.fsaverage_space', 'rh.fsaverage_space', 'lh_space', 'rh_space', which maps to an int; and a dictionary mapping an int to a string, indicating the region.

