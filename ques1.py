#a program that would print the words that start with s

st= "Print only the words that start with s in the sentence"
 
sl = st.split()

for val in sl:
    if val[0] == 's':
        print (val)

x= input("please press enter;")


