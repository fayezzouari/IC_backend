import sort_items

def cleanse(ch): #ch is the string of the number
    res= sort_items.sorted_items("values")
    res_list=list(res)
    latest_value= res[res_list[len(res_list)-1]]['Value']
    res=latest_value
    while True:
        if len(ch)!=len(latest_value):
            if len(ch)<len(latest_value):
                latest_value=latest_value[(len(latest_value)-len(ch)):len(latest_value)]
            else:
                ch=ch[(len(ch)-len(latest_value)):len(ch)]
        else: 
            if (int(ch)-int(latest_value))<0 or (int(ch)-int(latest_value))>500:
                ch=ch[1:len(ch)]
                latest_value=latest_value[1:len(latest_value)]       
            else:
                break
        
    return (int(ch)-int(latest_value))+int(res)


if __name__=='__main__':
    print(cleanse("1111175"))