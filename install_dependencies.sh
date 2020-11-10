# INSTALL PYTHON DEPENDENCIES
pip3 install -r requirements.txt

# INSTALL BLEURT
pip3 install --upgrade pip
git clone https://github.com/google-research/bleurt.git
cd bleurt
pip3 install . --user
wget https://storage.googleapis.com/bleurt-oss/bleurt-base-128.zip
unzip bleurt-base-128.zip
rm bleurt-base-128.zip 
cd ../
mv bleurt metrics

# INSTALL METEOR
wget https://www.cs.cmu.edu/~alavie/METEOR/download/meteor-1.5.tar.gz
tar -xvf meteor-1.5.tar.gz
mv meteor-1.5 metrics
rm meteor-1.5.tar.gz