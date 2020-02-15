import numpy as np
import struct
from PIL import Image
import scipy
import scipy.misc
import scipy.cluster
import codecs
import binascii
def detect(path):
  NUM_CLUSTERS = 5

  print("reading image")
  im = Image.open(path)
  im = im.resize((150, 150))      # optional, to reduce time
  ar = np.asarray(im)
  shape = ar.shape
  ar = ar.reshape(scipy.product(shape[:2]), shape[2])
  ar=ar.astype('float')
  print(ar)
  print('finding clusters')
  codes, dist = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)
  print('cluster centres:\n', codes)

  vecs, dist = scipy.cluster.vq.vq(ar, codes)         # assign codes
  counts, bins = scipy.histogram(vecs, len(codes))    # count occurrences

  index_max = scipy.argmax(counts)                    # find most frequent
  peak = codes[index_max]
  peak=peak.astype('int')
  print("hi")
  colour=[0,0,0]
  for i,c in enumerate(peak):
    colour[i]=format(c,'x')
  colour=''.join(colour)
  print(colour)
  print('most frequent is %s (#%s)' % (peak, colour))
  print("peak")
  print(peak)
  return peak
