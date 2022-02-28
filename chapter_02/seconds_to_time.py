total_secs = int(input("How many seconds, in total?\n> "))
hours = total_secs // 3600
secs_still_remaining = total_secs % 3600
minutes =  secs_still_remaining // 60
secs_finally_remaining = secs_still_remaining  % 60
print("Time:", hours, ":", minutes, ":", secs_finally_remaining)
