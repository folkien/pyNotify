echo "Instalacja pyNotify!"
START_DIR=`pwd`
cd /usr/bin
sudo ln -s $START_DIR/pyNotify.py ./pyNotify
sudo ln -s $START_DIR/pyReadNotify.py ./pyReadNotify
