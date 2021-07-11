import os,glob

work_folder = input('作業フォルダ名？:')
#デスクトップ上の作業フォルダ指定

os.chdir('C:\\Users\\ASO-Scan03\\Desktop\\'+ work_folder)
# 作業フォルダに移動

stl_num = glob.glob('*.stl')
# 作業フォルダ内の'.stl'走査してPathリスト化

f = open(work_folder+'.txt','w')
#書き込みモードでテキストファイル生成

f.write(work_folder +'\n'+''+'\n')
#ファイル名だけ最上段に書き込み　改行

f.close()
#クローズ

f =open(work_folder+'.txt','a')
#追記モードで開く

for i in stl_num:
    f.write(i+'\n'+'\n')
#スキャンしたstl名を書き込む
#空欄改行

f.close()
#ファイルをクローズする