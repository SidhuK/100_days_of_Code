Baby_Names_TidyTuesday
================
2022-03-21

## R Markdown

``` r
library(tidytuesdayR)
library(tidyverse)
```

    ## ── Attaching packages ─────────────────────────────────────── tidyverse 1.3.1 ──

    ## ✓ ggplot2 3.3.5     ✓ purrr   0.3.4
    ## ✓ tibble  3.1.6     ✓ dplyr   1.0.8
    ## ✓ tidyr   1.2.0     ✓ stringr 1.4.0
    ## ✓ readr   2.1.2     ✓ forcats 0.5.1

    ## ── Conflicts ────────────────────────────────────────── tidyverse_conflicts() ──
    ## x dplyr::filter() masks stats::filter()
    ## x dplyr::lag()    masks stats::lag()

``` r
library(skimr)
library(magick)
```

    ## Linking to ImageMagick 6.9.12.3
    ## Enabled features: cairo, fontconfig, freetype, heic, lcms, pango, raw, rsvg, webp
    ## Disabled features: fftw, ghostscript, x11

``` r
library(streamgraph)
library(gganimate)
library(hrbrthemes)
```

    ## NOTE: Either Arial Narrow or Roboto Condensed fonts are required to use these themes.

    ##       Please use hrbrthemes::import_roboto_condensed() to install Roboto Condensed and

    ##       if Arial Narrow is not on your system, please see https://bit.ly/arialnarrow

``` r
library(ggthemes)
```

``` r
# Loading the dataset

tuesdata <- tidytuesdayR::tt_load(2022, week = 12)
```

    ## --- Compiling #TidyTuesday Information for 2022-03-22 ----

    ## --- There are 8 files available ---

    ## --- Starting Download ---

    ## 
    ##  Downloading file 1 of 8: `applicants.csv`
    ##  Downloading file 2 of 8: `babynames.csv`
    ##  Downloading file 3 of 8: `births.csv`
    ##  Downloading file 4 of 8: `lifetables.csv`
    ##  Downloading file 5 of 8: `maorinames.csv`
    ##  Downloading file 6 of 8: `nz_births.csv`
    ##  Downloading file 7 of 8: `nz_lifetables.csv`
    ##  Downloading file 8 of 8: `nz_names.csv`

    ## --- Download complete ---

``` r
babynames <- tuesdata$babynames
```

``` r
# Take a general overview of the data
skim(babynames)
```

|                                                  |           |
|:-------------------------------------------------|:----------|
| Name                                             | babynames |
| Number of rows                                   | 1924665   |
| Number of columns                                | 5         |
| \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_   |           |
| Column type frequency:                           |           |
| character                                        | 2         |
| numeric                                          | 3         |
| \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |           |
| Group variables                                  | None      |

Data summary

**Variable type: character**

| skim_variable | n_missing | complete_rate | min | max | empty | n_unique | whitespace |
|:--------------|----------:|--------------:|----:|----:|------:|---------:|-----------:|
| sex           |         0 |             1 |   1 |   1 |     0 |        2 |          0 |
| name          |         0 |             1 |   2 |  15 |     0 |    97310 |          0 |

**Variable type: numeric**

| skim_variable | n_missing | complete_rate |    mean |      sd |   p0 |  p25 |  p50 |  p75 |     p100 | hist  |
|:--------------|----------:|--------------:|--------:|--------:|-----:|-----:|-----:|-----:|---------:|:------|
| year          |         0 |             1 | 1974.85 |   34.03 | 1880 | 1951 | 1985 | 2003 |  2017.00 | ▁▂▃▅▇ |
| n             |         0 |             1 |  180.87 | 1533.34 |    5 |    7 |   12 |   32 | 99686.00 | ▇▁▁▁▁ |
| prop          |         0 |             1 |    0.00 |    0.00 |    0 |    0 |    0 |    0 |     0.08 | ▇▁▁▁▁ |

``` r
# check for most common names
babynames %>% 
  count(name) %>% arrange(desc(n))
```

    ## # A tibble: 97,310 × 2
    ##    name        n
    ##    <chr>   <int>
    ##  1 Francis   276
    ##  2 James     276
    ##  3 Jean      276
    ##  4 Jesse     276
    ##  5 Jessie    276
    ##  6 John      276
    ##  7 Johnnie   276
    ##  8 Joseph    276
    ##  9 Lee       276
    ## 10 Leslie    276
    ## # … with 97,300 more rows

``` r
# make a new subset of most frequently occurring names through the years.
# babynames_common <- babynames %>% 
#   group_by(name) %>% 
#   mutate(freq = n()) %>% 
#   ungroup() %>% 
#   filter(freq > 275) %>%
#   select(-freq)
# 
# 
# sharedName <- babynames %>%
#   mutate(male = ifelse(sex == "M", n, 0), female = ifelse(sex == "F", n, 0)) %>%
#   group_by(name) %>%
#   summarize(Male = as.numeric(sum(male)), 
#             Female = as.numeric(sum(female)),
#             count = as.numeric(sum(n)),
#             AvgYear = round(as.numeric(sum(year * n) / sum(n)),0)) %>%
#   filter(Male > 30000 & Female > 30000) %>%
#   collect


babynames_popular <- babynames %>%
  group_by(sex, name) %>%
  summarize(total = sum(n)) %>%
  arrange(desc(total))
```

    ## `summarise()` has grouped output by 'sex'. You can override using the `.groups`
    ## argument.

``` r
babynames_top7 <-  babynames %>% 
  filter(name %in% 
           c("James","John", "Robert", 
             "Mary", "William", "David","Joseph","Ricard", "Elizabeth"))
```

``` r
p <- babynames_top7 %>%
  arrange(name, year) %>%
  mutate(x_reveal = row_number()) %>%
  ggplot(aes(x = year, y = n, colour = name)) +
  geom_line() +
  ggtitle("Popularity of American names in the previous 150 years") +
  theme_fivethirtyeight() +
  ylab("Number of babies born") +
  transition_reveal(along = x_reveal)

animate(p,nframes=300, fps = 4)
```

![](March-22_files/figure-gfm/unnamed-chunk-6-1.gif)<!-- -->
