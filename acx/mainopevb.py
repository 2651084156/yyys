import glob
import os
import random
import shutil
import sys
import time
# import cv2
import zipfile

from PIL import Image

# print (glob.glob(r"*\**\*.png"))
from tqdm import tqdm
import cv2

b=''
in_Dat = './list12'
n =0
# ap = os.listdir(c)
# shutil.rmtree('./tmp')
# os.mkdir('./tmp')
# if not os.path.exists(b):  # 判断当前路径是否存在，没有则创建new文件夹
#     os.makedirs(b)
fbpx =128


def zipDir(dirpath, outFullName):
    """
    压缩指定文件夹
    :param dirpath: 目标文件夹路径
    :param outFullName: 压缩文件保存路径+xxxx.zip
    :return: 无
    """
    zip = zipfile.ZipFile(outFullName, "w", zipfile.ZIP_DEFLATED)
    for path, dirnames, filenames in os.walk(dirpath):
        # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
        fpath = path.replace(dirpath, '')

        for filename in tqdm(filenames):
            zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
    zip.close()
def inout(file_in, file_out):
    img = Image.open(file_in)
    out =img
    out.save(file_out)
def ResizeImage(file_in, file_out,w):
    """
    改变图片分辨率
    :param file_in: 输入图片
    :param file_out: 输出图片
    :param w: 输出图片宽
    :param h: 输出图片高
    """
    h =w
    # img = Image.open(file_in)
    #输出图片指定宽高
    # out = img.resize((w, h), Image.ANTIALIAS)
    # 第二个参数：
    # Image.NEAREST ：低质量
    # Image.BILINEAR：双线性
    # Image.BICUBIC ：三次样条插值
    # Image.ANTIALIAS：高质量
    # out.save(file_out)
    pic = cv2.imread(file_in, cv2.IMREAD_UNCHANGED)
    pic_n = cv2.resize(pic, (h, h))
    # pic_name = i
    cv2.imwrite(file_out, pic_n)
def make_tmp(path):
    global b
    global n
    if n >=10:
        exit('主程序错误')
    if not os.path.exists(path):  # 判断当前路径是否存在，没有则创建new文件夹
        os.makedirs(path)
        b=path
    else:
        a12 = path + str(random.randint(0,1000))
        # a12 = path
        n = n+1
        make_tmp(a12)
# make_tmp('./tmp')
# print(b)
def mains():
    nmm = 0
    cdd = '''选择版本:(键入选项前数字)
    1  ， 1.12.2 
    2 ， 1.16.5
    3 , 生成全部组合的zip   
        '''
    print(cdd)
    cds1 =''
    cdd1 = '''选择版本:(键入选项前数字)
        1  ， forge (1.16.5)
        2 ， fb  (1.16.5)
            '''

    while True:
        inbb = input('请输入:\n')
        cds = str(inbb)
        if cds == '1':
            print('选择mc版本1.12.2')
            break
        elif cds == '2':
            print('选择mc版本1.16.5 ')
            print(cdd1)

            while True:
                fbfo = input('请输入:\n')
                cds1 = str(fbfo)
                if cds1 == '1':
                    print('选择forge')
                    break
                elif cds1 == '2':
                    print('选择fb')
                    break

                else:
                    print('无效输入，请重新输入')
            break
        elif cds == '3':
            print('全部 确定')
            nmm = 1
            break
        else:
            print('无效输入，请重新输入')
    cdfs =''
    global fbpx
    while True:
        if nmm == 1:
            break

        print('''
    选择分辨率:(键入选项前数字)
    1 , 2048
    2 , 1024
    3 , 512
    4 , 256
    5 , 128
    6 , 64
    7 , 自定义 自行输入数字


                ''')
        ins = input('选择：')
        cdfs = str(ins)
        if cdfs == '1':
            print('选择2048')
            fbpx =2048
            break
        elif cdfs == '2':
            print('选择1024')
            fbpx = 1024
            break
        elif cdfs == '3':
            print('选择512')
            fbpx = 512
            break

        elif cdfs == '4':
            print('选择256')
            fbpx = 256
            break
        elif cdfs == '5':
            print('选择128')
            fbpx = 128
            break

        elif cdfs == '6':
            print('选择64')
            fbpx = 64
            break
        elif cdfs == '7':
            print('自定义')
            fbpx = int(input('输入自定义'))
            break
        else:
            print('无效输入，请重新输入')
    return {'1':nmm,'2':cds,'3':cds1,'4':cdfs} # 1 -是否是全部 2- 游戏版本 3-fo/fb 4- 分辨率

def make1_12_2():
    cds = os.listdir('./list12/1.12/minecraft')
    # cds = os.walk('./list12/1.12')
    # list(cds)
    # print(cds)
    # for i in cds:
    #     print(1)
    in11 = './list12/1.12/minecraft/'
    # print(cds)
    if 'blockstates' in cds:
        try:
            # shutil.copy2(in11, b)
            shutil.copytree(in11, c)
            # time.sleep(3)
            # shutil.rmtree(b + '/',False)
            # print(b)

            # os.system('rmdir /s/q ' +b.replace('./',''))
        except IOError as e:
            print("Unable to copy file. %s" % e)
            exit('主程序错误')
        except:
            print("Unexpected error:", sys.exc_info())
            exit('主程序错误')

        if os.path.exists(b + '/tmp/textures/blocks'):  # 判断当前路径是否存在，没有则创建new文件夹
            # print(b.replace('./','')+'/tmp/textures/blocks')
            # print('rmdir /s/q ' +b+'/tmp/textures/blocks')
            os.system('rmdir /s/q ' + b.replace('/', '\\') + '/tmp/textures/blocks'.replace('/', '\\'))
            os.makedirs(b + '/tmp/textures/blocks')
        if os.path.exists(b + '/tmp/textures/items'):  # 判断当前路径是否存在，没有则创建new文件夹
            os.system('rmdir /s/q ' + b.replace('/', '\\') + '/tmp/textures/items'.replace('/', '\\'))
            os.makedirs(b + '/tmp/textures/items')
        if os.path.exists(b + '/tmp/mcpatcher/ctm'):  # 判断当前路径是否存在，没有则创建new文件夹
            os.system('rmdir /s/q ' + b.replace('/', '\\') + '/tmp/mcpatcher/ctm'.replace('/', '\\'))
            os.makedirs(b + '/tmp/mcpatcher/ctm')
        # if not os.path.exists(b):  # 判断当前路径是否存在，没有则创建new文件夹

        # print(tuple(os.walk('./list12/1.12/minecraft/textures/blocks')))
        ades = tuple(os.walk('./list12/1.12/minecraft/textures/blocks'))
        for i in tqdm(ades[0][2]):

            if 'bookshelf.png' == i:
                inout(ades[0][0] + '/bookshelf.png', b + '/tmp/textures/blocks/' + i)
                # print(i[-4:])
                continue
            if i[-4:] == '.png':
                # print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
                # inout('./list12/1.12/minecraft/textures/blocks'+'/bookshelf.png',)
                ResizeImage(ades[0][0] + '/' + i, b + '/tmp/textures/blocks/' + i, fbpx)
                continue
            # ResizeImage
        for i in tqdm(ades[0][1]):
            ccc = tuple(os.walk('./list12/1.12/minecraft/textures/blocks/' + i))
            if not os.path.exists(b + '/tmp/textures/blocks/' + i + '/'):  # 判断当前路径是否存在，没有则创建new文件夹
                os.makedirs(b + '/tmp/textures/blocks/' + i + '/')
            for j in tqdm(ccc[0][2]):
                ResizeImage(ccc[0][0] + '/' + j, b + '/tmp/textures/blocks/' + i + '/' + j, fbpx)
        # print(os.listdir('./list12/1.12/minecraft/textures/items'))
        ades1 = os.listdir('./list12/1.12/minecraft/textures/items')
        for i in tqdm(ades1):
            cfdas = './list12/1.12/minecraft/textures/items/' + i
            if i[-4:] == '.png':
                # print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
                # inout('./list12/1.12/minecraft/textures/blocks'+'/bookshelf.png',)
                ResizeImage(cfdas, b + '/tmp/textures/items/' + i, fbpx)
        # print(tuple(os.walk('./list12/1.12/minecraft/textures/blocks')))
        ades2 = tuple(os.walk('./list12/1.12/minecraft/mcpatcher/ctm'))
        for i in tqdm(ades2[0][1]):
            ccc = tuple(os.walk('./list12/1.12/minecraft/mcpatcher/ctm/' + i))
            if not os.path.exists(b + '/tmp/mcpatcher/ctm/' + i + '/'):  # 判断当前路径是否存在，没有则创建new文件夹
                os.makedirs(b + '/tmp/mcpatcher/ctm/' + i + '/')
            for j in tqdm(ccc[0][2]):
                if j[-4:] == '.png':
                    ResizeImage(ccc[0][0] + '/' + j, b + '/tmp/mcpatcher/ctm/' + i + '/' + j, fbpx)
                else:
                    with open(ccc[0][0] + '/' + j,'rb') as f:
                        c43=f.read()
                        with open(b + '/tmp/mcpatcher/ctm/' + i + '/' + j,'wb') as f2:
                            f2.write(c43)
    in12 = r'.\list12\fo\1.12'
    acds = b+'/tmp2/'
    try:
        # shutil.copy2(in11, b)
        shutil.copytree(in12, acds)
        # time.sleep(3)
        # shutil.rmtree(b + '/',False)
        # print(b)

        # os.system('rmdir /s/q ' +b.replace('./',''))
    except IOError as e:
        print("Unable to copy file. %s" % e)
        exit('主程序错误')
    except:
        print("Unexpected error:", sys.exc_info())
        exit('主程序错误')
    osin ='./list12/textures/blocks'
    lidss = os.listdir(osin)
    for i in tqdm(lidss):
        cdfr = osin +'/'+i
        if not os.path.exists(acds+'textures/blocks/'):  # 判断当前路径是否存在，没有则创建new文件夹
            os.makedirs(acds+'textures/blocks/')
        # ResizeImage(cdfr,acds+'textures/blocks/'+i,fbpx)
        if i[-4:] == '.png':
            ResizeImage(cdfr,acds+'textures/blocks/'+i,fbpx)
        else:
            with open(cdfr, 'rb') as f:
                c43 = f.read()
                with open(acds+'textures/blocks/'+i, 'wb') as f2:
                    f2.write(c43)
    tmp3 =b+'/tmp3/'
    if not os.path.exists(tmp3):  # 判断当前路径是否存在，没有则创建new文件夹
        os.makedirs(tmp3)
    os.makedirs(tmp3+'/assets/')
    # os.makedirs(tmp3+'/assets/minecraft')
    # os.makedirs(tmp3+'/assets/tmeov')

    with open('./list12/pack.png','rb') as ff:
        ffffr=ff.read()
        with open(tmp3+'pack.png', 'wb') as fff:
            fff.write(ffffr)
    with open(tmp3+'pack.mcmeta', 'w',encoding='utf8') as ff:
        ff.write(r'''{
  "pack": {
    "pack_format": 3,
    "description": " 抖音B站搜索\u00A7dTMEO \u00A76{**-**}×-1.12[严禁倒卖] 作者求赞助\u00A7e\u00A7nhttps://afdian.net/@TMEO123/"
  }
}
'''.replace('{**-**}',str(fbpx)))
    with open(tmp3 + '/assets/.mcassetsroot', 'wb') as fff:
        fff.write(b'')
    shutil.copytree(b+'/tmp/', tmp3+'/assets/minecraft/')
    shutil.copytree(b + '/tmp2/', tmp3 + '/assets/tmeov')
    zipDir(tmp3, './out/1.12.2-forge-'+str(fbpx)+'x'+'.zip')
    os.system('rmdir /s/q ' + b.replace('/', '\\') )

def g1_16_5yb():
    cds = os.listdir('./list12/1.16/minecraft')
    # cds = os.walk('./list12/1.12')
    # list(cds)
    # print(cds)
    # for i in cds:
    #     print(1)
    in11 = './list12/1.16/minecraft/'
    # print(cds)
    if 'blockstates' in cds:
        try:
            # shutil.copy2(in11, b)
            shutil.copytree(in11, c)
            # time.sleep(3)
            # shutil.rmtree(b + '/',False)
            # print(b)

            # os.system('rmdir /s/q ' +b.replace('./',''))
        except IOError as e:
            print("Unable to copy file. %s" % e)
            exit('主程序错误')
        except:
            print("Unexpected error:", sys.exc_info())
            exit('主程序错误')

        if os.path.exists(b + '/tmp/textures/blocks'):  # 判断当前路径是否存在，没有则创建new文件夹
            # print(b.replace('./','')+'/tmp/textures/blocks')
            # print('rmdir /s/q ' +b+'/tmp/textures/blocks')
            os.system('rmdir /s/q ' + b.replace('/', '\\') + '/tmp/textures/blocks'.replace('/', '\\'))
            os.makedirs(b + '/tmp/textures/blocks')
        if os.path.exists(b + '/tmp/textures/items'):  # 判断当前路径是否存在，没有则创建new文件夹
            os.system('rmdir /s/q ' + b.replace('/', '\\') + '/tmp/textures/items'.replace('/', '\\'))
            os.makedirs(b + '/tmp/textures/items')
        if os.path.exists(b + '/tmp/optifine/ctm'):  # 判断当前路径是否存在，没有则创建new文件夹
            os.system('rmdir /s/q ' + b.replace('/', '\\') + '/tmp/optifine/ctm'.replace('/', '\\'))
            os.makedirs(b + '/tmp/optifine/ctm')
        # if not os.path.exists(b):  # 判断当前路径是否存在，没有则创建new文件夹

        # print(tuple(os.walk('./list12/1.16/minecraft/textures/block')))
        ades = tuple(os.walk('./list12/1.16/minecraft/textures/block'))

        for i in tqdm(ades[0][2]):

            if 'bookshelf.png' == i:
                inout(ades[0][0] + '/bookshelf.png', b + '/tmp/textures/block/' + i)
                # print(i[-4:])
                continue
            if i[-4:] == '.png':
                # print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
                # inout('./list12/1.12/minecraft/textures/blocks'+'/bookshelf.png',)
                ResizeImage(ades[0][0] + '/' + i, b + '/tmp/textures/block/' + i, fbpx)
                continue
            # ResizeImage
        for i in tqdm(ades[0][1]):
            ccc = tuple(os.walk('./list12/1.16/minecraft/textures/block/' + i))
            if not os.path.exists(b + '/tmp/textures/block/' + i + '/'):  # 判断当前路径是否存在，没有则创建new文件夹
                os.makedirs(b + '/tmp/textures/blocks/' + i + '/')
            for j in tqdm(ccc[0][2]):
                ResizeImage(ccc[0][0] + '/' + j, b + '/tmp/textures/block/' + i + '/' + j, fbpx)
        # print(os.listdir('./list12/1.16/minecraft/textures/item'))
        ades1 = os.listdir('./list12/1.16/minecraft/textures/item')
        for i in tqdm(ades1):
            cfdas = './list12/1.16/minecraft/textures/item/' + i
            if i[-4:] == '.png':
                # print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
                # inout('./list12/1.12/minecraft/textures/blocks'+'/bookshelf.png',)
                ResizeImage(cfdas, b + '/tmp/textures/item/' + i, fbpx)
        # print(tuple(os.walk('./list12/1.16/minecraft/textures/block')))
        ades2 = tuple(os.walk('./list12/1.16/minecraft/optifine/ctm'))
        for i in tqdm(ades2[0][1]):
            ccc = tuple(os.walk('./list12/1.16/minecraft/optifine/ctm/' + i))
            if not os.path.exists(b + '/tmp/optifine/ctm/' + i + '/'):  # 判断当前路径是否存在，没有则创建new文件夹
                os.makedirs(b + '/tmp/optifine/ctm/' + i + '/')
            for j in tqdm(ccc[0][2]):
                if j[-4:] == '.png':
                    ResizeImage(ccc[0][0] + '/' + j, b + '/tmp/optifine/ctm/' + i + '/' + j, fbpx)
                else:
                    with open(ccc[0][0] + '/' + j, 'rb') as f:
                        c43 = f.read()
                        with open(b + '/tmp/optifine/ctm/' + i + '/' + j, 'wb') as f2:
                            f2.write(c43)
def make1_16_5_forge():
    g1_16_5yb()
    in12 = r'.\list12\fo\1.16'
    acds = b + '/tmp2/'
    try:
        # shutil.copy2(in11, b)
        shutil.copytree(in12, acds)
        # time.sleep(3)
        # shutil.rmtree(b + '/',False)
        # print(b)

        # os.system('rmdir /s/q ' +b.replace('./',''))
    except IOError as e:
        print("Unable to copy file. %s" % e)
        exit('主程序错误')
    except:
        print("Unexpected error:", sys.exc_info())
        exit('主程序错误')
    osin = './list12/textures/blocks'
    lidss = os.listdir(osin)
    for i in tqdm(lidss):
        cdfr = osin + '/' + i
        if not os.path.exists(acds + 'textures/blocks/'):  # 判断当前路径是否存在，没有则创建new文件夹
            os.makedirs(acds + 'textures/blocks/')
        # ResizeImage(cdfr,acds+'textures/blocks/'+i,fbpx)
        if i[-4:] == '.png':
            ResizeImage(cdfr, acds + 'textures/blocks/' + i, fbpx)
        else:
            with open(cdfr, 'rb') as f:
                c43 = f.read()
                with open(acds + 'textures/blocks/' + i, 'wb') as f2:
                    f2.write(c43)
    tmp3 = b + '/tmp3/'
    if not os.path.exists(tmp3):  # 判断当前路径是否存在，没有则创建new文件夹
        os.makedirs(tmp3)
    os.makedirs(tmp3 + '/assets/')
    # os.makedirs(tmp3+'/assets/minecraft')
    # os.makedirs(tmp3+'/assets/tmeov')

    with open('./list12/pack.png', 'rb') as ff:
        ffffr = ff.read()
        with open(tmp3 + 'pack.png', 'wb') as fff:
            fff.write(ffffr)
    with open(tmp3 + 'pack.mcmeta', 'w', encoding='utf8') as ff:
        ff.write(r'''{
  "pack": {
    "pack_format": 6,
    "description": "抖音B站\u00A7dTMEO\u00A76{***-**}×-1.16[严禁倒卖]作者求赞助\u00A7e\u00A7nafdian.net/@TMEO123/"
  }
}

    '''.replace('{***-**}', str(fbpx)))
    # with open(tmp3 + '/assets/.mcassetsroot', 'wb') as fff:
    #     fff.write(b'')
    shutil.copytree(b + '/tmp/', tmp3 + '/assets/minecraft/')
    shutil.copytree(b + '/tmp2/', tmp3 + '/assets/tmeov')
    zipDir(tmp3, './out/1.16.5-forge-' + str(fbpx) + 'x' + '.zip')
    os.system('rmdir /s/q ' + b.replace('/', '\\'))

def make1_16_5_fb():
    g1_16_5yb()
    in12 = r'.\list12\fb\1.16'
    acds = b + '/tmp2/'
    try:
        # shutil.copy2(in11, b)
        shutil.copytree(in12, acds)
        # time.sleep(3)
        # shutil.rmtree(b + '/',False)
        # print(b)

        # os.system('rmdir /s/q ' +b.replace('./',''))
    except IOError as e:
        print("Unable to copy file. %s" % e)
        exit('主程序错误')
    except:
        print("Unexpected error:", sys.exc_info())
        exit('主程序错误')
    osin = './list12/textures/blocks'
    lidss = os.listdir(osin)
    for i in tqdm(lidss):
        cdfr = osin + '/' + i
        if not os.path.exists(acds + 'textures/blocks/'):  # 判断当前路径是否存在，没有则创建new文件夹
            os.makedirs(acds + 'textures/blocks/')
        # ResizeImage(cdfr,acds+'textures/blocks/'+i,fbpx)
        if i[-4:] == '.png':
            ResizeImage(cdfr, acds + 'textures/blocks/' + i, fbpx)
        else:
            with open(cdfr, 'rb') as f:
                c43 = f.read()
                with open(acds + 'textures/blocks/' + i, 'wb') as f2:
                    f2.write(c43)
    tmp3 = b + '/tmp3/'
    if not os.path.exists(tmp3):  # 判断当前路径是否存在，没有则创建new文件夹
        os.makedirs(tmp3)
    os.makedirs(tmp3 + '/assets/')
    # os.makedirs(tmp3+'/assets/minecraft')
    # os.makedirs(tmp3+'/assets/tmeov')

    with open('./list12/pack.png', 'rb') as ff:
        ffffr = ff.read()
        with open(tmp3 + 'pack.png', 'wb') as fff:
            fff.write(ffffr)
    with open(tmp3 + 'pack.mcmeta', 'w', encoding='utf8') as ff:
        ff.write(r'''{
      "pack": {
        "pack_format": 6,
        "description": "抖音B站\u00A7dTMEO\u00A76{***-**}×-1.16[严禁倒卖]作者求赞助\u00A7e\u00A7nafdian.net/@TMEO123/"
      }
    }

        '''.replace('{***-**}', str(fbpx)))
    # with open(tmp3 + '/assets/.mcassetsroot', 'wb') as fff:
    #     fff.write(b'')
    shutil.copytree(b + '/tmp/', tmp3 + '/assets/minecraft/')
    shutil.copytree(b + '/tmp2/', tmp3 + '/assets/fabric_tmeo')
    zipDir(tmp3, './out/1.16.5-fabric-' + str(fbpx) + 'x' + '.zip')
    os.system('rmdir /s/q ' + b.replace('/', '\\'))

if __name__ == '__main__':
    print('任意键以开始:')
    input('输入后需要回车:\n')
    cd =mains()
    print(cd)
    # if cd['1'] == 0:
    print('信息确认完成')

    if cd['1'] == 0:
        make_tmp('./tmp')
        c = b + '/tmp/'
        if cd['2'] == '1':
            make1_12_2()
            # zipDir(c,'zipx.zip')
        if cd['2'] == '2':
            if cd['3'] == '1': #for
                make1_16_5_forge()
            if cd['3'] == '2':#fb
                make1_16_5_fb()
    if cd['1'] == 1:
        dddsc =[2048,1024,512,256,128,64]
        for i in tqdm(dddsc):
            fbpx =i
            make_tmp('./tmp')
            c = b + '/tmp/'
            make1_12_2()

        for i in tqdm(dddsc):
            fbpx =i
            make_tmp('./tmp')
            c = b + '/tmp/'

            make1_16_5_forge()

        for i in tqdm(dddsc):
            fbpx =i
            make_tmp('./tmp')
            c = b + '/tmp/'


            make1_16_5_fb()

    print('程序运行完成')
    print('程序运行完成')
    print('程序运行完成')
    print('程序运行完成')
    print('程序运行完成')
    print('程序运行完成')
    print('程序运行完成')
    print('程序运行完成')
    print('程序运行完成')
    print('程序运行完成')
    time.sleep(1)
    print('程序运行完成')
    print('现在你可以安全的关闭窗口或者100s之后自动关')
    print('现在你可以安全的关闭窗口或者100s之后自动关')
    print('现在你可以安全的关闭窗口或者100s之后自动关')
    print('现在你可以安全的关闭窗口或者100s之后自动关')
    print('现在你可以安全的关闭窗口或者100s之后自动关')
    print('现在你可以安全的关闭窗口或者100s之后自动关')
    print('现在你可以安全的关闭窗口或者100s之后自动关')


    time.sleep(100)
    print(' 程序关闭\n程序关闭')
    time.sleep(10)











