import matplotlib.pyplot as plt


def boxPlotter(title, n_distributions, labels):
    colors = ["ivory", "antiquewhite", "wheat", "peachpuff"]

    fig, ax = plt.subplots()
    ax.set_ylabel("number")

    bplot = ax.boxplot(n_distributions, patch_artist=True, tick_labels=labels)

    # Colours!
    for patch, color in zip(bplot["boxes"], colors):
        patch.set_facecolor(color)

    plt.savefig(f"{title}_box_plot.png")


def histogramer(title, n_distributions, labels=""):
    colors = ["ivory", "antiquewhite", "wheat", "peachpuff"]

    num_dists = len(n_distributions)
    fig, axs = plt.subplots(1, num_dists, figsize=(5 * num_dists, 4), tight_layout=True)

    if num_dists == 1:
        axs = [axs]

    # Plot histograms
    for i in range(num_dists):
        axs[i].hist(n_distributions[i], bins=20, color=colors[i], edgecolor="black")
        if labels:
            axs[i].set_title(f"{title} {labels[i]}")
        axs[i].set_xlabel("Value")
        axs[i].set_ylabel("Frequency")

    plt.savefig(f"{title}_histogram.png")
