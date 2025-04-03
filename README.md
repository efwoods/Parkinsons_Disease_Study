<div align="center">
     <a href="https://efwoods.github.io/Parkinsons_Disease_Study/">
          <img src="https://github.com/efwoods/Parkinsons_Disease_Study/blob/main/img/3D_Plot_of_Correlated_fALFF.png?raw=true" alt="3D-Visualization"  width="800">
     </a>
</div>

# [Parkinson's Disease Study: Written Report & Analysis](https://github.com/efwoods/Parkinsons_Disease_Study/blob/main/report/HW_Module3_Evan_Woods.pdf)

This study is a personal work that investigates the functional connectivity of brains of cognitively normal patients, Parkinson's disease patients with mild cognitive impairment, and Parkinson's disease patients with dementia. 
This project is a part of the edX MITx 6.419x Data Analysis: Statistical Modeling and Computation in Applications course. It implements data acquired from [OpenNeuro: Parkinson's disease, functional connectivity, and cognition](https://openneuro.org/datasets/ds004392/versions/1.0.0) and is cited below.

This project clustered the patients using the fractional amplitude low-frequency fluctuation (fALFF) of the BOLD signal of the right substantia nigra. 

<p align="center">
  <img src="https://github.com/efwoods/Parkinsons_Disease_Study/blob/main/img/BOLD.png" alt="BOLD Signal Example" width="400">
  <img src="https://github.com/efwoods/Parkinsons_Disease_Study/blob/main/img/fALFF_SN_Spectral_Clustering.png" alt="Spectral Clustering Example" width="425">
</p>

A network of similar brain activity was created per patient group. Green nodes in the network below indicate brain regions that have activity similar to the right substantia nigra  for the cognitively normal patients.
Red nodes indicate like activity to the right substantia nigra in patients with Parkinson's Disease Dementia. The fALFF of parkinson's disease dementia patients is lower than the cognitively normal patients.

<div align="center">
     <img src="https://github.com/efwoods/Parkinsons_Disease_Study/blob/main/img/statistically_significant_correlated_regions_sn_cogn_pdd_graph.png" alt="2D-Visualization"  width="800">
</div>

The 3D coordinates were calculated and the visualization of the neural activity is available [at the github page for this repository](https://efwoods.github.io/Parkinsons_Disease_Study/).

The detailed report of the methods, results, and discussion [are available at this link](https://github.com/efwoods/Parkinsons_Disease_Study/blob/main/report/HW_Module3_Evan_Woods.pdf).

## Data Citation
Korey P. Wylie and Benzi M. Kluger and Luis D. Medina and Samantha K. Holden and Eugene Kronberg and Jason R. Tregellas and Isabelle Buard (2023). Parkinson's disease, functional connectivity, and cognition. OpenNeuro. [Dataset] doi: doi:10.18112/openneuro.ds004392.v1.0.0

### Original Dataset Description
Title: Parkinson's disease, functional connectivity, and cognition.

This dataset contains patients diagnosed with Parkinson's disease, scanned with resting state fMRI, and who underwent a neurocognitive test battery. Included are cognitively normal patients, Parkinson's disease with mild cognitive impairment, and Parkinson's disease dementia.
