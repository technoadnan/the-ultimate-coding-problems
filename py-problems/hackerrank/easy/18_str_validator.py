def count_substring(string, sub_string):
    sub = []
    st = []
    for k in sub_string:
        sub.append(k)
    for j in range(string):
        st.append(j)
    print(sub)
        
    return 

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)