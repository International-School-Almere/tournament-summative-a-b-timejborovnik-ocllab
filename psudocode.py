#Algorithm 1 — calculate points from rank
# FUNCTION calculate_points(rank)
# IF rank = 1 THEN return 10
# IF rank = 2 THEN return 8
# IF rank = 3 THEN return 6
# IF rank = 4 THEN return 4
# IF rank = 5 THEN return 2
# IF rank is between 6 and 8 THEN return 1
# OTHERWISE return 0
# END FUNCTION

#Algorithm 2 — calculate team total
# FUNCTION calculate_team_total(team_name)
# SET total = 0
# FOR each member in team_members[team_name]
# FOR each event in events
# IF member has a score in that event
# ADD member.score to total
# END IF
# END FOR
# END FOR
# RETURN total
# END FUNCTION

#Algorithm 3 — sort leaderboard
# FUNCTION sort_leaderboard(competitors)
# SORT competitors by total_points from highest to lowest
# FOR i = 0 TO length of sorted list - 1
# SET sorted_list[i].rank = i + 1
# IF i > 0 AND current total = previous total
# SET current rank = previous rank (tie)
# END IF
# END FOR
# RETURN sorted list
# END FUNCTION

#Algorithm 4a — validate name
# FUNCTION validate_name(name)
# IF name is empty OR name is only spaces
# RETURN False, "Name cannot be blank"
# END IF
# IF name already exists in competitors
# RETURN False, "Duplicate name detected"
# END IF
# RETURN True, ""
# END FUNCTION

#Algorithm 4b — validate rank
# FUNCTION validate_rank(rank)
# IF rank is not a number
# RETURN False, "Rank must be a number"
# END IF
# IF rank < 0
# RETURN False, "Rank must be positive"
# END IF
# RETURN True, ""
# END FUNCTION