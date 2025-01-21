import matplotlib.pyplot as plt
import numpy as np


file_paths = ['D:/cjzdat/jak3/time/3lxl/rmsd.dat','D:/cjzdat/jak3/time/3lxlp/rmsd.dat', 
               'D:/cjzdat/jak3/time/3lxlb/rmsd.dat']
labels = ['IZA-WT','IZA-SP', 'IZA-DP']
#colors = ['blue', 'orange', 'green', 'red']

all_data = []
for file_path in file_paths:
    data = np.loadtxt(file_path)
    all_data.append(data)

#plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
i = 0
for data in all_data:
    x = 0.004*data[:, 0]
    y = data[:, 1]
    #plt.plot(x, y, label=labels[i], color=colors[i])
    ax.plot(x, y, label=labels[i])
    i = i + 1

ax.axis([0, 6000, 0, 7])

ax.set_xlabel('Simulation times(ns)', fontweight='bold',fontsize=18)
ax.set_ylabel('RMSDs of JAK3(Å)',fontweight='bold', fontsize=18)

save_path='D:/cjzdat/jak3/picture/iza-jak3-rmsd.png'
show_grid=True

#ax = plt.gca()
#plt.yticks([0, 2, 4, 6, 8, 10, 12])
for label in ax.get_xticklabels():
    label.set_fontsize(14)  
    label.set_fontweight('bold')  

for label in ax.get_yticklabels():
    label.set_fontsize(14)  
    label.set_fontweight('bold') 

#plt.title('')
#ax.legend()
#legend = plt.legend()
legend = ax.legend(loc='upper right', bbox_to_anchor=(1.015, 1.015), framealpha=0.5)

for text in legend.get_texts():
    text.set_fontsize(13)  
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