from extract_movement import Image, MOVEMENT
import os, sys

def cut_atom_config(workDir):
    if not os.path.exists(workDir):
        raise FileNotFoundError(workDir+'  is not exist!')
    res = []
    for path,dirList,fileList in os.walk(workDir):
        print(path)
        print(dirList)
        print(fileList)
        print()
        if "MOVEMENT" in fileList:
            #pm.sourceFileList.append(os.path.abspath(path))
            # use relative path
            res.append(os.path.join(path, "MOVEMENT"))
        elif "movement" in fileList:
            res.append(os.path.join(path, "movement"))
    cwd = os.getcwd()
    for d in res:
        os.chdir(os.path.dirname(d))
        file = os.path.basename(d)
        mvm = MOVEMENT(file)
        cut_atom_config_from_movement(mvm)
        os.chdir(cwd)

def cut_atom_config_from_movement(mvm: MOVEMENT, prefix=""):
    atom_config = "{}atom.config".format(prefix)
    with open(atom_config, 'w') as wf:
        for line in mvm.image_list[0].content:
            wf.write(line)
    os.system('config2poscar.x {}'.format(atom_config))

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    # parser.add_argument('-i', '--input', help='specify input movement filename', type=str, default='MOVEMENT')
    # parser.add_argument('-s', '--savepath', help='specify stored directory', type=str, default='movement_save')
    # parser.add_argument('-wt', '--work_type', help='specify work type {interval or range}', type=str, default='interval')
    
    # parser.add_argument('-t', '--interval', help='specify interval', type=int, default=10)
    # parser.add_argument('-f', '--first_range', help='specify start of range', type=int, default=0)
    # parser.add_argument('-e', '--end_range', help='specify end of range', type=int, default=1)
    os.chdir("/data/home/wuxingxing/datas/PWMLFF_library/mg")
    parser.add_argument('-w', '--work_dir', help='specify stored directory', type=str, default=os.getcwd())
    args = parser.parse_args()
    cut_atom_config(args.work_dir)
