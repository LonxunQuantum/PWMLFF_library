import numpy as np
import matplotlib.pyplot as plt

size = 20
dirs = ["Al", "Alloy","HfO2","LiGePS"]
methods = {"dp":"DP","nep_lkf":"NEP"}
c_dp = plt.cm.Reds(np.linspace(1.,.4, len(dirs)))
c_nep = plt.cm.Blues(np.linspace(1., .4, len(dirs)))
markers = ["o","*","s","d"]
marker_2 = ["s","^"]

def plot_energy():
    for method in methods:
        for ii,_dir in enumerate(dirs):
            if method == "dp":
                c = c_dp[ii]
            elif method == "nep_lkf":
                c = c_nep[ii]
            data = np.loadtxt("../%s/%s/model_record/epoch_valid.dat"%(_dir,method),skiprows=1)
            plt.plot(data[:,0],data[:,2],lw=1.,c=c,label="%s-%s"%(_dir,methods[method]),marker=markers[ii],alpha=.6,markersize=3.5,markeredgecolor=None)
    plt.xlim([0,110])
    plt.xticks(size=size-4)
    plt.yscale("log")
    plt.yticks(size=size-4)
    plt.xlabel("Epoch",size=size)
    plt.ylabel("RMSE of Energy (eV/atom)",size=size)
    plt.legend(fontsize=size-6)
    plt.tight_layout()
    plt.savefig("Energy.png",dpi=360)
    plt.close()

def plot_force():
    for method in methods:
        for ii,_dir in enumerate(dirs):
            if method == "dp":
                c = c_dp[ii]
            elif method == "nep_lkf":
                c = c_nep[ii]
            data = np.loadtxt("../%s/%s/model_record/epoch_valid.dat"%(_dir,method),skiprows=1)
            plt.plot(data[:,0],data[:,3],lw=1.,c=c,label="%s-%s"%(_dir,methods[method]),marker=markers[ii],alpha=.6,markersize=3.5,markeredgecolor=None)
    plt.xlim([0,110])
    plt.ylim([0.01,0.3])
    plt.xticks(size=size-4)
    plt.yscale("log")
    plt.yticks(size=size-4)
    plt.xlabel("Epoch",size=size)
    plt.ylabel(r"RMSE of Force (eV/$\mathrm{\AA}$)",size=size)
    plt.legend(fontsize=size-10)
    plt.tight_layout()
    plt.savefig("Force.png",dpi=360)
    plt.close()

def plot_system():
    for _dir in dirs:
        fig = plt.figure(dpi=360)
        ax1 = fig.add_subplot(111)
        ax2 = ax1.twinx()
        plt.plot(-1,-1,lw=1,c="k",marker=marker_2[0],markersize=5.,label="DP")
        plt.plot(-1,-1,lw=1,c="k",marker=marker_2[1],markersize=5.,label="NEP")
        for ii,method in enumerate(methods):
            data = np.loadtxt("../%s/%s/model_record/epoch_valid.dat"%(_dir,method),skiprows=1)
            ax1.plot(data[:,0],data[:,2],lw=1,c="C0",marker=marker_2[ii],markersize=4.5)
            ax2.plot(data[:,0],data[:,3],lw=1,c="C1",marker=marker_2[ii],markersize=4.5)
        plt.xlim([0,45])
        ax1.set_xticks(range(0,41,10))
        ax1.set_xticklabels(range(0,41,10),size=size-4)
        ax1.set_yscale("log")
        ax2.set_yscale("log")
        ax1.set_ylim([1e-4,.3])
        ax2.set_ylim([1e-4,.3])
        ax1.set_yticks([1e-4,1e-3,1e-2,.1])
        ax1.set_yticklabels(["10$^{-4}$","10$^{-3}$","10$^{-2}$","10$^{-1}$"],size=size-4)
        ax2.set_yticks([1e-4,1e-3,1e-2,.1])
        ax2.set_yticklabels(["10$^{-4}$","10$^{-3}$","10$^{-2}$","10$^{-1}$"],size=size-4)
        ax1.set_xlabel("Epoch",size=size)
        ax1.set_ylabel("RMSE of Energy (eV/atom)",size=size)
        ax2.set_ylabel("RMSE of Force (eV/$\mathrm{\AA}$)",size=size)
        plt.gca().spines["left"].set_color("C0")
        plt.gca().spines["right"].set_color("C1")
        plt.gca().spines["left"].set_linewidth(2)
        plt.gca().spines["right"].set_linewidth(2)
        plt.title(_dir,size=size+4)
        plt.legend(fontsize=size-6)
        plt.tight_layout()
        plt.savefig("%s.png"%_dir,dpi=360)
        plt.close()

if __name__ == "__main__":
#    plot_energy()
#    plot_force()
    plot_system()
