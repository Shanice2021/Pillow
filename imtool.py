import sys
from PIL import Image

def resizeIMG(imgName):
    try:
        img = Image.open(imgName)
        print("Current size (width, height)", img.size)
    except FileNotFoundError as fnfe:
        print(fnfe)

def showMenu():
    print("**************")
    print('1.等比例縮放')
    print('2.圖片旋轉')
    print('3.產生縮圖')
    print('4.套用濾鏡')
    print('5.其他')
    print('*******************')


if __name__ =="__main__":
    if len(sys.argv)>1:
        showMenu()
        op = input("選擇功能:")
        if op == "1":
            resizeIMG(sys.argv[1])
    else:
        print("argument error!")