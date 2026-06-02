MARS
Experiments on MARS, as it is the largest dataset available to date for video-based person reID. Please follow deep-person-reid to prepare the data. The instructions are copied here:

Create a directory named mars/.
Download dataset to mars/ from http://www.liangzheng.com.cn/Project/project_mars.html.
Extract bbox_train.zip and bbox_test.zip.
Download split information from https://github.com/liangzheng06/MARS-evaluation/tree/master/info and put info/ in data/mars (we want to follow the standard split in [8]). The data structure would look like:
Download mars_attributes.csv from http://irip.buaa.edu.cn/mars_duke_attributes/index.html, and put the file in data/mars. The data structure would look like:
mars/
    bbox_test/
    bbox_train/
    info/
    mars_attributes.csv
Change the global variable _C.DATASETS.ROOT_DIR to /path2mars/mars and _C.DATASETS.NAME to mars in config or configs.

Utilize V2E to generate the corresponding event sequence.

The event version of MARS is so large (almost 20,000 videos). In the following weeks, we will put our data in this link: https://pan.baidu.com/s/1jont6AXijx3bwLzeHblwnw password:y762

iLIDS-VID
Create a directory named ilids-vid/ under data/.

Download the dataset from http://www.eecs.qmul.ac.uk/~xiatian/downloads_qmul_iLIDS-VID_ReID_dataset.html to "ilids-vid".

Download the event sequence from: https://pan.baidu.com/s/19BgDlcbeKtt7EySNpD8gpw password：5jdg

Organize the data structure to match

ilids-vid/
    i-LIDS-VID/
    i-LIDS-VID—event/
    train-test people splits
PRID
Create a directory named PRID/ under data/.

Download the dataset and event sequence from: https://pan.baidu.com/s/13OTKjwcfbrQQDbDtPyEYRA password：5olr

Organize the data structure to match

PRID/
    prid_2011/
    prid_2011_event/
