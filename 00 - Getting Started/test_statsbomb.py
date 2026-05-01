from mplsoccer import Sbopen
parser = Sbopen()

# # opening data using competition method
# df_competition = parser.competition()
# # structure of data
# df_competition.info()

# # opening data using match method
# df_match = parser.match(competition_id=72, season_id=30)
# # structure of data
# df_match.info()

# # opening data using match method
# df_lineup = parser.lineup(69301)
# # structure of data
# df_lineup.info()

# # opening data
# df_event, df_related, df_freeze, df_tactics = parser.event(69301)
# # if you want only event data you can use
# # df_event = parser.event(69301)[0]
# # structure of data
# df_event.info()

# 360 data
df_frame, df_visible = parser.frame(3788741)
# exploring the data
df_frame.info()
