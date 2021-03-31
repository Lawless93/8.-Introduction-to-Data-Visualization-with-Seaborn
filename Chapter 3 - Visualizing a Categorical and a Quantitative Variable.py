# Create column subplots based on age category
sns.catplot(y="Internet usage", data=survey_data,
            kind="count", col="Age Category")

# Show plot
plt.show()


# Create a bar plot of interest in math, separated by gender
sns.catplot(x="Gender", y="Interested in Math",
            data=survey_data, kind="bar")

# Show plot
plt.show()


# Turn off the confidence intervals
sns.catplot(x="study_time", y="G3",
            data=student_data,
            kind="bar",
            order=["<2 hours", "2 to 5 hours", "5 to 10 hours", ">10 hours"],
            ci=None)

# Show plot
plt.show()


# Specify the category ordering
study_time_order = ["<2 hours", "2 to 5 hours",
                    "5 to 10 hours", ">10 hours"]

# Create a box plot and set the order of the categories
sns.catplot(x="study_time", y="G3", data=student_data,
            kind="box", order=study_time_order)

# Show plot
plt.show()


# Create a box plot with subgroups and omit the outliers
sns.catplot(x="internet", y="G3", data=student_data,
            kind="box", hue="location", sym="")

# Show plot
plt.show()


# Set the whiskers at the min and max values
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box",
            whis=[0, 100])

# Show plot
plt.show()


# Remove the lines joining the points
sns.catplot(x="famrel", y="absences",
            data=student_data,
            kind="point",
            capsize=0.2,
            join=False)

# Show plot
plt.show()


# Import median function from numpy
from numpy import median

# Plot the median number of absences instead of the mean
sns.catplot(x="romantic", y="absences",
			data=student_data,
            kind="point",
            hue="school",
            ci=None,
            estimator=median)

# Show plot
plt.show()