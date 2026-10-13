sudo mount -U 407ccbb6-b29c-4aef-8b33-1776cf2be7c3 /mnt/Fedora44
sudo mount -U 17264ae4-05ef-4b6b-a41f-8fbdef0a8d12 /mnt/Fedora44/root01/boot

sudo chroot /mnt/Fedora44/root01

sudo umount -R /mnt/Fedora44
