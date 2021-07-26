def user_info(name):
   if name =="john":
        return {"name":"john","age":25,"Profession":"Teaching", "salary":"35000"}
   elif name =="joe":
        return {"name":"joe","age":28,"Profession":"Developer","salary":"30000"} 
   elif name =="puja":
        return {"name":"puja","age":29,"Profession":"Doctor","salary":"78000"}
   else:
        return "No data found...!"

while True:
    data = input("Enter the names: ").strip()
    print(data)
    if data=='exit':
        break 
    info = user_info(data)
    print(info)