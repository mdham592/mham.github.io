# Cyber Defender's "Reveal Lab" write-up.

## Scenario
"You are a forensic investigator at a financial institution, and your SIEM flagged unusual activity on a workstation with access to sensitive financial data. Suspecting a breach, you received a memory dump from the compromised machine. Your task is to analyze the memory for signs of compromise, trace the anomaly's origin, and assess its scope to contain the incident effectively."

## Question 1
### "Identifying the name of the malicious process helps understand the nature of the attack. What is the name of the malicious process?"

Using volatility, I listed all of the running processes at the time and reviewed the list until something stood out.

Command used:
<pre>
sudo python3 vol.py -f mem.dmp windows.pslist
</pre>
<br> <br>
![suspicious_processes](./Reveal_Lab/suspicious_processes.png)
<br> <br>

## Question 2
### "Knowing the parent process ID (PPID) of the malicious process aids in tracing the process hierarchy and understanding the attack flow. What is the parent PID of the malicious process?"

Listing the running processes also revealed the PID.

<br> <br>
![parent_pid](./Reveal_Lab/ppid_suspicious_processes.png)
<br> <br>
## Question 3
### "Determining the file name used by the malware for executing the second-stage payload is crucial for identifying subsequent malicious activities. What is the file name that the malware uses to execute the second-stage payload?"

I reviewed the command line activity using volatility to determine the file names used by the malware for the second-stage payload.

Command used:
<pre>
sudo python3 vol.py -f mem.dmp windows.cmdline
</pre>
<br> <br>
![filename](./Reveal_Lab/filename.png)
<br> <br>
## Question 4
### "Identifying the shared directory on the remote server helps trace the resources targeted by the attacker. What is the name of the shared directory being accessed on the remote server?"

The file share name can also be found in the command line history.

<br> <br>
![directory](./Reveal_Lab/directory.png)
<br> <br>

## Question 5
### "What is the MITRE ATT&CK sub-technique ID that describes the execution of a second-stage payload using a Windows utility to run the malicious file?"
<br> <br>
Tactic [T1218.011](https://attack.mitre.org/techniques/T1218/011/), "System Binary Proxy Execution: Rundll32" applies to this activity as Rundll32 was used to run the second-stage payload.
<br> <br>

## Question 6
### Identifying the username under which the malicious process runs helps in assessing the compromised account and its potential impact. What is the username that the malicious process runs under?

Using the getsids option in Volitliy, it mapped the user associated with the PowerShell activity. 

Command used:
<pre>
sudo python3 vol.py -f mem.dmp getsids
</pre>
<br> <br>
![User](./Reveal_Lab/user.png)
<br> <br>
## Question 7
### Knowing the name of the malware family is essential for correlating the attack with known threats and developing appropriate defenses. What is the name of the malware family?

Using the IP of the remote share server, I used Virustotal to confirm the malware family to be "STRELASTEALER."

https://www.virustotal.com/gui/ip-address/45.9.74.32
<br> <br>
![vt](./Reveal_Lab/vt.png)
<br> <br>

