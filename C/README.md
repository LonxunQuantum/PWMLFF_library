**summary**
    
    This directory includes the AIMD trajectories of the C Slab 80 atomic system at temperatures of 300K(500 images), 1000K(500 images), and 2000K(500 images)

**The data cloud drive link**

      https://pan.baidu.com/s/1-vXPh2MBxA1h2vWkVkStsA?pwd=pwmt 

   You could also scan this QR code to download.

   ![Alt text](C_QR.png)
   
**PWmat version** 
    
    20230616

**etot.input**

    8  1
    JOB = MD
    MD_DETAIL = 2 500 1 300 300
    XCFUNCTIONAL = PBE
    Ecut = 60
    ECUT2 = 240
    MP_N123 = 7 5 1 0 0 0 3
    ENERGY_DECOMP = T
    IN.ATOM = atom.config
    IN.PSP1 = C.SG15.PBE.UPF
    OUT.STRESS = T

**MD initial configuration**

![](/C/POSCAR.png)



