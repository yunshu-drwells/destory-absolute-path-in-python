import os
import re
import glob

def search_all_executable(cur_path):
    print("current path:", cur_path)
    # 搜索所有.exe文件
    files = glob.glob(cur_path+"/*.exe")
    return files
    
# 定义一个函数，接受一个文件名作为参数，读取文件后返回十六进制内容
def read_binary_file(filename):
    # 以二进制模式打开文件
    with open(filename, "rb") as f:
        # 获取文件大小
        size = os.path.getsize(filename)
        # 读取文件内容，返回一个字节对象
        data = f.read(size)
        # 将字节对象解码为ASCII字符串，忽略无法解码的字节
        # text = data.decode("ascii", errors="ignore")
        # 转化为十六进制
        text = data.hex()
        # 输出字符串到屏幕
        # print(type(text))
        return text


# 定义一个函数，接受一个文件名以及ASCII字符串作为参数，转化成二进制字节然后写入文件
def write_binary_file(filename, text):
    # 十六进制的字符串转化成二进制的字符串
    bin_str = bin(int(text, 16))
    # 将二进制的字符串转化成二进制的字节
    bin_num = int(bin_str, 2) # 二进制的整数 
    bin_bytes = bin_num.to_bytes((bin_num.bit_length() + 7) // 8, "big") # 二进制的字节 
    # print(bin_bytes) # 输出 b'\x1c'³ 
    # 打开一个文件，以写入模式
    with open(filename, "wb") as f:
        # 将二进制字符串写入文件中
        f.write(bin_bytes)
    # 打印提示信息
    print("alter ", filename, " down!")
   
# 正则替换
def re_replace(match):
    return match.group().replace(match.group(1), "")
    
def re_match_alter(text):
    # 定义一个正则表达式，匹配#!"f:\python3.9.0\python\python39\python.exe字符串
	# 22:" 65:e 78:x
    # #!(*:)python.exe
    # #!"(*:)python.exe"
    pattern0 = r'2321([0-9a-f]{2}3a5c.*)707974686f6e2e657865'
    pattern1 = r'232122([0-9a-f]{2}3a5c.*)707974686f6e2e65786522'    
    # pattern0 = r'#!"(.*)python.exe"'
    # pattern1 = r'#!(.*)python.exe'
    
            
    # 使用re.search方法，查找字符串中是否有匹配的子串
    match = re.search(pattern0, text)
    par_used = 0 # 记录是哪个正则匹配成功
    
    # 如果有匹配的子串，打印出来
    if not match:
        # 使用re.search方法，查找字符串中是否有匹配的子串
        match = re.search(pattern1, text)
        par_used = 1
    # print("Found a match:", match)
    # print("Found a match:", match.group(0))
    # print("Found a match:", match.group(1))
    
    # 按照匹配成功的正则去替换
    if match is not None:
        if par_used == 1:
            result = re.sub(pattern1, re_replace, text)
        else:
            result = re.sub(pattern0, re_replace, text)
        # print(result)
        return result
    return ""

        

if __name__ == '__main__':
    cur_path = os.getcwd()
    files = search_all_executable(cur_path)
    for file in files:
        print("processing: ", file)
        # 以ascii编码方式打开.exe文件并返回内容
        text = read_binary_file(file)
        # print(text)
        # 正则匹配并替换，然后返回结果
        result = re_match_alter(text)
        # 将结果覆盖写回文件
        if result != "":
            write_binary_file(file, result)
        else:
            print("do nothing ", file, " already satisfied!")
    input('Press Enter to exit…')
    
'''    
    string = '2321433A5C55736572735C41646D696E6973747261746F725C4465736B746F705C776869737065725C776869737065725C507974686F6E5C507974686F6E3331305C707974686F6E2E657865'
    pattern = r'2321(.*)707974686F6E2E657865'
    match = re.search(pattern, string)
    print(match)
    
    file = files[0]
    print("processing: ", file)
    # 以ascii编码方式打开.exe文件并返回内容
    text = read_binary_file(file)
    # print(text)
    # 正则匹配并替换，然后返回结果
    result = re_match_alter(text)
    # print(result)
    # # 将结果覆盖写回文件
    if result != "":
        write_binary_file(file, result)
        
'''    


