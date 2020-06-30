#4. Write a program to construct a dictionary from the two lists containing the names of 
# students and their corresponding subjects. The dictionary should maps the students with
# their respective subjects. Let’s see how to do this using for loops and dictionary 
# comprehension. HINT-Use Zip function also
#● Student = [&#39;Smit&#39;, &#39;Jaya&#39;, &#39;Rayyan&#39;]
#● capital = [&#39;CSE&#39;, &#39;Networking&#39;, &#39;Operating System&#39;]

students = ["Smit", "Jaya", "Rayyan"] 
capital = ["CSE","Networking", "Operating System"]

print ("key= " + str(students)) 
print ("value= " + str(capital)) 

result = dict(zip(students, capital)) 
print ("Result = " +  str(result))