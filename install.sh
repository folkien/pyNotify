echo "Instalacja pyNotify!"
START_DIR=`pwd`
cd /usr/bin
sudo ln -sf $START_DIR/pyNotify.py ./pyNotify
sudo ln -sf $START_DIR/pyReadNotify.py ./pyReadNotify
