def main():
    d = {'1001': '林双', '1002': '顾许', '2007': '卫明', '1880': '米雪'}
    for key in list(d.keys()):
        if (int(key)%2==0):
            del d[key]
    print(d)
if __name__ =='__main__':
    main()
