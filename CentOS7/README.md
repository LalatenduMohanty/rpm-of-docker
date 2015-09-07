docker pull centos

docker save --output=centos.tar centos

tar czvf centos-docker-image-1.0.tar.gz centos.tar README.md centos-7.ks

md5sum centos-docker-image-1.0.tar.gz >sources

fedpkg --dist f22 srpm

mock -r fedora-22-x86_64 centos-docker-image-1.0-1.fc22.src.rpm
