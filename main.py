import numpy as np

sales = np.array([
    [100, 150, 200],
    [120, 130, 180],
    [90, 160, 210]
])

rows,columns = sales.shape # rows days, columns products

total_sales= np.sum(sales)
max_sales = np.max(sales)
min_sales = np.min(sales)
avg_sales = np.mean(sales)

print("Total Sales",total_sales)
print("Highest Sale",max_sales)
print("Lowest Sale",min_sales)
print(f"Avg Sale {avg_sales:.2f}")

print("Total sales per day:", np.sum(sales,axis=1))


scores = np.array([
    [80, 90, 70], # example of one result per row 80+90+70 =  240
    [60, 75, 85],
    [95, 88, 92],
    [89, 78, 100]
]) # example of one result per column 80+60+95+89 = 324

students,subjects = scores.shape # rows = students, columns = subjects.

print("Students:",students)
print("Subjects:",subjects)

avg_score_each_student = np.mean(scores,axis=1) # axis=1 operate across columns (horizontal) and produce one result per row.
print("Avg score each student:",avg_score_each_student)

avg_score_each_subject = np.mean(scores,axis=0) # axis=0 operate across rows (Vertical) and produce one result per column.
print("Avg score each subject: ",avg_score_each_subject)

print("Highest score",np.max(scores))

condition_mask = scores > 85
print("Scores greater than 85",scores[condition_mask])