**summary**
    
    This directory includes the AIMD trajectories of the CH3CH2OH system at temperatures of 100K(500 images), 300K(500 images), and 400K(500 images)

**PWmat version** 
    
     20230616

**CH3CH2OH etot.input**

    4  1
    JOB = MD
    MD_DETAIL = 2 500 1 100 100 #for 100K data
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

![](/CH3CH2OH/POSCAR.png)



