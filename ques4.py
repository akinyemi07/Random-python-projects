#a program to print the even number of letter for a string 

st= "print every word in this sentence that has an even number of letters"

for num in st.split():
    if len(num) % 2 ==0 :
        print (num)


end =input("pleases press enter")

