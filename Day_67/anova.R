library(tidyverse)
library(gt)


# Loading the dataset
my_data <- PlantGrowth


# Anova Analysis
anova <- aov(weight ~ group, data = my_data)

# Anova Summary
anova_summary <- (summary(anova))

# convert into DF
anova_table <- as.data.frame(summary(anova)[[1]])

# Add rows, check if the p value is significant
anova_table <- anova_table %>%
  rownames_to_column(var = "Variable") %>%
  mutate(significant = ifelse(`Pr(>F)` < 0.05, "Yes", ""))


# Format the table for export
anova_table %>%
  gt() %>%
  tab_header(title = "One Way Anova",
             subtitle = "Summary of Analysis of Variance") %>%
  tab_footnote(footnote = "The data was statistically significant",
               locations = cells_column_labels("Pr(>F)")) %>%
  tab_source_note("Data from the Plant Growth dataset built-in R")
