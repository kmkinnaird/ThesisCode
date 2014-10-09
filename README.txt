CodeForDissertation

=-=-=-=-=-=-=

This is the code as it was used for the results in my Ph.D. Dissertation "Aligned Hierarchies for Sequential Data."

An updated version will be released soon.

=-=-=-=-=-=-=

Notes for files in MATLABcode:

* For DistMat_from_FeatureVectors.m

This function computes the pairwise squared Euclidean distance between feature vectors. 

* For extractFeatures.m
This function extracts the Chroma feature vectors as well as the CLP (Chroma-Log-Pitch), CENS (Chroma Energized Normalized Statistics), and CRP (Chroma DCT-Reduced log Pitch) features in [M2007, ME2011]. As the comment notes, much of this function is based on “demoChromaToolbox.m” from the Chroma Toolbox downloaded from http://www.mpi-inf.mpg.de/resources/MIR/chromatoolbox/ and discussed [ME2011].



Notes for files in scriptsNotMATLAB:

* For all python scripts in this folder:
We would like to acknowledge Michael A. Casey, who introduced us to and helped us implement the music21 Python library (see http://web.mit.edu/music21/) in the following Python scripts. 

* For extractAllMP4usingMatlab.sh:
This Bash script was used to extract the Chroma feature vectors from Mazurka audio files. This script as presented here will not process the full directory, but a quick edit to the first line beginning with ``find'' can make this script process the full directory. 

We would also like to acknowledge Michael A. Casey again for his helpful conversations regarding feature extraction from audio files through bash. 




References:

[M2007]  M. M\”{u}ller, “Information Retrieval for Music and Motion”, Springer Verlag, 2007.

[ME2011]  M. M\”{u}ller & S. Ewert, “Chroma Toolbox: MATLAB Implementations for Extracting Variants of Chroma-Based Audio Features”, 12th International Society for Music Information Retrieval Conference, 2011. 