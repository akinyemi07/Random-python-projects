#program to print fist letter using list comprehension

st= "create a list of first letter of every word in this string"

lst=[st.split()[0] for num in st.split()]

print(lst)

