# macer
a mac address changer for linux

## usage
this will show you your network interfaces and their mac addresses

```bash
python macer.py 
```
you can change your selected interface mac address like this

```bash
python macer.py -i [selected interface] -m [new mac address]
```

an example

```bash
python macer.py -i eth0 -m 00:11:22:33:44:55
