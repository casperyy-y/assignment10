def compute_scores(score1, score2, score3):
    total_points = score1 + score2 + score3
    average_score = total_points / 3
    return total_points, average_score

last_name = input("Enter student last name: ")
score1 = float(input("Enter first exam score: "))
score2 = float(input("Enter second exam score: "))
score3 = float(input("Enter third exam score: "))

total_points, average_score = compute_scores(score1, score2, score3)

print(f"Student: {last_name}")
print(f"Total Points: {total_points}")
print(f"Average Score: {average_score:.2f}")
