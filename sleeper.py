kc = sleeper_projection_df[sleeper_projection_df["team"] == "KC"]

# Convert 'stats' dictionary column into separate columns
df_expanded = kc.join(pd.json_normalize(kc["stats"]))

# Drop the original 'stats' column (optional)
df_expanded = df_expanded.drop(columns=["stats"])