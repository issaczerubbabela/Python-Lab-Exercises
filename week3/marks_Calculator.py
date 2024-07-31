def func(marks):
    total = sum(marks)
    mean = total/len(marks)
    grade = 'f' if mean < 50 else 'c' if mean <70 else 'b' if mean<90 else 'a'
    return mean, grade
marks = [int(items) for items in input('enter marks').split()]
mean, grade = func(marks)
print('the mean marks is ', mean)
print('the mean grade is ', grade)
