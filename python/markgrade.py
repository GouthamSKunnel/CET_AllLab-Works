m1=int(input("enter marl of 1st subject"))
m2=int(input("enter mark of 2nd subject"))
m3=int(input("mark of 3rd subject"))

sum=(m1+m2+m3)
avg=sum/3;

if avg>=90:
    print("Total mark = ",sum," and grade = A with an avg of ",avg);
elif avg<90 and avg>=70 :
    print("Total mark = ",sum," and grade = B with an avg of ",avg);
elif avg < 70 and avg >=40:
    print("Total mark = ",sum," and grade = C with an avg of ",avg);
elif avg <40:
    print("Total mark = ",sum," and grade = F with an avg of ",avg);
