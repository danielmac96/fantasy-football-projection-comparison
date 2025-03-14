import pandas as pd

kc_df_0 = pd.read_json("sleeper_data.json", orient="records")

kc_df_1 = kc_df_0[kc_df_0["team"] == "KC"]

stats_expanded = pd.json_normalize(kc_df_1["stats"])
stats_expanded["date"] = kc_df_1["date"].values
stats_expanded["player_id"] = kc_df_1["player_id"].values

# Convert 'stats' dictionary column into separate columns
kc_df_1_expand = pd.merge(kc_df_1, stats_expanded, on=["date", "player_id"], how="left")

player_expanded = pd.json_normalize(kc_df_1["player"])
player_expanded["date"] = kc_df_1["date"].values
player_expanded["player_id"] = kc_df_1["player_id"].values

kc_df_2_expanded = pd.merge(kc_df_1_expand, player_expanded, on=["date", "player_id"], how="left")
