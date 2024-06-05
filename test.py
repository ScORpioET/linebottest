# 中文字符串
chinese_string = "哈囉 大家好. 我是"

# 將字符串編碼成 unicode 編碼
unicode_encoded = chinese_string.encode('unicode_escape')

# 轉換為字符串表示形式
unicode_string = unicode_encoded.decode('ascii')

print(unicode_string)
