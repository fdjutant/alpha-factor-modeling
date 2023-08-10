import matplotlib.pyplot as plt

data = [1, 2, 3, 4, 5, 6, 7]
errors = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
x = range(len(data))

labels = ['CD63', 'CD81', 'CD9', 'CD63,\n CD81', 'CD63,\n CD9', 'CD81,\n CD9', 'CD63,\n CD81, CD9']

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x, data, yerr=errors, capsize=5, width=0.5,
       color='#1f77b4', edgecolor='black', linewidth=1.2)
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=14)

ax.set_yticklabels(ax.get_yticks(), fontsize=14)
# ax.set_xlabel('Protein', fontsize=14)
# ax.xaxis.label.set_position((0.5,-0.15))
ax.set_ylabel('Binned counts', fontsize=14)
ax.set_title('Biomarker expression Levels', fontsize=14)

for i in range(3, len(data), 3):
    ax.axvline(i - 0.5, color='k', linestyle='--')

# Remove top and right borders
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.savefig('bar-plot.png', transparent=True)

plt.show()
