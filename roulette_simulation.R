# roulette_simulation.R
# Monte Carlo simulation of 100 £1 European roulette bets
# Compare simulated results with theoretical expectation

set.seed(123)  # reproducibility

bets <- 100      # number of bets per session
runs <- 10000    # number of Monte Carlo runs

# Simulate outcomes: +35 for a win, -1 for a loss
simulate_session <- function(bets) {
  sum(sample(c(-1, 35),
             size = bets,
             replace = TRUE,
             prob = c(36/37, 1/37)))
}

# Run many simulations
results <- replicate(runs, simulate_session(bets))

# Summary statistics
mean_result <- mean(results)
sd_result   <- sd(results)
expected_ev <- bets * ((35 * (1/37)) - (36/37))

cat("Simulated mean result:", round(mean_result, 2), "\n")
cat("Theoretical expected result:", round(expected_ev, 2), "\n")
cat("Standard deviation:", round(sd_result, 2), "\n")

# Plot histogram
hist(results,
     breaks = 40,
     main = "Distribution of Returns: 100 £1 Roulette Bets",
     xlab = "Net Return (£)",
     col = "lightblue",
     border = "white")

abline(v = expected_ev, col = "red", lwd = 2)
legend("topright", legend = c("Theoretical mean"), col = "red", lwd = 2)
