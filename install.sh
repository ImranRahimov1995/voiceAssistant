# need to ubuntu
sudo apt-get install libportaudio2
sudo apt-get install libasound-dev

python3 -m venv venv 
source venv/bin/activate

. ./env.sh


python3 -m pip install --upgrade pip
python3 -m pip install --upgrade setuptools
pip3 install -r requeirements.txt