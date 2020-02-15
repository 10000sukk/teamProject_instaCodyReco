import os
import sys
import Cloth_detector

cody_path="D:\\realcody\\"
ootd=os.listdir(cody_path)
for files in ootd:
    try:
        Cloth_detector.recommend_fs(cody_path+files,0)
        print(cody_path+files)
    
    except KeyboardInterrupt:
        # Ctrl+C 입력시 예외 발생
        sys.exit()
    except:
        pass
