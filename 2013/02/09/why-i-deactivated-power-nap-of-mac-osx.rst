Why I deactivated Power Nap of Mac OS X
=======================================

:public: True
:tags: ["mac", "os x", "timemachine"]
:summary: "I backup my Mac Book to my NAS but Power Nap broken it two times. :("

I really like the idea behind Power Nap of the OS X but I got big trouble afterwards. I backup my Mac with TimeMachine on my NAS (based on Debian Squeeze) with netatalk, which works sweet. Oh, by the way guys of netatalk your are great.

.. image:: /static/img/2013-02-09-why-i-deactivated-power-nap-of-mac-osx/timemachine.png
    :scale: 60%

My new MacBook Air backup fine to this share also in his Power Nap (with PowerAdapter) but often I took it in to my bag and run frantic out of my flat. In this moment TimeMachine copied some new files and update some hardlinks and out of this the sparseimage with the backup data broke up two times. The first one I was able to repair the image but the second one died.

For interested people::

    Verifying volume “Time Machine Backups”
    Checking file systemChecking Journaled HFS Plus volume.
    Detected a case-sensitive volume.
    Checking extents overflow file.
    Checking catalog file.
    Incorrect number of thread records
    Incorrect number of thread records
    Checking multi-linked files.
    Incorrect number of file hard links
    Checking catalog hierarchy.
    Invalid directory item count
    (It should be 71659 instead of 71656)
    Invalid directory item count
    (It should be 6783 instead of 6780)
    Invalid directory item count
    (It should be 71 instead of 69)
    Missing thread record (id = 1337771)
    Invalid directory item count
    (It should be 0 instead of 4)
    Missing thread record (id = 1337777)
    Invalid directory item count
    (It should be 0 instead of 11)
    Incorrect folder count in a directory (id = 19)
    (It should be 6783 instead of 6780)
    Incorrect folder count in a directory (id = 1337771)
    (It should be 0 instead of 1)
    Incorrect folder count in a directory (id = 1337777)
    (It should be 0 instead of 2)
    Checking extended attributes file.
    Incorrect number of extended attributes
    (It should be 779961 instead of 779953)
    Incorrect number of Access Control Lists
    (It should be 779911 instead of 779903)
    Checking multi-linked directories.
    Incorrect number of directory hard links
    Checking volume bitmap.
    Volume bitmap needs minor repair for under-allocation
    Checking volume information.
    Invalid volume free block count
    (It should be 672247867 instead of 675275581)
    Volume header needs minor repair
    The volume Time Machine Backups was found corrupt and needs to be repaired.
    Error: This disk needs to be repaired. Click Repair Disk.

Sorry I forgot to copy the log of the repair process but the result was hdutils isn't able to repair the volume. Now I started a fresh backup with disabled Power Nap.