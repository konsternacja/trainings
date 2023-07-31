# LOAD PACKAGES ############################################

library(datasets)

# LOAD DATA ################################################

?iris
head(iris)

# HISTOGRAMS

hist(iris$Sepal.Width)
hist(iris$Petal.Length)

# DENSITY PLOTS

plot(density(iris$Sepal.Width)) 
plot(density(iris$Sepal.Length)) 

# SHAPIRO TEST

shapiro.test(iris$Sepal.Width)
shapiro.test(iris$Sepal.Length)

# width has normal distribution, length has not.