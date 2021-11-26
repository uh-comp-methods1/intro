# Installation on hub.cs.helsinki.fi

1. If you are not in the UH network, you need to establish first a VPN connection, see the [instructions](#vpn-connection) below
2. Log into `turso.cs.helsinki.fi` by opening a terminal and running
```
ssh your_username@turso.cs.helsinki.fi
```
3. Install the Python environment on `turso` by running
```
curl -O https://raw.githubusercontent.com/uh-comp-methods1/intro/main/docs/install_turso.sh
bash install_turso.sh
```

The last step takes a while, so wait patiently. After it is finished, you can close the connection to `turso`. 

## VPN connection

See the [instructions](https://helpdesk.it.helsinki.fi/en/help/5190) at IT-Helpdesk. Those preferring the Linux command line can use `openvpn` with this [configuration](https://cubbli.cs.helsinki.fi/hy-vpn-tun.ovpn), see the [instructions](https://wiki.helsinki.fi/display/it4sci/Remote+access+to+University+resources).


