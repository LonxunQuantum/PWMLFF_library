**summary**

      This directory includes 9791 images of Mg system. 

<div align="left">
<img src="image.png" width = "80%" />
</div>

#
**pw1**

      3672 images (36 atoms) dynamics temperature 300K
     
**pw2**

      3295 images (36 atoms) dynamics temperature 500K
     
**pw3**

      3267 images (36 atoms) dynamics temperature 800K
     
**pw5**

      918 images (36 atoms) dynamics temperature 300K
      
**pw6**

      823 images (36 atoms) dynamics temperature 500K
      
**pw7**

      816 images (36 atoms) dynamics temperature 800K
      

**PWmat version** 
    
    ***

**etot.input**

    ***

**MD initial configuration**


# **models**

We provide models trained with different optimizers, batch sizes, and GPU configurations.

Due to limitations on GitHub, we have only uploaded models with batch sizes of 1, 16, and 32. For the `complete set of model data, please visit the corresponding Baidu Netdisk link for downloading`.

For example:
```
LKF_bs512_t1/
------------/best.pth.tar
------------/checkpoint.pth.tar
------------/dp_torch2_best.cpkt
------------/dp_torch2.cpkt
------------/epoch_train.dat
------------/epoch_valid.dat
------------/train_loss.png
```
Here, `"LKF"` refers to using the `RLEKF optimizer`, and `"adam"` indicates training using the `Adam optimizer`. 

`"bs512"` represents a `batch_size` of `512`.

In directories that contain "GPU" in their names, the number following "GPU" indicates the number of GPUs used. Please note that` multi-GPU training has not been added to the PWMLFF2024.3 version yet`.

Regarding the model names, if the name is `"best.pth.tar"` or `"checkpoint.pth.tar"`, it means that the model was `trained using an earlier version` of PWMLFF that is no longer supported in the new version. We provide model conversion, and the corresponding converted model names are `"dp_torch2_best.cpkt"` and `"dp_torch2.cpkt"`.

Models with `"best"` in their names indicate the model with the `lowest validation loss` during the training process, while others represent the model at the end of the last epoch.

`"train_loss.png"` shows the decreasing trend of the training loss during model training. The data is sourced from the `"epoch_train.dat"` file in the same directory. Since the validation loss is only saved for the last epoch, it is written below the title instead of being plotted on the graph.
