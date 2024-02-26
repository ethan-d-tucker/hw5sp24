from scipy import stats
import numpy as np
import matplotlib.pyplot as plt


def plot_normal_dist():
    """
    Plots the probability density function (PDF) and cumulative distribution function (CDF)
    of a standard normal distribution. Highlights the probability for x < 1 in the PDF plot and
    marks the cumulative probability at x = 1 in the CDF plot.

    No parameters or returns. This is a direct visualization tool.
    """

    # Set up the figure and axes for the two stacked plots
    fig, axs = plt.subplots(2, 1, figsize=(10, 8))

    # Generate a range of x values for the standard normal distribution
    x_values = np.linspace(-4, 4, 1000)

    # Calculate the PDF for the standard normal distribution
    pdf_values = stats.norm.pdf(x_values)
    # Plot the PDF and shade the area for x < 1
    axs[0].plot(x_values, pdf_values, label="PDF for N(0,1)")
    axs[0].fill_between(x_values, pdf_values, where=(x_values < 1), color='grey', alpha=0.5)
    axs[0].set_title("PDF of N(0,1) with area under curve for P(x<1)")

    # Calculate the CDF for the standard normal distribution
    cdf_values = stats.norm.cdf(x_values)
    # Plot the CDF and mark the value at x = 1
    axs[1].plot(x_values, cdf_values, label="CDF for N(0,1)", color='blue')
    axs[1].plot([1, 1], [0, stats.norm.cdf(1)], color='red', linestyle='dashed')
    axs[1].scatter([1], [stats.norm.cdf(1)], color='red')
    axs[1].set_title("CDF of N(0,1) with P(x<1) marked")

    # Labeling the axes
    for ax in axs:
        ax.set_xlabel('x')
        ax.set_ylabel('Probability')

    # Adding legends to both subplots
    axs[0].legend()
    axs[1].legend()

    # Adjust layout to prevent overlap and display the plots
    plt.tight_layout()
    plt.show()


# Call the function to plot the distributions
plot_normal_dist()
