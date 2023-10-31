**summary**
    
    This directory includes the AIMD trajectories of the CH4 system at temperatures of 300K(1000 images), 500K(1000 images), 1000K(1000 images), and 1200K(1000 images)

**PWmat version** 
    
     20230616

**CH3CH2OH etot.input**

    8  1
    JOB = MD
    MD_DETAIL = 2 500 1 100 100 #for 500K data
    XCFUNCTIONAL = PBE
    Ecut = 60
    ECUT2 = 240
    MP_N123 = 1 1 1 0 0 0 3
    ENERGY_DECOMP = T
    IN.ATOM = atom.config
    IN.PSP1 = C.SG15.PBE.UPF
    IN.PSP2 = H.SG15.PBE.UPF
    IN.PSP2 = O.SG15.PBE.UPF
    OUT.STRESS = T

**MD initial configuration**

![](/CH4/POSCAR.png)



