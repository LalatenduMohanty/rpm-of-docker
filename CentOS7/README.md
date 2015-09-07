docker pull centos

docker save --output=centos.tar centos

tar czvf centos-docker-image-1.0.tar.gz centos.tar README centos-7.ks

fedpkg --dist f22 srpm

mock -r fedora-22-x86_64 centos-docker-image-1.0-1.fc22.src.rpm
