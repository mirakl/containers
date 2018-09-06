## The dentry cache filler

Sometimes you need to investigate the dentry cache filling and cleanup by the kernel. This container will create a lot of negative dentry cache entries by using the stat command on a lot of random unexisting files.

It prints the dentry cache statistics (from /proc/slabinfo) every 1000 files

# Sample output : 

    Dentry cache - Active: 458128 Total: 812490 Size: 155998080 bytes
    Dentry cache - Active: 460378 Total: 814737 Size: 156429504 bytes
    Dentry cache - Active: 462373 Total: 816732 Size: 156812544 bytes
    Dentry cache - Active: 464219 Total: 818643 Size: 157179456 bytes
    Dentry cache - Active: 466209 Total: 820680 Size: 157570560 bytes
    Dentry cache - Active: 468276 Total: 822822 Size: 157981824 bytes

# Usage : 

Run docker image directly :
    docker run mirakl/dentry-cache-filler

Build & run : 
    make run

