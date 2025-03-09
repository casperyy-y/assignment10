def compute_bowling_scores(score1, score2, score3, handicap):
    average_score = (score1 + score2 + score3) / 3
    adjusted_average = average_score + handicap
    return average_score, adjusted_average

last_name = input("Enter bowler last name: ")
score1 = int(input("Enter first game score: "))
score2 = int(input("Enter second game score: "))
score3 = int(input("Enter third game score: "))
handicap = int(input("Enter handicap: "))

average_score, adjusted_average = compute_bowling_scores(score1, score2, score3, handicap)

print(f"Bowler: {last_name}")
print(f"Average Score: {average_score:.2f}")
print(f"Average Score with Handicap: {adjusted_average:.2f}")
