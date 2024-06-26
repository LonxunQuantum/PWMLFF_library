# download

[**The data cloud drive link**](https://pan.baidu.com/s/1qohKH2vkvqjK8wBlbFg3NQ?pwd=pwmt)

```
https://pan.baidu.com/s/1qohKH2vkvqjK8wBlbFg3NQ?pwd=pwmt
```
   
   You could also scan this QR code to download.

![Alt text](Mg_QR.png)
   
# Mg_2600images

**summary**
    
    This directory includes the AIMD trajectories of the Mg bulk 108 atomic system at temperatures of 300K(600 images), 500K(1000 images), 800K(1000 images).

**PWmat version** 
    
    300K data with 20221214 version
    500K data with 20230418 version
    800K data with 20230418 version

**etot.input**

    4 1
    in.atom = atom.config
    IN.PSP1 = Mg.SG15.PBE.UPF
    Ecut = 50
    Ecut2 = 200
    job = md

    md_detail = 2, 1000, 2.0, 800.000000, 800.000000 #for 800K data
    md_detail = 2, 1000, 2.0, 500.000000, 500.000000 #for 500K data
    md_detail = 2, 600, 2.0, 300.000000, 300.000000 #for 300K data
    
    mp_n123 = 1 1 1 0 0 0 2
    xcfunctional = GGA
    E_error = 0
    Rho_error = 1E-5
    SCF_ITER0_1 =    6   4    3    0.0000     0.20000    2
    SCF_ITER0_2 =   94   4    3    1.0000     0.20000    2
    SCF_ITER1_1 =   40   4    3    1.0000     0.20000    2

    OUT.WG = F 
    OUT.RHO = F 
    OUT.VR = F 
    OUT.FORCE = T 
    OUT.STRESS = T 
    OUT.MLMD = T
    ENERGY_DECOMP = T, 1

**MD initial configuration**

![](./Mg_2600images/POSCAR.png)


# Mg_12791images
**summary**

      This directory includes 9791 images of Mg system. 

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
