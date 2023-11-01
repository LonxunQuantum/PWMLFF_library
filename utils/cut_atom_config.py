from extract_movement import Image, MOVEMENT
import os, sys
import shutil

def cut_atom_config(workDir, type):
    if not os.path.exists(workDir):
        raise FileNotFoundError(workDir+'  is not exist!')
    res = []
    for path,dirList,fileList in os.walk(workDir):
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
        if type == "1":
            cut_atom_config_from_movement(mvm)
        if type == "2":
            cut_movement_to_multi(mvm)
        os.chdir(cwd)

def cut_movement_to_multi(mvm:MOVEMENT, cut_num:int=3000):
    for i, start in enumerate(range(0, mvm.image_nums, cut_num)):
        end = start + cut_num if start + cut_num < mvm.image_nums else mvm.image_nums
        if start >= end:
            continue
        save_dir = "{}_{}".format(start, end)
        if os.path.exists(save_dir) is False:
            os.makedirs(save_dir)
        save_file = os.path.join(save_dir, "MOVEMENT")
        with open(save_file, 'w') as wf:
            for mvm_image in mvm.image_list[start:end]:
                for line in mvm_image.content:
                    wf.write(line)
        print("{} split: {} with {} images".format(os.path.abspath(save_dir), save_file, end-start))
        os.system('zip -r {}.zip {}/'.format(save_dir, save_dir))
        shutil.rmtree(save_dir)
        # os.remove("MOVEMENT")
        
    
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
    os.chdir("/data/home/wuxingxing/datas/PWMLFF_library/Si/Si_39988images")
    parser.add_argument('-w', '--work_dir', help='specify stored directory', type=str, default=os.getcwd())
    parser.add_argument('-t', '--type', help='specify stored directory', type=str, default="2")

    args = parser.parse_args()
    cut_atom_config(args.work_dir, args.type)
