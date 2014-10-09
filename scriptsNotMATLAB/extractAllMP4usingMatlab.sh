#!/bin/bash
OutDir=/ihome/kinnaird/myFeatures
mkdir -p "${OutDir}"
ls -d mazurka06-1 | while read currentDir
do
  cd "${currentDir}"
  mkdir -p "${OutDir}"/"CP"/"${currentDir}"
  mkdir -p "${OutDir}"/"CLP"/"${currentDir}"
  mkdir -p "${OutDir}"/"CENS"/"${currentDir}"
  mkdir -p "${OutDir}"/"CRP"/"${currentDir}"
  mkdir -p "${OutDir}"/"CRPS"/"${currentDir}"

  mkdir -p "${OutDir}"/"CP_dist"/"${currentDir}"
  mkdir -p "${OutDir}"/"CLP_dist"/"${currentDir}"
  mkdir -p "${OutDir}"/"CENS_dist"/"${currentDir}"
  mkdir -p "${OutDir}"/"CRP_dist"/"${currentDir}"
  mkdir -p "${OutDir}"/"CRPS_dist"/"${currentDir}"

  find . -name "pid1263-01.mp4" -print | while read currentFileName
  do 
    tmpfile=/ihome/kinnaird/tmpfile.wav
    mplayer -ao pcm:file=$tmpfile "${currentFileName}" &
    wait

    matlab -nodisplay </ihome/kinnaird/extractFeatures.m > /ihome/kinnaird/tempout.txt &
    wait 
    
    currentFileName=${currentFileName:2}
    echo "${currentDir}"/"$currentFileName"
    mv /ihome/kinnaird/temp_CP.mat  "${OutDir}"/"CP"/"${currentDir}"/"${currentFileName/.mp4}_CP".mat
    mv /ihome/kinnaird/temp_CLP.mat  "${OutDir}"/"CLP"/"${currentDir}"/"${currentFileName/.mp4}_CLP".mat
    mv /ihome/kinnaird/temp_CENS.mat  "${OutDir}"/"CENS"/"${currentDir}"/"${currentFileName/.mp4}_CENS".mat
    mv /ihome/kinnaird/temp_CRP.mat  "${OutDir}"/"CRP"/"${currentDir}"/"${currentFileName/.mp4}_CRP".mat
    mv /ihome/kinnaird/temp_CRPS.mat  "${OutDir}"/"CRPS"/"${currentDir}"/"${currentFileName/.mp4}_CRPS".mat

    mv /ihome/kinnaird/temp_CP_dist.mat  "${OutDir}"/"CP_dist"/"${currentDir}"/"${currentFileName/.mp4}_CP_dist".mat
    mv /ihome/kinnaird/temp_CLP_dist.mat  "${OutDir}"/"CLP_dist"/"${currentDir}"/"${currentFileName/.mp4}_CLP_dist".mat
    mv /ihome/kinnaird/temp_CENS_dist.mat  "${OutDir}"/"CENS_dist"/"${currentDir}"/"${currentFileName/.mp4}_CENS_dist".mat
    mv /ihome/kinnaird/temp_CRP_dist.mat  "${OutDir}"/"CRP_dist"/"${currentDir}"/"${currentFileName/.mp4}_CRP_dist".mat
    mv /ihome/kinnaird/temp_CRPS_dist.mat  "${OutDir}"/"CRPS_dist"/"${currentDir}"/"${currentFileName/.mp4}_CRPS_dist".mat

    # rm $tmpfile

  done
  cd ..
done
