---
title: 'Thunderbolt Cluster Setup Guide | SmolCluster'
date: 2026-05-09
permalink: /posts/2026/05/thunderbolt-cluster-setup-guide/
tags:
  - Distributed Setup
  - Cluster Setup
  - Thunderbolt Networking
  - Guide
---

You want to train models. You have Mac minis. You don't want to rent GPU clouds. So you **wire them together** and make a cluster.

This guide walks you through setting up a solid distributed training cluster using Thunderbolt networking for ~10-20 Gbps of pure local bandwidth, zero egress costs, and full control over every packet.

By the end, your minis will be talking to each other over dedicated Thunderbolt links while your laptop SSHes in over Wi-Fi. PyTorch FSDP, DDP, pipeline parallelism — all waiting to be explored.

---

## Why This Approach?

- **No cloud costs:** You own the hardware. Bandwidth is free.
- **Good bandwidth:** Thunderbolt = ~10-20 Gbps.
- **Low latency:** <1ms between nodes. Perfect for distributed training.
- **Simple setup:** Just enable a bridge, assign IPs, disable a firewall (will re-enable later!). Done.

---

## The Network Topology

Here's the key insight: split your traffic into two networks.

| Purpose | Network | Use For |
|---|---|---|
| **Control + Internet** | Wi-Fi | SSH, GitHub, pip installs, remote access |
| **Training Traffic** | Thunderbolt | All-reduce, gradient syncs, model data |

This keeps your training traffic on its own dedicated highway while your laptop still has internet access for control commands.

What it looks like:


#TODO
add arch.png here

Clean separation. No Wi-Fi congestion. Just throughput where it matters.

---

## Step-by-Step Setup

### 1. Enable Thunderbolt Bridge

Before opening settings, decide your coordinator machine first.

- Pick one machine as the central node: either any of the **minis** or a **MacBook** maybe.
- Connect every other Mac mini directly to this central node over Thunderbolt. This is called a **star** topology. 
- This gives you a clean star layout and makes management easier because one machine acts as the control point.


> **IMPORTANT:** Little ⚡ check!
> - Connect cluster cables only to ports that support **Thunderbolt** (look for the ⚡ symbol).
> - Using a non-Thunderbolt USB-C port is a common mistake and can cause link failures or unstable connectivity.
> - On Mac minis especially, double-check the exact port before plugging in. On newer MacBooks, many USB-C ports are Thunderbolt-capable, but you should still confirm your specific model.




Once the cabling is done, on **each Mac mini or MacBook**, open System Settings and navigate to the Thunderbolt Bridge.

If you don't see it, it should appear after you plug in the Thunderbolt cables.

### 2. Assign Static IPs

Give each node a unique static IP on the Thunderbolt network using the macOS UI.

On each mini:

1. Open **System Settings** -> **Network**.
2. Click **Thunderbolt Bridge**.
3. Click **Details...**.
4. Go to **TCP/IP**.
5. Change **Configure IPv4** from **Using DHCP** to **Manually**.
6. Enter these values:
    - **mini1**: IP Address `10.10.0.1`, Subnet Mask `255.255.255.0`
    - **mini2**: IP Address `10.10.0.2`, Subnet Mask `255.255.255.0`
    - **mini3**: IP Address `10.10.0.3`, Subnet Mask `255.255.255.0`
7. Leave **Router/Gateway** empty for this direct local link.
8. Click **OK**, then **Apply**.

Verify from Terminal:

```bash
ifconfig bridge0
```

You should see something like `inet 10.10.0.1 netmask 0xffffff00` in the output.

### 3. Test Connectivity with Ping

From your coordinator node (e.g., mini1), ping the other nodes:

```bash
ping 10.10.0.1
```

You should see:

```
64 bytes from 10.10.0.1: icmp_seq=0 ttl=64 time=0.123 ms
64 bytes from 10.10.0.1: icmp_seq=1 ttl=64 time=0.089 ms
```

**This should be ultra-fast** (<1ms). If ping is slow or times out, check:

- Are the Thunderbolt cables actually plugged in?
- Does the bridge interface exist? (`ifconfig bridge0`)
- Are the IPs actually assigned?

### 4. Disable the macOS Firewall (Optional )

This is the #1 gotcha. The macOS packet filter (PF) can silently block Thunderbolt TCP traffic. Your ping will work fine, but TCP connections will hang or fail with "No route to host" errors.

Disable it:

```bash
sudo pfctl -d
```

Verify it's off:

```bash
sudo pfctl -s info
```

Look for this in the output:

```
Status: Disabled
```

**Why does this matter?** PF is a stateful packet filter. It can block connections even if routing is fine. 

**When to use:** When you start seeing "Errno 65: No route to host" in your training code later, 90% of the time it's this and its not your routing or cabling fault. Disabling PF is a critical step in validating your cluster setup.

### 5. Test TCP Connectivity

Test actual TCP (not just ICMP ping). On coordinator node (e.g., mini1), listen on a port:

```bash
nc -l 65432
```

On one of the other nodes (e.g., mini2), try to connect:

```bash
nc 10.10.0.1 65432
```

If it works, the `nc` command will just hang (no error output). Ctrl+C to exit.

**What just happened:** Routing works. TCP is flowing. Firewall isn't blocking. You're ready for training code.

### 6. Set Up SSH Keys

Generate a key on your laptop:

```bash
ssh-keygen -t ed25519 -f ~/.ssh/macmini_cluster
```

Copy it to each node:

```bash
ssh-copy-id -i ~/.ssh/macmini_cluster.pub user@<IP_ADDRESS>
```
Replace `user` and `<IP_ADDRESS>` with your actual username and IP address on the minis.

> You can get your username by running `whoami` on the nodes (here `node` is your machine).

Eg: 

```bash
ssh-copy-id -i ~/.ssh/macmini_cluster.pub user@10.10.0.1
ssh-copy-id -i ~/.ssh/macmini_cluster.pub user@10.10.0.2
ssh-copy-id -i ~/.ssh/macmini_cluster.pub user@10.10.0.3
```
This allows you to SSH into the minis without typing a password, which is essential for smooth cluster management.

### 7. Create SSH Config

Edit `~/.ssh/config` on your laptop:

```bash
Host mini1
    HostName YOUR_IP_HERE
    User your_username
    IdentityFile ~/.ssh/macmini_cluster
    IdentitiesOnly yes
```

Eg:

```bash
    Host mini2
    HostName 10.10.0.2
    User your_username
    IdentityFile ~/.ssh/macmini_cluster
    IdentitiesOnly yes

```

Now you can just run `ssh mini1` instead of typing the full IP. Much cleaner.

---


## Debugging Commands

| What to Check | Command |
|---|---|
| View routes | `netstat -rn` |
| Check bridge config | `ifconfig bridge0` |
| See listening ports | `lsof -iTCP -sTCP:LISTEN` |
| Trace traffic on bridge0 | `sudo tcpdump -ni bridge0 port 65432` |
| Flush ARP cache | `sudo arp -a -d` |
| Verify firewall status | `sudo pfctl -s info` |

---

## Common Errors & How to Fix Them

### "Errno 65: No route to host"

- **PF firewall is enabled** — run `sudo pfctl -d` and verify with `sudo pfctl -s info`
- **Bad bridge route** — check `netstat -rn`, make sure you see `bridge0` for 10.10.0.x traffic


### "Ping works but TCP fails"

Usually a firewall or socket binding issue:

- Verify `sudo pfctl -s info` shows "Status: Disabled"
- Test with `nc` manually before running training code

---

## My IP Layout

| Node | IP |
|---|---|
| Mac mini 1 | 10.10.0.1 |
| Mac mini 2 | 10.10.0.2 |
| Mac mini 3 | 10.10.0.3 |
| Raspberry Pi 5 | 10.10.1.0/4 |
| Jetson Orin Nano | 10.10.2.0/3 |



---



## Final Checklist

- [ ] Thunderbolt Bridge enabled on all minis
- [ ] Static IPs assigned (10.10.0.x)
- [ ] Ping works between all nodes (<1ms)
- [ ] macOS firewall disabled on all nodes
- [ ] TCP connectivity verified with `nc`
- [ ] SSH keys set up from your laptop
- [ ] SSH config created for easy access
- [ ] Wi-Fi still works for control traffic

---

You're ready. Spin up your PyTorch code, bind to `0.0.0.0`, initialize your cluster, and train. Your gradient syncs will be faster than anything in the cloud.

**Built for [smolcluster](https://smolcluster.com)** — distributed ML from scratch, on your own hardware.
---
title: "Wiring Mac Minis into a Training Cluster | Thunderbolt Networking for Distributed Training and Inference"
collection: talks
type: "Guide"
permalink: /talks/thunderbolt-cluster-setup
date: 2026-05-10
venue: "SmolCluster"
location: "smolcluster.com"
website_url: "https://smolcluster.com"
excerpt: "A step-by-step guide to wiring Mac minis together over Thunderbolt for distributed training and inference — dedicated ~10-20 Gbps bandwidth, <1ms latency, zero cloud costs."
---

You want to train models. You have Mac minis. You don't want to rent GPU clouds. So you **wire them together** and make a cluster.

This guide walks you through setting up a solid distributed training cluster using Thunderbolt networking for ~10-20 Gbps of pure local bandwidth, zero egress costs, and full control over every packet.

By the end, your minis will be talking to each other over dedicated Thunderbolt links while your laptop SSHes in over Wi-Fi. PyTorch FSDP, DDP, pipeline parallelism — all waiting to be explored.

---

## Why This Approach?

- **No cloud costs:** You own the hardware. Bandwidth is free.
- **Good bandwidth:** Thunderbolt = ~10-20 Gbps.
- **Low latency:** <1ms between nodes. Perfect for distributed training.
- **Simple setup:** Just enable a bridge, assign IPs, disable a firewall (will re-enable later!). Done.

---

## The Network Topology

Here's the key insight: split your traffic into two networks.

| Purpose | Network | Use For |
|---|---|---|
| **Control + Internet** | Wi-Fi | SSH, GitHub, pip installs, remote access |
| **Training Traffic** | Thunderbolt | All-reduce, gradient syncs, model data |

This keeps your training traffic on its own dedicated highway while your laptop still has internet access for control commands.

What it looks like:


#TODO
add arch.png here

Clean separation. No Wi-Fi congestion. Just throughput where it matters.

---

## Step-by-Step Setup

### 1. Enable Thunderbolt Bridge

Before opening settings, decide your coordinator machine first.

- Pick one machine as the central node: either any of the **minis** or a **MacBook** maybe.
- Connect every other Mac mini directly to this central node over Thunderbolt. This is called a **star** topology. 
- This gives you a clean star layout and makes management easier because one machine acts as the control point.


> **IMPORTANT:** Little ⚡ check!
> - Connect cluster cables only to ports that support **Thunderbolt** (look for the ⚡ symbol).
> - Using a non-Thunderbolt USB-C port is a common mistake and can cause link failures or unstable connectivity.
> - On Mac minis especially, double-check the exact port before plugging in. On newer MacBooks, many USB-C ports are Thunderbolt-capable, but you should still confirm your specific model.




Once the cabling is done, on **each Mac mini or MacBook**, open System Settings and navigate to the Thunderbolt Bridge.

If you don't see it, it should appear after you plug in the Thunderbolt cables.

### 2. Assign Static IPs

Give each node a unique static IP on the Thunderbolt network using the macOS UI.

On each mini:

1. Open **System Settings** -> **Network**.
2. Click **Thunderbolt Bridge**.
3. Click **Details...**.
4. Go to **TCP/IP**.
5. Change **Configure IPv4** from **Using DHCP** to **Manually**.
6. Enter these values:
    - **mini1**: IP Address `10.10.0.1`, Subnet Mask `255.255.255.0`
    - **mini2**: IP Address `10.10.0.2`, Subnet Mask `255.255.255.0`
    - **mini3**: IP Address `10.10.0.3`, Subnet Mask `255.255.255.0`
7. Leave **Router/Gateway** empty for this direct local link.
8. Click **OK**, then **Apply**.

Verify from Terminal:

```bash
ifconfig bridge0
```

You should see something like `inet 10.10.0.1 netmask 0xffffff00` in the output.

### 3. Test Connectivity with Ping

From your coordinator node (e.g., mini1), ping the other nodes:

```bash
ping 10.10.0.1
```

You should see:

```
64 bytes from 10.10.0.1: icmp_seq=0 ttl=64 time=0.123 ms
64 bytes from 10.10.0.1: icmp_seq=1 ttl=64 time=0.089 ms
```

**This should be ultra-fast** (<1ms). If ping is slow or times out, check:

- Are the Thunderbolt cables actually plugged in?
- Does the bridge interface exist? (`ifconfig bridge0`)
- Are the IPs actually assigned?

### 4. Disable the macOS Firewall (Optional )

This is the #1 gotcha. The macOS packet filter (PF) can silently block Thunderbolt TCP traffic. Your ping will work fine, but TCP connections will hang or fail with "No route to host" errors.

Disable it:

```bash
sudo pfctl -d
```

Verify it's off:

```bash
sudo pfctl -s info
```

Look for this in the output:

```
Status: Disabled
```

**Why does this matter?** PF is a stateful packet filter. It can block connections even if routing is fine. 

**When to use:** When you start seeing "Errno 65: No route to host" in your training code later, 90% of the time it's this and its not your routing or cabling fault. Disabling PF is a critical step in validating your cluster setup.

### 5. Test TCP Connectivity

Test actual TCP (not just ICMP ping). On coordinator node (e.g., mini1), listen on a port:

```bash
nc -l 65432
```

On one of the other nodes (e.g., mini2), try to connect:

```bash
nc 10.10.0.1 65432
```

If it works, the `nc` command will just hang (no error output). Ctrl+C to exit.

**What just happened:** Routing works. TCP is flowing. Firewall isn't blocking. You're ready for training code.

### 6. Set Up SSH Keys

Generate a key on your laptop:

```bash
ssh-keygen -t ed25519 -f ~/.ssh/macmini_cluster
```

Copy it to each node:

```bash
ssh-copy-id -i ~/.ssh/macmini_cluster.pub user@<IP_ADDRESS>
```
Replace `user` and `<IP_ADDRESS>` with your actual username and IP address on the minis.

> You can get your username by running `whoami` on the nodes (here `node` is your machine).

Eg: 

```bash
ssh-copy-id -i ~/.ssh/macmini_cluster.pub user@10.10.0.1
ssh-copy-id -i ~/.ssh/macmini_cluster.pub user@10.10.0.2
ssh-copy-id -i ~/.ssh/macmini_cluster.pub user@10.10.0.3
```
This allows you to SSH into the minis without typing a password, which is essential for smooth cluster management.

### 7. Create SSH Config

Edit `~/.ssh/config` on your laptop:

```bash
Host mini1
    HostName YOUR_IP_HERE
    User your_username
    IdentityFile ~/.ssh/macmini_cluster
    IdentitiesOnly yes
```

Eg:

```bash
    Host mini2
    HostName 10.10.0.2
    User your_username
    IdentityFile ~/.ssh/macmini_cluster
    IdentitiesOnly yes

```

Now you can just run `ssh mini1` instead of typing the full IP. Much cleaner.

---


## Debugging Commands

| What to Check | Command |
|---|---|
| View routes | `netstat -rn` |
| Check bridge config | `ifconfig bridge0` |
| See listening ports | `lsof -iTCP -sTCP:LISTEN` |
| Trace traffic on bridge0 | `sudo tcpdump -ni bridge0 port 65432` |
| Flush ARP cache | `sudo arp -a -d` |
| Verify firewall status | `sudo pfctl -s info` |

---

## Common Errors & How to Fix Them

### "Errno 65: No route to host"

- **PF firewall is enabled** — run `sudo pfctl -d` and verify with `sudo pfctl -s info`
- **Bad bridge route** — check `netstat -rn`, make sure you see `bridge0` for 10.10.0.x traffic


### "Ping works but TCP fails"

Usually a firewall or socket binding issue:

- Verify `sudo pfctl -s info` shows "Status: Disabled"
- Test with `nc` manually before running training code

---

## My IP Layout

| Node | IP |
|---|---|
| Mac mini 1 | 10.10.0.1 |
| Mac mini 2 | 10.10.0.2 |
| Mac mini 3 | 10.10.0.3 |
| Raspberry Pi 5 | 10.10.1.0/4 |
| Jetson Orin Nano | 10.10.2.0/3 |



---



## Final Checklist

- [ ] Thunderbolt Bridge enabled on all minis
- [ ] Static IPs assigned (10.10.0.x)
- [ ] Ping works between all nodes (<1ms)
- [ ] macOS firewall disabled on all nodes
- [ ] TCP connectivity verified with `nc`
- [ ] SSH keys set up from your laptop
- [ ] SSH config created for easy access
- [ ] Wi-Fi still works for control traffic

---

You're ready. Spin up your PyTorch code, bind to `0.0.0.0`, initialize your cluster, and train. Your gradient syncs will be faster than anything in the cloud.

**Built for [smolcluster](https://smolcluster.com)** — distributed ML from scratch, on your own hardware.
