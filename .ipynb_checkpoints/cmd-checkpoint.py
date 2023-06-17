# Pythonでシェルコマンドを動かし、結果を取得する関数
# 参考 : https://qiita.com/inatatsu_csg/items/40b11701d256a84a0510 

def cmd(input=""):
    import subprocess    
    
    return (subprocess.Popen(input, 
                             stdout=subprocess.PIPE, shell=True
                            ).communicate()[0]).decode('utf-8')[:-1].split("\n")