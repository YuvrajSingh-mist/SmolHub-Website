---
title: 'Thunderbolt Cluster Setup Guide'
date: 2026-05-09
permalink: /posts/mac-cluster-setup-guide/
author_profile: false
excerpt: "Wire Mac minis into a high-bandwidth local Thunderbolt cluster for distributed training and inference with zero cloud egress cost, low latency, and direct control over cluster networking."
tags:
  - Distributed Setup
  - Cluster Setup
  - Thunderbolt Networking
  - Guide
---

 > **Tested on:** macOS 26.2 (both coordinator and worker nodes)

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

<figure>
  <img src="/images/blogs/thunderbolt-cluster-guide/architecture.png" alt="Thunderbolt cluster architecture - star topology with Thunderbolt Bridge connecting minis">
  <figcaption>Figure 1. Thunderbolt cluster architecture with a central coordinator in star topology.</figcaption>
</figure>

Clean separation. No Wi-Fi congestion. Just throughput where it matters.

---

## Step-by-Step Setup

## 1. Enable Thunderbolt Bridge

Before opening settings, decide your coordinator machine first.

- Pick one machine as the central node: either any of the **minis** or a **MacBook** maybe.
- Connect every other Mac mini directly to this central node over Thunderbolt. This is called a **star** topology. 
- This gives you a clean star layout and makes management easier because one machine acts as the control point.


> **IMPORTANT:** Little ⚡ check!

<figure style="width: fit-content; max-width: 100%; margin: 0 auto 1rem auto; display: flex; flex-direction: column; align-items: center;">
  <img src="/images/blogs/thunderbolt-cluster-guide/thunderbolt-sign.jpeg" alt="Thunderbolt sign check" style="max-height: 260px; width: auto; max-width: 100%; display: block;">
  <figcaption>Figure 2. Use only USB-C ports marked with the Thunderbolt symbol.</figcaption>
</figure>

> - Connect cluster cables only to ports that 
support **Thunderbolt** (look for the ⚡ symbol).
> - Using a non-Thunderbolt USB-C port is a common mistake and can cause link failures or unstable connectivity.
> - On Mac minis especially, double-check the exact port before plugging in. On newer MacBooks, many USB-C ports are Thunderbolt-capable, but you should still confirm your specific model.


Once the cabling is done, on **each Mac mini or MacBook**, open System Settings and navigate to the Thunderbolt Bridge.

If you don't see it, it should appear after you plug in the Thunderbolt cables like in the following image: 

<div style="display: flex; flex-wrap: wrap; gap: 1rem; align-items: flex-start;">
  <figure style="flex: 1 1 320px; margin: 0;">
    <img src="/images/blogs/thunderbolt-cluster-guide/thunderbolt-not-connected.png" alt="Thunderbolt bridge not connected">
    <figcaption>Figure 3. Thunderbolt Bridge not yet connected.</figcaption>
  </figure>
  <figure style="flex: 1 1 320px; margin: 0;">
    <img src="/images/blogs/thunderbolt-cluster-guide/thudnerbolt-connected.png" alt="Thunderbolt bridge connected">
    <figcaption>Figure 4. Thunderbolt Bridge connected and active.</figcaption>
  </figure>
</div>

## 2. Assign Static IPs

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


Here's how's mine look like:

<figure>
  <img src="/images/blogs/thunderbolt-cluster-guide/thunderbolt-settings.png" alt="Thunderbolt cluster TCP IP settings panel">
  <figcaption>Figure 5. Manual TCP/IP settings for a Thunderbolt Bridge interface.</figcaption>
</figure>
Verify from Terminal:

```bash
ifconfig bridge0
```

You should see something like `inet 10.10.0.1 netmask 0xffffff00` in the output.

## 3. Test Connectivity with Ping

From your coordinator node (e.g., mini1), ping the other nodes:

```bash
ping 10.10.0.1
```

You should see:

```
64 bytes from 10.10.0.1: icmp_seq=0 ttl=64 time=0.423 ms
64 bytes from 10.10.0.1: icmp_seq=1 ttl=64 time=0.422 ms
```

**This should be ultra-fast** (<1ms). If ping is slow or times out, check:

- Are the Thunderbolt cables actually plugged in?
- Does the bridge interface exist? (`ifconfig bridge0`)
- Are the IPs actually assigned?

## 4. Disable the macOS Firewall (Optional )

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

## 5. Test TCP Connectivity

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

## 6. Set Up SSH Keys

SSH keys let you authenticate without typing passwords — essential for scripts and distributed work.

#### Step 6a: Generate the Key Pair

On your laptop, generate an ed25519 key (modern, fast, secure):

```bash
ssh-keygen -t ed25519 -f ~/.ssh/macmini_cluster
```

You'll see:

```
Generating public/private ed25519 key pair.
Enter passphrase (empty for no passphrase):
```

**Passphrase choice:**
- **With passphrase:** Adds a password layer. Recommended for security, but you'll need to type it or use `ssh-agent` each session.
- **Empty passphrase (just press Enter):** No password. Convenient for scripts, but the key file itself is your only protection. Use this if your laptop is trusted and well-protected.

For a cluster setup where you'll run lots of jobs, **empty passphrase is typical**. Your laptop's disk encryption is your security layer.

After pressing Enter (or entering a passphrase), you'll see:

```
Your identification has been saved in /Users/your_user/.ssh/macmini_cluster
Your public key has been saved in /Users/your_user/.ssh/macmini_cluster.pub
The key fingerprint is:
SHA256:... (your fingerprint)
```

#### Step 6b: Verify the Keys Were Created

```bash
ls -la ~/.ssh/macmini_cluster*
```

You should see:

```
-rw-------  1 your_user  staff  464 May 10 12:00 macmini_cluster
-rw-r--r--  1 your_user  staff  103 May 10 12:00 macmini_cluster.pub
```

**Permissions matter:**
- `macmini_cluster` (private key): `600` (owner read/write only) ✓
- `macmini_cluster.pub` (public key): `644` (readable by all) ✓

If permissions are wrong, SSH will refuse to use the key. Fix it:

```bash
chmod 600 ~/.ssh/macmini_cluster
chmod 644 ~/.ssh/macmini_cluster.pub
```

#### Step 6c: Get Your Username on the Minis

Before copying keys, find your username on each mini. SSH into one and run:

```bash
whoami
```

You'll see something like `yuvraj` or something like this for your username. **Use this exact username** in the next steps.

#### Step 6d: Copy the Public Key to Each Node

This authorizes your laptop to log in without a password:

```bash
ssh-copy-id -i ~/.ssh/macmini_cluster.pub your_username@10.10.0.1
ssh-copy-id -i ~/.ssh/macmini_cluster.pub your_username@10.10.0.2
ssh-copy-id -i ~/.ssh/macmini_cluster.pub your_username@10.10.0.3
```

Replace `your_username` with the actual username (e.g., `yuvraj`).

For each command, you'll be prompted for a password — this is the **login password on that mini**, not the key passphrase. Enter it to authorize the key copy.

**Full example flow:**

```bash
$ ssh-copy-id -i ~/.ssh/macmini_cluster.pub yuvraj@10.10.0.1
```

You'll see:

```
/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "/Users/your_user/.ssh/macmini_cluster.pub"
/usr/bin/ssh-copy-id: INFO: attempting to log in with the key(s) from "/Users/your_user/.ssh/macmini_cluster.pub" to see if they work
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
yuvraj@10.10.0.1's password:
```

**Type your login password** (not visible as you type), then press Enter:

```
Number of key(s) added: 1

Now try logging in with:
  "ssh -i /Users/your_user/.ssh/macmini_cluster 'yuvraj@10.10.0.1'"

and check to make sure that only the key(s) you wanted were added.
```

✓ **Success!** Your public key is now authorized on mini1. Repeat for mini2 and mini3.

#### Step 6e: Test Passwordless SSH

Try logging in without a password:

```bash
ssh -i ~/.ssh/macmini_cluster your_username@10.10.0.1
```

If it works, you'll be logged in with **no password prompt**. Type `exit` to disconnect.

If it fails with "Permission denied (publickey)", check:
- Is the private key readable? (`ls -la ~/.ssh/macmini_cluster` should show `600`)
- Did `ssh-copy-id` succeed? (Check for error messages from Step 6d)
- Is the username correct? (Run `whoami` on the mini to verify)

**What just happened:** Passwordless authentication is now set up for all three minis.


## 7. Create SSH Config

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

- Thunderbolt Bridge enabled on all minis
- Static IPs assigned (10.10.0.x)
- Ping works between all nodes (<1ms)
- macOS firewall disabled on all nodes
- TCP connectivity verified with `nc`
- SSH keys set up from your laptop
- SSH config created for easy access
- Wi-Fi still works for control traffic

---

You're ready. Spin up your PyTorch code, bind to `0.0.0.0`, initialize your cluster, and train. Your gradient syncs will be faster than anything in the cloud.

**Built for [smolcluster](https://smolcluster.com)** — distributed training and inference library from scratch, on your own hardware.

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

You're ready! Congratualtions! Now, in the next few posts we'll spin up a training/inference job to see it in action!

**Built for [smolcluster](https://smolcluster.com)** — distributed training and inference library from scratch, for local compute, on your own hardware.

<figure>
  <img src="/images/blogs/thunderbolt-cluster-guide/my-mac-mini-cluster.jpeg" alt="My Mac Minis Cluster">
  <figcaption>My Mac mini cluster (3x M4 16 gig each) — three nodes wired together over Thunderbolt.</figcaption>
</figure>

