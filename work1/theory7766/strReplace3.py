def main():
    s = input('s=')
    if 'ol' in s:
        s1=s.replace("ol", "fzu", len(s))
    print(s1[::-1])
    return
if __name__=='__main__':
    main()