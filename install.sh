echo "Instalacja pyNotify!"
START_DIR=`pwd`
sudo apt-get install gir1.2-notify-0.7
sudo ln -sf $START_DIR/pyNotify.py          /usr/bin/pyNotify
sudo ln -sf $START_DIR/pyReadNotify.py      /usr/bin/pyReadNotify
