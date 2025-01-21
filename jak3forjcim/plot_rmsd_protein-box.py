import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd


file_paths = ['E:\cjzdata2\jak3\/time\/3lxl/rmsd.dat','E:\cjzdata2\jak3\/time\/3lxlp/rmsd.dat',  
              'E:\cjzdata2\jak3\/time\/3lxlb/rmsd.dat']
labels = ['IZA-WT','IZA-SP', 'IZA-DP']
#colors = ['b', 'o', 'g']

all_data = []
category_lst = []
i = 0
for file_path in file_paths:
    data = np.loadtxt(file_path)  
    for row in data:
        all_data.append(row[1])
        category_lst.append(labels[i])
    i = i + 1

#plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

df = pd.DataFrame({
    'value': np.array(all_data),
    'category': category_lst
})

#ax.boxplot(all_data)
sns.boxplot(x="category", y="value", data=df)

#ax.axis([0, 3000, 0, 20])

ax.set_xlabel('System indexes', fontweight='bold',fontsize=18)
ax.set_ylabel('RMSDs of JAK3(Å)',fontweight='bold', fontsize=18)

save_path='E:/cjzdata2/jak3/timepicture/rmsf_images/IZA-jak3-rmsd-box.png'
show_grid=True

#ax = plt.gca()
#plt.yticks([0, 2, 4, 6, 8, 10, 12])

for label in ax.get_xticklabels():
    label.set_fontsize(16)  
    label.set_fontweight('bold')  


for label in ax.get_yticklabels():
    label.set_fontsize(16) 
    label.set_fontweight('bold')  

#plt.title('')
#ax.legend()
#legend = plt.legend()
legend = ax.legend(loc='upper right', bbox_to_anchor=(1.015, 1.015), framealpha=0.5)

for text in legend.get_texts():
    text.set_fontsize(16) 
    text.set_fontweight('bold')  

for line in legend.get_lines():
    line.set_linewidth(3)  

#for residue in residue_lst:
    #plt.axvline(x=residue, color='black', linestyle='--', dashes=(5, 2))

plt.grid(show_grid)
plt.savefig(save_path, dpi=600, bbox_inches='tight')
#plt.ion()
#plt.pause(300)
plt.show()