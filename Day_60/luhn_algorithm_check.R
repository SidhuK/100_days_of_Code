
# Ask for an input
enter_number <-  (readline(prompt = "Enter a Number
                           to check if it passes the Luhn Algorithm test: "))


# Remove spaces from the input
remove_spaces <- stringr::str_replace_all(enter_number, " ", "")


# Convert into a list of digits
digits <- as.integer(stringr::str_split(remove_spaces, "")[[1]])


# If length of digits is false, or doesnt contain digits, then return f
if (length(digits) < 2 || anyNA(digits)) {
  FALSE
} else {
  doublers <- rev(rep(c(FALSE, TRUE), length.out = length(digits)))
  digits[doublers] <- 2  * digits[doublers]
  digits[digits > 9] <- digits[digits > 9] - 9
  sum(digits) %% 10 == 0
}
