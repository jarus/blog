Simple IMAP Copy/Migrate/Backup script
======================================

:public: True
:tags: ["python", "imap", "backup", "mail"]

In the last weeks I spend some time to migrate my own GoogleMail account and the accounts of my parents to a own dovecot/exim server.
The reason for this migration is to get more control of my mail system. Also Google disabled the Exchange Active Sync for free accounts. Active Sync was a very nice to integrate GoogleMail accounts into iOS Devices with well worked push support.

I search for a simple script to copy mails from one IMAP server to another but there was not the perfect solution for me. The most scripts copy everything and have no possibility to select folders or map folders to another folder.

My solution was to wrote it by myself. The goal was a very simple command line interface to copy a selection of folders from one server to another.

::

    python imapcopy.py imap.googlemail.com:993 username@googlemail.com:password \
    mail.example.com "username@example.com:password" \
    "[Google Mail]/All messages" DestinationFolder


It should also work great with many messages. My archive contains over 69.000 mails. (Yes, I should clean up.)
The script doesn't have a dependencies because the imaplib_ is very impressive and useful.

You can find the script under:

.. github-repo:: jarus/imap_copy


**Update** I got one nice `pull requests <https://github.com/jarus/imap_copy/pull/3>`_ which allows limit the amount of messages to copy. Also you can skip a number of messages.

.. _imaplib: http://docs.python.org/2/library/imaplib.html
