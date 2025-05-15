
# Secure File Transfer Utility
[Server / Decrypter](./decrypter.py).

[Client / Encrypter](./encrypter.py).




### Resources used:

[https://linux.die.net/man/8/iptables](https://gnupg.readthedocs.io/en/latest/)


## Why this project was important:

Throughout school and my career, file encryption has always been taught to me as critical to improving an organization's overall security posture. However, this project was the first time I got to experience using encryption at a lower level. I learned to use Python to generate a GPG key pair. I sent the public key to my Linux VM and wrote two scripts to automate encrypting, decrypting, and sending the encrypted files back to my Windows host while the files were encrypted.  It was interesting to learn that GPG doesn't require you to hard-code a filepath or the keys' content inside the program; it automatically looks inside the encrypted files' content for a key ID, to correlate the public keys' encryption back to the private key.  

## Program and code walk-through:

To prepare the encrypter and decrypter programs to work, I first needed to create files to upload and a file path for my Windows machine to save the files.

![Ping SC1.PNG](./preupload_server1.PNG)

![Ping SC1.PNG](./preupload_server2.PNG)

![Ping SC1.PNG](./preupload_clientfiles.PNG)



Running the decrypter script sets a socket listener on port 7777 ready to handle incoming requests.

![Ping SC1.PNG](./decrypter_server_listening.PNG)

![Ping SC1.PNG](./server_listen.PNG)



While the decrypter script waits for the file upload activity, the encrypter script reads in the public key to encrypt the upload files.

![Ping SC1.PNG](./public_key_usage.PNG)

![Ping SC1.PNG](./Client_encrypt_file.PNG)



The encrypter script would then send the encrypted files to the Windows device.

![Ping SC1.PNG](./Client_call_sendfile.PNG)

![Ping SC1.PNG](./client_sendfile_method.PNG)

![Ping SC1.PNG](./encrypter_output_sc.PNG)



The Windows device would receive the files and decrypt them with the private key stored on the device.
![Ping SC1.PNG](./decrypter_output_sc.PNG)
![Ping SC1.PNG](./postupload_server1.PNG)
![Ping SC1.PNG](./postupload_server2.PNG)



### Lab Screenshot
![Ping SC1.PNG](./full_sc.PNG)


## Future Improvements
If this program is to be used in a professional setting, I would first remove the hard-coded passphrase from the decrypter script. I would also improve the encrypter script to consistently monitor a directory for new files that the user would want to move to the "server" so they do not need to rerun the script every time.
