**summary**

      This directory includes 10263 images of CuO system. 
   
[**The data cloud drive link**](https://pan.baidu.com/s/158e0r2BYuoLKCeaQDdg43w?pwd=pwmt)

```
https://pan.baidu.com/s/158e0r2BYuoLKCeaQDdg43w?pwd=pwmt
```
   
You could also scan this QR code to download.

   ![Alt text](CuO_QR.png)

<div align="left">
<img src="image.png" width = "80%" />
</div>


**PW1**
   
      1440 images (64 atoms) dynamics temperature 300K

    
**PW11**
   
      1839 images (64 atoms) dynamics temperature 300K

    
**PW111**
   
      1322 images (64 atoms) dynamics temperature 500K

    
**PW1111**
   
      1844 images (64 atoms) dynamics temperature 800K

    
**PW11111**
   
      1768 images (64 atoms) dynamics temperature 1000K

    
**PW2**
   
      360 images (64 atoms)  dynamics temperature 300K

    
**PW22**
   
      459 images (64 atoms)  dynamics temperature 300K

    
**PW222**
   
      330 images (64 atoms)  dynamics temperature 500K

    
**PW2222**
   
      460 images (64 atoms)  dynamics temperature 800K

    
**PW22222**
   
      441 images (64 atoms)  dynamics temperature 1000K


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
