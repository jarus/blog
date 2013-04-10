Simple IMAP Copy/Migrate/Backup script
======================================

:public: True
:tags: ["python", "imap", "backup", "mail"]

In the last weeks I spend some time to migrate my own GoogleMail account and the accounts of my parents to a own dovecot/exim server. In the last time I wish to have more control about my mail setup and data also Google disabled the Exchange Active Sync for free accounts which I need for push mail on my iOS devices.

I search in the WWWW for a simple script to copy mails from one IMAP server to another but there was not the perfect solution for me. The most scripts copy everything and have no possibility to select folders or map folders to another folder.

The solution was: Do it yourself.

My goal was a very simple command line interface and I think I reached this. It also works great whit many messages. I tests it with over 69.000 mails. (Yes I should clean up my mailbox)

::

    python imapcopy.py imap.googlemail.com:993 username@googlemail.com:password \
    mail.example.com "username@example.com:password" \
    "[Google Mail]/All messages" DestinationFolder


You can find the script under:

.. github-repo:: jarus/imap_copy


