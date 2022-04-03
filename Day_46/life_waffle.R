# Loading Packages

library(tidyverse)
library(lubridate)
library(waffle)
library(hrbrthemes)


# Create the data-----

life_data <-
  # make months
  tibble(months = factor(rep(month.abb[1:12], 77), levels=month.abb[1:12])) %>% 
  # remove months until December  (or start months from December)
  slice(12:(n()-1)) %>%  
  # till 75 years
  tibble(
    age = rep(0:75, each = 12) 
  ) %>%
  # easier to find each month by adding row number.
  rowid_to_column("row_name") 

## add the "eras" or major events so far to be colored in the waffle chart
life_data <- life_data %>%
  mutate(era = fct_inorder(case_when(row_name < 165 ~ "Childhood",
                                     row_name < 210 ~ "High School",
                                     row_name < 268 ~ "Bachelor's",
                                     row_name < 292 ~ "Master's",
                                     row_name < ((year(Sys.Date()) - 1992)*12) + 
                                       (month(Sys.Date()) - 11) ~ "Adulting",
                                     ## months into "Adulting" based on current month
                                     TRUE ~ "Time left")))

# Making the actual chart -----
life_in_months <- life_data %>%
  count(era) %>% 
  ## the count of each era is the number of months in that era
  ggplot(aes(fill = era, values = n)) +
  ## make each row a year/12 months
  geom_waffle(color = "#F7F7F7", n_rows = 12, size = 1, flip = TRUE) + 
  ## assign colors to the eras
  scale_fill_manual(name = "", values = c("#EF476F","#FCA311","#FFD166","#0EAD69","#4ECDC4","#118AB2")) +  
  coord_equal() +
  theme_ipsum(grid = "") +
  theme(legend.text = element_text(size = 40),
        plot.background = element_rect(fill = "#F7F7F7", color = "#F7F7F7")) +
  theme_enhance_waffle()


life_in_months

# Save the chart as svg for editing further
ggsave("life_in_months2.svg",  width = 15, height = 25, dpi = 300)

