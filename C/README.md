**summary**
    
    This directory includes the AIMD trajectories of the Ni bulk 108 atomic system at temperatures of 300K(500 images), 1000K(500 images), and 200K(500 images)

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



