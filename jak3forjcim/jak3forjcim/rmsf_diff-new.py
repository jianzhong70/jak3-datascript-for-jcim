import matplotlib.pyplot as plt
import os

def plot_data_with_difference(p_path, dp_path, wt_path, y_range=None, offset=0, save_fig_name=None, legends=['P', 'WT']):
    
    def load_data(file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()[1:]  
            data = [float(line.strip().split()[1]) for line in lines]
        return data

    data1 = load_data(p_path)
    data2 = load_data(dp_path)
    data3 = load_data(wt_path)

    
    differences1 = [d1 - d3 for d1, d3 in zip(data1, data3)]
    differences2 = [d2 - d3 for d2, d3 in zip(data2, data3)]

    
    numbers = list(range(1, len(data1) + 1))
    if offset != 0:
        numbers = [n + offset for n in numbers]

    
    fig, ax = plt.subplots()

    ax.plot(numbers, data3, label='{}'.format(legends[0]), color='blue', linewidth=2)
    ax.plot(numbers, data1, label='{}'.format(legends[1]), color='orange', linewidth=2)
    ax.plot(numbers, data2, label='{}'.format(legends[2]), color='green', linewidth=2)
    ax.plot(numbers, differences1, label=r'$\Delta$RMSF-SP', color='red', linewidth=2)
    ax.plot(numbers, differences2, label=r'$\Delta$RMSF-DP', color='cyan', linewidth=2)

    ax.set_xlabel('Residue Index', fontweight='bold', fontsize=16)
    ax.set_ylabel(r'RMSF($\mathring{A}$)', fontweight='bold', fontsize=16)
    #ax.tick_params(labelsize=14,labelweight='bold')
    plt.xticks(fontweight='bold', fontsize=14)
    plt.yticks(fontweight='bold', fontsize=14)

    if y_range is not None:
        ax.set_ylim(y_range)

    ax.axhline(y=0, color='black', linewidth=2)
    ax.axis([16,301, -20, 700])
    # plt.legend(loc='upper right', fontsize=12)
    ax.legend(prop={'weight': 'bold', 'size': 12})
    show_grid=True

    for spine in plt.gca().spines.values():
        spine.set_linewidth(1.5)

    plt.tight_layout()
    plt.grid(show_grid)
    # plt.show()
    plt.savefig(save_fig_name, dpi=600, bbox_inches='tight')

if __name__ == '__main__':
    
    output_folder = 'rmsf_images'
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    y_range = (-2, 9.6)
    offset = 16

    file_list= [ 
                ('E:/cjzdata2/jak3/time/3lxl/rmsf.dat',  'IZA-WT'),    # 0    6eif_ap
                ('E:/cjzdata2/jak3/time/3lxlp/rmsf.dat', 'IZA-SP'),     # 1   6eif_wt
                ('E:/cjzdata2/jak3/time/3lxlb/rmsf.dat', 'IZA-DP'),    # 2   7fhs_ap
                ('E:/cjzdata2/jak3/time/3lxk/rmsf.dat',  'MI1-WT'),     # 3   7fhs_wt
                ('E:/cjzdata2/jak3/time/3lxkp/rmsf.dat', 'MI1-SP'),    # 4   7fht_ap
                ('E:/cjzdata2/jak3/time/3lxkb/rmsf.dat', 'MI1-DP'),     # 5   7fht_wt
                # ('../apo/ap/nowat/rmsf1.dat', 'apo_DYRK1Ap'),     # 6   apo_ap
                # ('../apo/wt/nowat/rmsf1.dat', 'apo_DYRK1A'),      # 7   apo_wt
                ]

    output_file = '3lxl'
    legends = [file_list[0][1], file_list[1][1], file_list[2][1]]
    wt_file, sp_file, dp_file = file_list[0][0], file_list[1][0], file_list[2][0]
    
    file_name = f'rmsf-{"".join(output_file)}-diff.png'
    output_path = os.path.join(output_folder, file_name)
    plot_data_with_difference(sp_file, dp_file, wt_file, y_range=y_range, offset=offset, save_fig_name=output_path, legends=legends)

    output_file = '3lxk'
    legends = [file_list[3][1], file_list[4][1], file_list[5][1]]
    wt_file, sp_file, dp_file = file_list[3][0], file_list[4][0], file_list[5][0]
    
    file_name = f'rmsf-{"".join(output_file)}-diff.png'
    output_path = os.path.join(output_folder, file_name)
    plot_data_with_difference(sp_file, dp_file, wt_file, y_range=y_range, offset=offset, save_fig_name=output_path, legends=legends)

    