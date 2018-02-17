 mount -o remount, rw / 
cd /usr/lib/python2.7/site-packages/motioneye/template
curl -H 'Cache-control: no-cache' -o main.html  https://raw.githubusercontent.com/retributionxd/motioneye/master/motioneye/templates/main.html  
cd ~
curl -H 'Cache-control: no-cache' -o gpioDude.py  https://raw.githubusercontent.com/retributionxd/motioneye/master/gpioDude.py
echo 'python /root/gpioDude.py &' >> /etc/init.d/S85motioneye
cat /etc/init.d/S85motioneye
