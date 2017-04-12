import matplotlib.pyplot as plt
from matplotlib._png import read_png
from matplotlib.pylab import Rectangle, gca
import os

os.chdir('/Users/u0107775/Data/GandT_Seq/161020_MariaXydia/GeneCoverage')

def main():
    ax = plt.subplot(111)
    ax.set_autoscaley_on(False)
    ax.set_autoscalex_on(False)
    ax.set_ylim([0,10])
    ax.set_xlim([0,10])

    list_of_corners = [left0, right0, bottom0, top0]
    list_of_images = ['AGGCAGAA-TCGACTAG.160812_Maria_Xydia_GandT.160902.HiSeq2500.FCA.lane5.gcap_16_04.R1.fastq.gz.avgprof.pdf',\
                      'AGGCAGAA-TCTCTCCG.160812_Maria_Xydia_GandT.160902.HiSeq2500.FCA.lane5.gcap_16_04.R1.fastq.gz.avgprof.pdf',\
                      'AGGCAGAA-TTATGCGA.160812_Maria_Xydia_GandT.160902.HiSeq2500.FCA.lane5.gcap_16_04.R1.fastq.gz.avgprof.pdf',\
                      'AGGCAGAA-TTCTAGCT.160812_Maria_Xydia_GandT.160902.HiSeq2500.FCA.lane5.gcap_16_04.R1.fastq.gz.avgprof.pdf']
    ax, fig = plt.subplots(1, 1)
    
    for extent, img in zip(list_of_corners, list_of_images):
        ax.imshow(img, extent=extent)

    plt.draw()
    plt.savefig('out.png', dpi=300)