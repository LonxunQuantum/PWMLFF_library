**summary**:
    
    This directory includes the AIMD trajectories of the Si bulk 64 atomic system at temperatures of 500K(600 images), 800K(1000 images), 900K(1000 images), 1100K(1000 images), and 1300K(1000 images).

**PWmat version**: 
    
    20230514

**etot.input**:

    4 1
    in.atom = atom.config
    IN.PSP1 = Ni.SG15.PBE.UPF
    Ecut = 60
    Ecut2 = 240
    job = md
    md_detail = 2, 1000, 2.0, 1100.000000, 1100.000000
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


**structure:**

![](/ni/POSCAR.png)



