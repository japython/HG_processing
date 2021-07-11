import os, glob, shutil, re, time

split_folder = input('作業フォルダ？:')

#path = os.path.join(r'\\192.168.0.248','qs','AA（大谷⇔CAD stl受け渡し用）','2F⇔7F_AAフォルダ',split_folder)
#デスクトップ上の作業フォルダは以下パスを使用する
path = os.path.join(r'C:\\Users','Iida_Tetsuya','Desktop',split_folder)

# 作業フォルダに移動
os.chdir(path)

# 作業フォルダ内の'.stl'をリスト化
stl_num = glob.glob('*/*.stl')

#サッポロ分をリストの先頭に持ってくる
for num, i in enumerate(stl_num):
    if '-S' in i:
    	#リスト位置[0]に挿入
        stl_num.insert(0,i)
        #元位置の要素を削除（上記「先頭挿入」とどういうタイミングで実施されるかで修検討）
        del stl_num[num]
    else:
        continue

print('処理stlファイル数:{}'.format(str(len(stl_num))))

stl_length = len(stl_num)

folder_split_num = len(stl_num) % 5

if folder_split_num == 0:
    #余りが出ない場合は5の倍数フォルダ作成数
    folder_split_num = len(stl_num) / 5
else:
    #余りが出る場合は5の倍数プラス1フォルダ数作成
    folder_split_num = (len(stl_num) / 5) + 1

#フォルダの日付とAMかPMかを決める
day=input('フォルダ名？:')


#遠し番号入りのフォルダを適正数作成
for i in range(int(folder_split_num)):
    os.mkdir(day + ' ' + str(i+1))

#stlリスト開始位置
n = 0

#上記リスト分割する個数
s = 5

#分割リスト格納用空リスト
stl_split_list=[]

#リストを指定した個数で分割していくループ処理
for i in stl_num:
    stl_split_list.append(stl_num[n:n+s:1])
    n += s
    #カウント数がリストの長さを超えたらループ終了
    if n >= stl_length:
        break

#5個づつ分割されたリストで各フォルダに移動
for i, x in enumerate(stl_split_list):
    for y in x:
        shutil.copy('./'+ y,'./'+ day + ' ' + str(i+1))

print('complete!')

time.sleep(3)