path = r'C:\Users\admin\Desktop\TestData.properties'

with open(path, 'r', encoding='UTF-8') as f:
    li = f.readlines()
with open(path, 'w', encoding='UTF-8') as w:
    for line in li:
        if line.startswith('en_us.common.common.connectbrowser.url.value'):
            w.write('en_us.common.common.connectbrowser.url.value = https:/12.12.12.12/ui/\n')
        else:
            w.write(line)
