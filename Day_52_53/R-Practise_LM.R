library(tidyverse)


petals <- iris


linear_model <- lm(petals, formula = Sepal.Length ~ Sepal.Width)

summary(linear_model)


ggplot(petals) +
  geom_point(aes(x = Sepal.Length, y = Sepal.Width, color = Species))


linear_model2 <- lm(petals, formula = Sepal.Length ~ Petal.Length)

summary(linear_model2)


ggplot(petals) +
  geom_point(aes(x = Sepal.Length, y = Petal.Length, color = Species))




ggplot(petals) +
  aes(
    x = Sepal.Length,
    y = Petal.Length,
    colour = Species,
    size = Petal.Width
  ) +
  geom_point(shape = "square") +
  geom_smooth(span = 1) +
  scale_color_brewer(palette = "Set3", direction = -1) +
  labs(
    x = "Sepal Length",
    y = "Petal Length",
    title = "Comparing the Sepal Length vs Petal Length",
    subtitle = "And using the relationship between the two to predit their function",
    caption = "Graphic: Karat Sidhu",
    color = "Species",
    size = "Petal Width"
  ) +
  ggthemes::theme_solarized_2() +
  theme(
    plot.title = element_text(size = 20,
                              face = "bold"),
    plot.caption = element_text(face = "bold"),
    axis.title.y = element_text(face = "bold"),
    axis.title.x = element_text(face = "bold")
  )










