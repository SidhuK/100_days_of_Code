# %% [markdown]
# # Marvel Movies Dataset

# %% [markdown]
# ## Load required packages

# %%
# MARVEL MOVIES DATASET ANALYSIS
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# %% [markdown]
# ## Load Data

# %%
marvel_movies = pd.read_csv("mcu_box_office.csv")

# %% [markdown]
# ## Data checks

# %% [markdown]
# #### How Many Rows and Columns does the data have?

# %%
marvel_movies.shape

# %% [markdown]
# #### What are the column names?

# %%
marvel_movies.columns

# %% [markdown]
# #### Look at the first 5 rows

# %%
marvel_movies.head()

# %% [markdown]
# #### Describe the various values, what are the maximum and minimum values?

# %%
marvel_movies.describe()

# %% [markdown]
# #### Are there any missing values?

# %%
marvel_movies.isna().any()

# %% [markdown]
# #### What are each columns datatypes?

# %%
marvel_movies.dtypes

# %% [markdown]
# #### Converting the budgets from objects into number

# %%
marvel_movies['production_budget'] = marvel_movies['production_budget'].str.split(
    ',').str.join("").astype(float)
marvel_movies['opening_weekend'] = marvel_movies['opening_weekend'].str.split(
    ',').str.join("").astype(float)
marvel_movies['domestic_box_office'] = marvel_movies['domestic_box_office'].str.split(
    ',').str.join("").astype(float)
marvel_movies['worldwide_box_office'] = marvel_movies['worldwide_box_office'].str.split(
    ',').str.join("").astype(float)


# %% [markdown]
# #### Converting Release date to datetime object.

# %%
marvel_movies.release_date = pd.to_datetime(marvel_movies.release_date)

# %% [markdown]
# #### Does the data contain any duplicate rows?

# %%
marvel_movies.duplicated().any()

# %% [markdown]
# ## Data Visualization

# %% [markdown]
# ### How were the movies rated by audience and critics?

# %% [markdown]
# #### Rotten Tomatoes Scores for each Marvel Movie

# %%
plt.figure(figsize=(20, 8))
plt.xticks(rotation=90)
sns.barplot(x="movie_title", y="tomato_meter",
            data=marvel_movies, hue="mcu_phase", dodge=False)
plt.title("Rotten Tomatoes Scores", fontsize=20, fontweight="bold")
plt.xlabel("Movies", fontsize=15)
plt.ylabel("Rotten Tomatoes Score", fontsize=15)
plt.vlines(x=(5.5, 11.5, 22.5), ymin=0, ymax=110)


# %% [markdown]
# #### Audience Scores for each Movie

# %%
plt.figure(figsize=(20, 8))
plt.xticks(rotation=90)
sns.barplot(x="movie_title", y="audience_score",
            data=marvel_movies, hue="mcu_phase", dodge=False)
plt.title("Audience Scores", fontsize=20, fontweight="bold")
plt.xlabel("Movies", fontsize=15)
plt.ylabel("Audience Score", fontsize=15)
plt.vlines(x=(5.5, 11.5, 22.5), ymin=0, ymax=110)


# %% [markdown]
# #### Comparing the Audience vs RT Scores for each MCU Phase

# %%
compare_scores = pd.melt(marvel_movies, id_vars=("movie_title", "mcu_phase"), value_vars=(
    "tomato_meter", "audience_score"), value_name="score", var_name="type")
compare_scores.head()


# %%
compare_scores.dtypes

# %%
g = sns.catplot(x="movie_title", y="score",
                data=compare_scores, hue="type", col="mcu_phase", kind="bar", dodge=True, sharex=False, aspect=0.9, height=8)
g.set_xticklabels(rotation=90)
g.set_axis_labels("", "Scores")


# %% [markdown]
# #### How different movies split RT critics vs Audience
#
# Positive Value = Higher rotten tomatoes score
# Negative Value = Higher Audience score

# %%
marvel_movies["score_difference"] = marvel_movies["tomato_meter"] - \
    marvel_movies["audience_score"]
plt.figure(figsize=(20, 8))
plt.xticks(rotation=90)

clrs = ['grey' if (min(marvel_movies.score_difference) < x < max(
    marvel_movies.score_difference)) else 'orange' for x in marvel_movies.score_difference]

sns.barplot(x="movie_title", y="score_difference",
            data=marvel_movies, palette=clrs, dodge=False)
plt.title("Score Difference between RT and Audience",
          fontsize=20, fontweight="bold")
plt.xlabel("")
plt.ylabel("Score", fontsize=15)


# %% [markdown]
# ### How long were the movies?

# %%
sns.displot(data=marvel_movies, x='movie_duration', hue='mcu_phase', kind='kde',
            fill=True, palette=sns.color_palette('bright')[:4], height=8, aspect=0.9)


# %% [markdown]
# #### Have the movies gotten longer?

# %%

plt.figure(figsize=(20, 8))
plt.xticks(rotation=90)
sns.regplot(x=marvel_movies.index, y="movie_duration", data=marvel_movies)
sns.scatterplot(data=marvel_movies, x="movie_title",
                y="movie_duration", hue="mcu_phase", palette=sns.color_palette('bright')[:4])


# %% [markdown]
# ### How much money did the movies make?

# %%
budget = pd.melt(marvel_movies, id_vars=("movie_title", "mcu_phase"), value_vars=(
    "production_budget", "opening_weekend", "domestic_box_office", "worldwide_box_office"), value_name="budget_value", var_name="budget_type")


# %%
g = sns.catplot(x="movie_title", y="budget_value",
                data=budget, hue="budget_type", kind="bar", dodge=True, sharex=False, aspect=3, height=6)
g.set_xticklabels(rotation=90)


# %% [markdown]
# This is not a very informative graph.

# %% [markdown]
# #### How did the cost of making marvel movies change overtime?

# %%

plt.figure(figsize=(20, 8))
plt.xticks(rotation=90)
sns.regplot(x=marvel_movies.index, y="production_budget", data=marvel_movies)
sns.scatterplot(data=marvel_movies, x="movie_title",
                y="production_budget", hue="mcu_phase", palette=sns.color_palette('bright')[:4])


# %% [markdown]
# It looks like the budget remained fairly consistent over time.
#
# #### How does the revenue generated change over time?

# %%
plt.figure(figsize=(20, 8))
plt.xticks(rotation=90)
sns.regplot(x=marvel_movies.index,
            y="worldwide_box_office", data=marvel_movies)
sns.scatterplot(data=marvel_movies, x="movie_title",
                y="worldwide_box_office", hue="mcu_phase", palette=sns.color_palette('bright')[:4])


# %% [markdown]
# We see a slight upwards trend here.

# %% [markdown]
# #### Lets look at the profit margin

# %%
marvel_movies["percent_profit_margin"] = (
    (marvel_movies["worldwide_box_office"] - marvel_movies["production_budget"])/marvel_movies["worldwide_box_office"])*100
plt.figure(figsize=(20, 8))
plt.xticks(rotation=90)
sns.lineplot(x=marvel_movies.index,
             y="percent_profit_margin", data=marvel_movies)
sns.barplot(data=marvel_movies, x="movie_title",
            y="percent_profit_margin", hue="mcu_phase", palette=sns.color_palette('bright')[:4], dodge=False)


# %% [markdown]
# #### Breaking down the best performing movies by their domestic vs international box office revenue

# %%
marvel_movies["rest_of_world_box_office"] = marvel_movies["worldwide_box_office"] - \
    marvel_movies["domestic_box_office"]
box_office = marvel_movies[["movie_title",
                            "rest_of_world_box_office", "domestic_box_office"]]
box_office = box_office.sort_values(
    "rest_of_world_box_office", ascending=False)


# %%

box_office_plot = box_office.set_index('movie_title').plot(kind='bar', stacked=True,
                                                           figsize=(15, 8))
box_office_plot


# %% [markdown]
# ### Does Higher Audience score = More Revenue?

# %%
plt.figure(figsize=(7, 5))
sns.scatterplot(x="audience_score",
                y="worldwide_box_office", data=marvel_movies)
