import MDAnalysis as mda
from MDAnalysis.analysis import helix_analysis as hel
import matplotlib.pyplot as plt

simulacio = mda.Universe("protein/simulation/input/system.psf","protein/simulation/input/system.pdb","protein/simulation/MD_100ns_v2/MD.dcd") #Carregar els arxius psf i dcd
helix = simulacio.select_atoms("resid 23-34") #Seleccionem la part de la helix


h = hel.HELANAL(helix,ref_axis=[0, 0, 1]).run() #Calcular les propietats

titols = h.results.summary.keys()#Ens ensenya l'estructura dels resultats per a decidir que volem graficar
print(titols)

#Graficar els resultats desitjats 
plt.plot(h.results.local_twists.mean(axis=1)) #Twist helix 
plt.xlabel("Frame")
plt.ylabel("Helix Average twist (degrees)")
plt.show()
