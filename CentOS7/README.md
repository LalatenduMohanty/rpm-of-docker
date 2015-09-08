docker pull centos

docker save --output=centos.tar centos

tar czvf centos-docker-image-1.0.tar.gz centos.tar README.md centos-7.ks

md5sum centos-docker-image-1.0.tar.gz >sources

fedpkg --dist f22 srpm

mock -r fedora-22-x86_64 centos-docker-image-1.0-1.fc22.src.rpm


#Test The POC

* Check that you dont have centos image
```
sudo docker images

```
* Enable the copr repo
* Install the RPM
```
sudo dnf copr enable lalatendu/centos-docker-image 
sudo dnf install centos-docker-image
```
* You should have the centos docker image now
```
sudo docker images
```
* Remove the RPM
```
sudo dnf remove centos-docker-image -y
```
