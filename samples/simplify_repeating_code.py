# CODE FRAGMENT - reference

# TOO MUCH REPETITION
labels = list(df.columns)
labels[0] = labels[0].replace(' ', '_')
labels[1] = labels[1].replace(' ', '_')
labels[2] = labels[2].replace(' ', '_')
labels[3] = labels[3].replace(' ', '_')
labels[5] = labels[5].replace(' ', '_')
labels[6] = labels[6].replace(' ', '_')
df.columns = labels

df.head()

# BETTER
df.columns = [label.replace(' ', '_') for label in df.columns]
df.head()
