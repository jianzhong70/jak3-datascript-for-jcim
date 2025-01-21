import csv
import matplotlib.pyplot as plt
import numpy as np
# Openning the decompe files
filename='E:/cjzdata2/jak3/decomp/3lxlb-decomp.dat'
#Obtaining the complete information of all residues
output_all_file='E:/cjzdata2/jak3/timepicture/rmsf_images/3lxlb-decomp.dat'
#Obtaining energy contribution of key residues
output_key_file='E:/cjzdata2/jak3/timepicture/rmsf_images/3lxlb_key.dat'
#output_key_last='E:/cjzdata2/jak3/timepicture/rmsf_images/3lxlb_key_last.dat'

offset = 16
threshold=-1.0

png_save_path='E:/cjzdata2/jak3/timepicture/rmsf_images/3lxlb-decomp.png'
max_residue=301 #The number of the last residue from the proteins
xlabel='Residue number'
ylabel='Energy contributions(kcal/mol)'

residue_list=[]

head=['#Number','S_vdw','B_vdw','T_vdw','S_ele', 'B_ele','T_ele','S_gb','B_gb','T_gb','Total']
flag_begin = False
flag_total = False
flag_sidechain = False
flag_backbone = False

cnt_total = 0
cnt_sidechain = 0
cnt_backbone = 0
total_line=[]
sidechain_line=[]
backbone_line = []
with open(filename, 'r') as file:
    # The conversion between the data and csv format
    reader = csv.reader(file)

    # Reading the data and printing
    for row in reader:
        for element in row:
            if 'DELTAS' in element:
                # When including the objective word, extracting the corresponding information
                flag_begin = True
                break
            if flag_begin and ('Total' in element):
                flag_total = True
                break
            if flag_begin and ('Sidechain' in element):
                flag_sidechain = True
                break
            if flag_begin and ('Backbone' in element):
                flag_backbone = True
                break
        if flag_begin and flag_total:
            cnt_total = cnt_total + 1
        if flag_begin and flag_sidechain:
            cnt_sidechain = cnt_sidechain + 1
        if flag_begin and flag_backbone:
            cnt_backbone = cnt_backbone + 1

        if cnt_total >= 4 and len(row) > 1 and cnt_sidechain == 0:
            line = [row[0], round((float)(row[5]), 2), round((float)(row[8]), 2), round((float)(row[11]), 2), round((float)(row[17]), 2)]
            #print(line)
            total_line += [line]
        if cnt_sidechain >= 4 and len(row) > 1 and cnt_backbone == 0:
            line = [row[0], round((float)(row[5]), 2), round((float)(row[8]), 2), round((float)(row[11]), 2)]
            #print(line)
            sidechain_line += [line]
        if cnt_backbone >= 4 and len(row)>1:
            print(row)
            line = [row[0], round((float)(row[5]), 2), round((float)(row[8]), 2), round((float)(row[11]), 2)]
            print(line)
            backbone_line += [line]
    #print(sidechain_line)

with open(output_all_file, 'w') as file:
    # Traversaling the all data
    line = f"{head[0]:<{10}} {head[1]:<{10}} {head[2]:<{10}} {head[3]:<{10}} {head[4]:<{10}} {head[5]:<{10}} {head[6]:<{10}} {head[7]:<{10}} {head[8]:<{10}} {head[9]:<{10}} {head[10]:<{10}} \n"
    file.write(line)
    for i in range(len(total_line)):
        row_total = total_line[i]
        row_sidechain = sidechain_line[i]
        row_backbone =backbone_line[i]
        residue_name = row_sidechain[0].split()[0]
        residue_number = row_sidechain[0].split()[1]
        residue_number = (int)(residue_number) + offset
        line = f"{residue_number:<{10}} {row_sidechain[1]:<{10}} {row_backbone[1]:<{10}} {row_total[1]:<{10}} {row_sidechain[2]:<{10}} {row_backbone[2]:<{10}} {row_total[2]:<{10}} {row_sidechain[3]:<{10}} {row_backbone[3]:<{10}}  {row_total[3]:<{10}} {row_total[4]:<{10}}  \n"
        file.write(line)

        if (float)(row_total[4]) <= threshold:
            print(residue_name, residue_number,row_total[4])
            residue_list.append(residue_number)

with open(output_key_file, 'w') as file:
    # Traversaling the data and writing
    line = f"{head[0]:<{10}} {head[1]:<{10}} {head[2]:<{10}} {head[3]:<{10}} {head[4]:<{10}} {head[5]:<{10}} {head[6]:<{10}} {head[7]:<{10}} {head[8]:<{10}} {head[9]:<{10}} {head[10]:<{10}} \n"
    file.write(line)
    for i in range(len(total_line)):
        row_total = total_line[i]
        row_sidechain = sidechain_line[i]
        row_backbone = backbone_line[i]
        residue_name = row_sidechain[0].split()[0]
        residue_number = row_sidechain[0].split()[1]
        residue_number = (int)(residue_number) + offset
        for residue in residue_list:
                if (int)(residue) == residue_number:
                    line = f"{residue_number:<{10}} {row_sidechain[1]:<{10}} {row_backbone[1]:<{10}} {row_total[1]:<{10}} {row_sidechain[2]:<{10}} {row_backbone[2]:<{10}} {row_total[2]:<{10}} {row_sidechain[3]:<{10}} {row_backbone[3]:<{10}}  {row_total[3]:<{10}} {row_total[4]:<{10}}  \n"
                    file.write(line)

data = np.loadtxt(output_all_file) # LOading the output_all-file.

x_values = data[:, 0]
#print(x_values)
y_values = data[:, 10]
#yrange=(-4.0, 0.5)
#bottom = -1

i = 0
#for x, y in zip(x_values, y_values):
#    if x > max_residue:
#        break
#    if y > 0:
#        plt.vlines(x, ymin=0, ymax=y, color='black', linewidth=2)
#    else:
#        plt.vlines(x, ymin=y, ymax=0, color='black', linewidth=2)
#    #if y <= threshold:
       # plt.scatter(x, y, marker=markers[i], color='black', label=labels[i])
       # i = i + 1
fig, ax = plt.subplots()
markerline, stemlines, baseline = ax.stem(x_values, y_values)
plt.setp(markerline, color='red', marker='o')
plt.setp(stemlines, color='blue', linestyle=':')
plt.setp(baseline, color='grey', linewidth=3, linestyle='-')
ax.axhline(y=0,color='black')
ax.axhline(y=threshold, linestyle='--',color='black')

ax.set_xlabel(xlabel, fontweight='bold', fontsize=18)
ax.set_ylabel(ylabel, fontweight='bold', fontsize=14)


ax = plt.gca()
ax.axis([17,301,-3.0,0.6])

# Setting the property of the x_axis
for label in ax.get_xticklabels():
    label.set_fontsize(12)  # Setting the fontsize of the word
    label.set_fontweight('bold')  # Setting the thickness of the word

# Setting the property of the y_axis
for label in ax.get_yticklabels():
    label.set_fontsize(12)  # Setting the fontsize of the word
    label.set_fontweight('bold')  # Setting the thickness of the word


plt.savefig(png_save_path, dpi=600, bbox_inches='tight')
plt.show()
