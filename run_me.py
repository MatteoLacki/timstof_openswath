ssh immumz@graham.computecanada.ca

# creaat session
# tmux new -s matteo
tmux attach-session -t matteo
cd /home/immumz/projects/def-hroest/immumz
cd /home/immumz/projects/def-hroest/immumz/dia-pasef/src

cd /home/immumz/projects/def-hroest/immumz/data # data
cd /home/immumz/projects/def-hroest/immumz/results # results


# virtual env
source /project/6011811/bin/pyenv_27/bin/activate
cd /home/immumz/projects/def-hroest/immumz/dia-pasef/src/diapysef

# test run
sbatch --time 3:00:00 "./scripts/convertTDFtoMzML.py -a /home/immumz/projects/def-hroest/immumz/data/191203_AUR_400ngHeLa_90min_MIDIAv1_100ms_CE10_Slot1-1_1_1400.d -o /home/immumz/projects/def-hroest/immumz/results/test/test.mzML --total_number_overlap_mass_scans 10 --merge 3 --framerange 0 100"
sbatch --time 3:00:00 test.sh


# full run
./scripts/convertTDFtoMzML.py -a /home/immumz/projects/def-hroest/immumz/data/191203_AUR_400ngHeLa_90min_MIDIAv1_100ms_CE10_Slot1-1_1_1400.d -o /home/immumz/projects/def-hroest/immumz/results/191203_AUR_400ngHeLa_90min_MIDIAv1_100ms_CE10_Slot1-1_1_1400/midia.mzML --total_number_overlap_mass_scans 10 --merge 3
# killed... 

./scripts/convertTDFtoMzML.py -a /home/immumz/projects/def-hroest/immumz/data/191203_AUR_400ngHeLa_90min_MIDIAv2_100ms_Slot1-1_1_1402.d -o /home/immumz/projects/def-hroest/immumz/results/191203_AUR_400ngHeLa_90min_MIDIAv2_100ms_Slot1-1_1_1402/midia.mzML --total_number_overlap_mass_scans 10 --merge 3 --verbose 10


#htop
htop -u immumz