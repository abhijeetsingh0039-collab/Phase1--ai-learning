#======Challenge 1: AI improvement tracker======
from tokenize import Double


print("\n--- AI Improvement Tracker ---")
current_phase="python + API"
next_goal="Master APIs"
print(f"CURRENT PHASE: {current_phase}")
print(f"NEXT GOAL: {next_goal}")
hours=float(input("enter hours studied today: "))
days=int(input("enter number of days completed: "))
hours=hours*days
total_hours=42
total_hours=total_hours-hours
print(f"Total hours remaining: {total_hours} hours")