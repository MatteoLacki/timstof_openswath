ssh immumz@graham.computecanada.ca
tmux attach-session -t matteo
cd /home/immumz/projects/def-hroest/immumz
cd /home/immumz/projects/def-hroest/immumz/dia-pasef/src

cd /home/immumz/projects/def-hroest/immumz/data # data
cd /home/immumz/projects/def-hroest/immumz/results # results


# virtual env
source /project/6011811/bin/pyenv_27/bin/activate
cd /home/immumz/projects/def-hroest/immumz/dia-pasef/src/diapysef

# test run
./scripts/convertTDFtoMzML.py -a /home/immumz/projects/def-hroest/immumz/data/191203_AUR_400ngHeLa_90min_MIDIAv1_100ms_CE10_Slot1-1_1_1400.d -o /home/immumz/projects/def-hroest/immumz/results/test.mzML --total_number_overlap_mass_scans 10 --merge 3 --framerange 0 100

# full run
/scripts/convertTDFtoMzML.py -a /home/immumz/projects/def-hroest/immumz/data/191203_AUR_400ngHeLa_90min_MIDIAv1_100ms_CE10_Slot1-1_1_1400.d -o /home/immumz/projects/def-hroest/immumz/results/test.mzML --total_number_overlap_mass_scans 10 --merge 3 --framerange 0 100

