
maths = 82
python = 92
networking = 70
databases = 68
operating_systems = 62

total_marks = maths + python + networking + databases + operating_systems
print('Total Marks:', total_marks)

average = total_marks / 5
print('Average:', average)

pass_mark = 50

if average < pass_mark:
    print('You Failed ')
else:
    print('You Passed')
scores = [82, 92, 70, 68, 62]

highest_score = max(scores)
lowest_score = min(scores)

print('Highest Score:', highest_score)
print('Lowest Score', lowest_score)