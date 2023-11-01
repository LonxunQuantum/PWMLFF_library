**summary**
    
    This directory includes the AIMD trajectories of the CH4 system at temperatures of 300K(1000 images), 500K(1000 images), 1000K(1000 images), and 1200K(1000 images)

**The data cloud drive link**

      https://pan.baidu.com/s/1i9UOEjxEZq0wUEXpH3uvWg?pwd=ghrl
   
      Extracted code ghrl

   You could also scan this QR code to download.

   ![Alt text](CH4_QR.png)


**PWmat version** 
    
     20230616

**CH4 etot.input**

    8  1
    JOB = MD
    MD_DETAIL = 2 1000 1 300 300
    XCFUNCTIONAL = PBE
    Ecut = 60
    ECUT2 = 240
    MP_N123 = 2 2 2 0 0 0 3
    ENERGY_DECOMP = T
    IN.ATOM = atom.config
    IN.PSP1 = C.SG15.PBE.UPF
    IN.PSP2 = H.SG15.PBE.UPF
    OUT.STRESS = T

**MD initial configuration**

![](/CH4/POSCAR.png)



