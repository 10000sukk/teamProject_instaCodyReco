import os
import sys
import color_detector
import save_csv
import shutil
import reco
#이 파일은 darknet.exe가 설치된 경로에 위치해야함

# os가 윈도우일때 command, 다른 os의 경우 comm 수정 필요
# 각 path마다 뒤에 " "(공백) 필수
#target_img="D:\\cody\\cody(1130)_112.jpg "
#cody_path="D:\\realcody\\"
#ootd=os.listdir(cody_path)
def recommend_fs(path,mode):
    target_img=path+" "

    cate_data=".\\data\\category.data "
    cate_cfg=".\\cfg\\yolov3-tiny-category.cfg "
    cate_weights=".\\backup\\yolov3-tiny-category_7000.weights "

    pattern_data=".\\data\\pattern.data "
    pattern_cfg=".\\cfg\\yolov3-tiny-pattern.cfg "
    pattern_weights=".\\backup\\yolov3-tiny-pattern_15000.weights "


    category_comm=".\\darknet.exe detector test " + cate_data + cate_cfg + cate_weights + target_img + "-gpu 0,1"

    f=open("feature_map.txt","w")
    f.close()
    # 카테고리 분류 실행
    if os.system(category_comm):
        raise RuntimeError('Category Classifing failed!')

    file = os.listdir(".\\result_img\\")
    if len(file)>1:
        print('result_img/ : More than 1 image')
        shutil.rmtree('result_img\\')
        os.mkdir("result_img")
    category=file[0].split("_")[4].rstrip(".jpg")

    f=open("feature_map.txt","w")
    f.close()

    #아래부터는 detected crop image를 사용

    #RGB 컬러코드 추출
    color_code=color_detector.detect("result_img\\"+file[0])
    target_img=".\\result_img\\"+file[0]+" "
    pattern_comm=".\\darknet.exe detector test " + pattern_data + pattern_cfg + pattern_weights + target_img + "-gpu 0,1"

    # 패턴 분류 실행
    if os.system(pattern_comm):
        raise RuntimeError('Pattern Classifing failed!')
    os.remove("result_img\\"+file[0])
    file = os.listdir(".\\result_img\\")
    if len(file)>1:
        print('################### result_img/ : More than 1 image ###############')
        
    pattern=file[0].split("_")[4].rstrip(".jpg")
    #패턴 확인후 파일 label 파일 삭제

    os.remove("result_img\\"+file[0])
    #타겟 crop이미지 삭제

    f=open("feature_map.txt","r")
    feature_map=f.readline()
    f.close()
    f=open("feature_map.txt","w")
    f.close()
    feature_map=feature_map.rstrip(" ").split(" ")
    feature_map=[float(i) for i in feature_map]

    print("===================결과===================")
    print("Pattern : "+pattern)
    print("Category : "+category)
    print("Color : ",color_code)
    print("Feature : ",feature_map)
    print("==========================================")
    
    if mode==0:
        save_csv.addCSV(category,pattern,color_code,feature_map,path)
    else:
        reco.recomend(category,pattern,color_code,feature_map,"dataset")
