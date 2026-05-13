---
title: 'Clustering 4 Raspberry Pi 4B: Real Setup'
date: 2026-05-10
permalink: /posts/raspberry-pi-cluster-setup-guide/
author_profile: false
excerpt: "Build a 4-node Raspberry Pi 4B cluster with UCTRONICS enclosure, PoE+ hats, and TP-Link LS110P PoE switch. Real numbers: ~9.5 Mbps throughput (10 Mbps link cap), 60–62°C under full load, zero throttling at 1800 MHz throughout."
tags:
  - Distributed Setup
  - Cluster Setup
  - Ethernet Networking
  - Raspberry Pi
  - PoE
  - Guide
---

> **Tested on:** Raspberry Pi 4B 4GB (Rev 1.5), Debian GNU/Linux 13 (trixie) — kernel 6.12.62+rpt-rpi-v8, UCTRONICS U6260 enclosure, Official PoE+ HAT, TP-Link LS110P PoE switch

You have four Raspberry Pi 4Bs. You built the proper setup: UCTRONICS enclosure, PoE+ hats, TP-Link unmanaged switch. One power cable. Everything stacked, cooled, and networked.

This guide walks you through setting up a real 4-node Raspberry Pi cluster. Not marketing hype — actual ~9.5 Mbps throughput because the TP-Link LS110P negotiates at 10 Mbps, but stable, thermally managed, and perfect for distributed inference.

By the end, your Pis will boot via PoE, talk to each other with <5ms latency, and be ready for inference workloads across all 4 nodes.

<figure>
  <img src="/images/blogs/pi-cluster-setup-guide/my-pi-cluster.jpeg" alt="My Raspberry Pi cluster setup with UCTRONICS enclosure, PoE+ HATs, and TP-Link LS110P switch" />
  <figcaption>Figure 1. Manual TCP/IP settings for a Raspberry Pi cluster.</figcaption>
</figure>

---

## Why This Setup?

- **No separate power cables.** PoE powers each Pi over the same Ethernet cable. Cleaner.
- **Thermal managed.** UCTRONICS fans keep temps 45-62°C under full 16-core load. No throttling.
- **Real performance.** ~9.5 Mbps actual throughput — hard-capped by the TP-Link LS110P negotiating eth0 at 10 Mbps. CPU never touches it.
- **Simple network.** One switch. Star topology. All nodes see each other at <5ms latency.

---

## The Hardware

| Component | Model | Notes |
|---|---|---|
| **Cluster** | 4x Raspberry Pi 4B 4GB (Rev 1.5) | ARM Cortex-A72, up to 1800 MHz (ondemand governor) |
| **Enclosure** | UCTRONICS U6260 | Stacks 4 Pis, 2 cooling fans included |
| **Power/Network** | Official PoE+ HAT (×4) | 30W max per port, power + data over Ethernet |
| **Switch** | TP-Link LS110P | 10-port unmanaged, 8 PoE+ ports (10/100Mbps per port), **96W total PoE budget**, Plug & Play, Isolation Mode |
| **Cables** | Cat 6 Ethernet (×4) | Cat 6 recommended; some switch bundles include cables |
| **Storage** | MicroSD 32GB (×4) | Or NVMe boot via PoE+ HAT |

---

## Real Performance Expectations

**Be real with yourself:**

- **Throughput:** ~9.5 Mbps sustained per link. The TP-Link LS110P is a **10/100 Mbps switch** — 100 Mbps is its hard ceiling per port. 

> PS: Mine eth0 (my ethernet adapter) is currently negotiating at just 10 Mbps for some unknown reason even when my router says max is 100 Mbps. Highly recommend getting a switch with a 1 Gbps port if you want higher inter node bandwidth.
- **Latency:** <5ms between nodes. Good enough for inference batching.
- **Thermals:** Idle 45–49°C. Single core load peaks at ~54°C. All 4 cores sustained: 60–62°C. Full 16-core cluster sustained 10 min: **62.3°C max, zero throttling**. Clock holds at 1800 MHz throughout.
- **Power draw:** ~15-20W per Pi under load. Total ~60-80W cluster. Well within PoE+ limits (30W per port).

**Perfect for:**
- Distributed inference (models <500M params)
- Data preprocessing / ETL
- Learning how distributed systems actually work
- Edge AI that runs on device

**Not good for:**
- Large model training (>1B params gets slow)
- High-bandwidth gradient sync

---

## Step 1: Assemble the Hardware

1. Follow the UCTRONICS manual (trust me it's good!) to construct the housing.

2. Once its done, stack all 4 Pis with PoE+ HATs (make sure to properly align the pins with the Pi ones!)

3. Finally, place the stacked Pis into the enclosure. Stack order matters for airflow—usually bottom to top 
 > **IMPORTANT:** You'll need to conenct the inbuilt enclusure's fans to  a few of the PI's - follow the enclosure manual for the PIN configuration.

4. Plug the TP-Link switch into power. Wait 30 seconds for it to boot.

Plug each Pi into the switch via Cat 6 Ethernet cables. One end of the Cat 6 cable goes in the Pi, the other end goes into the switch.

<figure>
  <img src="/images/blogs/pi-cluster-setup-guide/tp-link-router.jpeg" alt="TP-Link Switch all plugged in with ethernet cables connecting to Pi cluster" />
  <figcaption>Figure 2. TP-Link Switch all plugged in with ethernet cables connecting to Pi cluster.</figcaption>
</figure>

> **Caution — Verify your cables before plugging in:**
> Cat 6 cables are labeled. Flip the cable and look for `CAT6` or `CAT.6` printed along the sheath. If it says `CAT5` or `CAT5e`, it'll still work but you won't get the full benefit for Gigabit at this length. If there's no label at all, it's likely a cheap unrated cable—swap it.
> 
> Also do a quick physical check: both RJ45 connectors should click firmly into the port (you'll hear it), the locking tab should be intact, and the cable shouldn't have any sharp kinks or crimps along the run. A damaged cable can cause intermittent drops that are annoying to debug later.

5. Watch for the red LED to light up on each Pi—that's PoE power being detected. Its just for verification that power is flowing. The green LED will start blinking as the Pi boots (after following [Step 2](#step-2-flash-raspberry-pi-os)).

<div style="display:flex; gap:1rem; align-items:flex-start; flex-wrap:wrap;">
  <figure style="flex:1; min-width:240px; margin:0;">
    <img src="/images/blogs/pi-cluster-setup-guide/pi-poe-hat.jpeg" alt="Pi PoE+ hat on Raspberry Pi" style="width:100%;" />
    <figcaption>Figure 3. Pi PoE+ hat on Raspberry Pi.</figcaption>
  </figure>
  <figure style="flex:1; min-width:240px; margin:0;">
    <img src="/images/blogs/pi-cluster-setup-guide/picluster-case-with-ethernet-cables.jpeg" alt="Complete Pi Cluster" style="width:100%;" />
    <figcaption>Figure 4. Complete Pi Cluster.</figcaption>
  </figure>
</div>

---

## Step 2: Flash Raspberry Pi OS

Download **Raspberry Pi Imager** from [raspberrypi.com](https://raspberrypi.com):

Launch Imager and flash each microSD card with these settings:

1. Click **Choose Device** → **Raspberry Pi 4**
2. Click **Choose OS** → **Raspberry Pi OS (64-bit)**
3. Click **Choose Storage** → Your microSD card
4. Click **Settings** (gear icon) and configure:
   - **Hostname:** `pi-1` (or `pi-2`, `pi-3`, `pi-4` for the others)
   - **Enable SSH:** ✓
   - **Set username and password:** `pi` / your password
   - **Configure wireless LAN:** Leave blank
   - **Set locale:** Your timezone

Click **Save**, then **Write**. Wait ~2 minutes per card.

Repeat for all 4 cards.

Follow the video here if you need a visual:

<div style="position:relative; padding-bottom:56.25%; height:0; overflow:hidden; max-width:480px;">
  <iframe
    src="https://youtu.be/_d-qvHJ7EwU"
    title="Raspberry Pi Imager Tutorial"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    allowfullscreen
    style="position:absolute; top:0; left:0; width:100%; height:100%;">
  </iframe>
</div>

---

## Step 3: Insert microSD Cards & Boot

Unscrew each of Pi from the enclosure and insert each flashed microSD card into each of your Pi (flip the board and you'll see a tiny microSD slot) in the UCTRONICS tray.

Plug all Cat 6 Ethernet cables into the switch ports. You should see:
- Red LED on each Pi lights up within 5 seconds (PoE power detected)
- All 4 Pis boot within 45 seconds
- Green LED activity on the switch ports as they initialize

Test from your laptop:

```bash
ping pi-1.local
ping pi-2.local
ping pi-3.local
ping pi-4.local
```

Expected:

```
PING pi-1.local (192.168.1.100): 56 data bytes
64 bytes from 192.168.1.100: icmp_seq=0 ttl=64 time=1.234 ms
64 bytes from 192.168.1.100: icmp_seq=1 ttl=64 time=1.156 ms
--- pi-1.local statistics ---
4 packets transmitted, 4 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 1.156/1.237/1.340/0.065 ms
```

If `.local` mDNS doesn't work on your laptop, find the IPs instead (Step 4).

---

## Step 4: Find Your IP Addresses

SSH into pi-1:

```bash
ssh pi@pi-1.local
```

Password: whatever you set in Imager (e.g., `raspberry`).

Once logged in, find the IP:

```bash
hostname -I (gives you all IPs assigned to the Pi)
```

Output (example):

```
192.168.1.100 fd12:3456::789
```

Note the IPv4 address (the first number). Repeat for all 4 Pis and write them down.

**Your IPs will be different** depending on your router and network. This is an example:

```
pi-1: 192.168.1.100
pi-2: 192.168.1.101
pi-3: 192.168.1.102
pi-4: 192.168.1.103
```

Before moving on, note these DHCP IPs — you'll need them for the next step to set up a private subnet.

---

## Step 4b: Assign Private Subnet IPs (Recommended)

> **Why?** A private subnet gives each Pi a stable, predictable address that you control, isolates all cluster traffic to a known range, and makes SSH config, scripts, and inter-node communication unambiguous.

We'll add a static secondary IP on `10.0.1.x/24` to each Pi's eth0 alongside the existing DHCP address. The Pi keeps internet access via DHCP; cluster jobs use `10.0.1.x`.

Do this on each Pi one at a time. SSH in using its DHCP IP from Step 4:

```bash
ssh pi@192.168.1.7   # pi4-1 — use your actual DHCP IP
```

Check your NetworkManager connection name:

```bash
nmcli connection show
```

Output:

```
NAME                UUID                                  TYPE      DEVICE
Wired connection 1  a1b2c3d4-...                          ethernet  eth0
```

Note the name in the first column. Then add the static private IP — use the matching IP from the table below:

```bash
# On pi4-1:
sudo nmcli connection modify "Wired connection 1" +ipv4.addresses "10.0.1.1/24"
sudo nmcli connection up "Wired connection 1"
```

Verify both IPs are now live:

```bash
ip addr show eth0
```

Expected:

```
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> ...
    inet 192.168.1.7/24 brd 192.168.1.255 scope global dynamic noprefixroute eth0
    inet 10.0.1.1/24 brd 10.0.1.255 scope global noprefixroute eth0
```

Repeat on all 4 Pis:

| Node | DHCP IP (Step 4) | Private IP to assign |
|---|---|---|
| pi4-1 | 192.168.1.7 | `10.0.1.1` |
| pi4-2 | 192.168.1.5 | `10.0.1.2` |
| pi4-3 | 192.168.1.3 | `10.0.1.3` |
| pi4-4 | 192.168.1.6 | `10.0.1.4` |

**From here on, all steps use `10.0.1.x` IPs.** The DHCP IPs are still active if you need them, but everything cluster-related — SSH keys, config, inter-node traffic — goes through `10.0.1.x`.

---

## Step 5: Test All 4 Nodes Ping Each Other

From your laptop, ping all 4 Pis using the private subnet IPs assigned in Step 4b:

```bash
ping 10.0.1.1
ping 10.0.1.2
ping 10.0.1.3
ping 10.0.1.4
```

(If private IPs aren't responding yet, you can use the DHCP IPs from Step 4 temporarily.)

### 5a: SSH into pi-1 and ping the other nodes

SSH into pi4-1:

```bash
ssh pi@10.0.1.1
```

It'll ask you to verify the host fingerprint the first time:

```
The authenticity of host '10.0.1.1 (10.0.1.1)' can't be established.
ED25519 key fingerprint is SHA256:abc123xyz...
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```

Type `yes` and press Enter:

```
Warning: Permanently added '10.0.1.1' (ED25519) to the list of known hosts.
pi@10.0.1.1's password:
```

Enter the password you set in Imager. You won't see anything typed—that's normal. Press Enter:

```
Linux pi-1 6.1.21-v8+ #1642 SMP PREEMPT Mon Apr  3 17:24:16 BST 2023 aarch64
...
Last login: Tue May 13 10:00:00 2026
pi@minilab-pi4-1:~ $
```

You're in.

From there, ping the others:

```bash
ping 10.0.1.2
ping 10.0.1.3
ping 10.0.1.4
```

Expected output for each:

```
PING 10.0.1.2 (10.0.1.2): 56 data bytes
64 bytes from 10.0.1.2: icmp_seq=0 ttl=64 time=2.341 ms
64 bytes from 10.0.1.2: icmp_seq=1 ttl=64 time=2.215 ms
```

All working? Good. Move on.

---

## Step 6: Set Up SSH Keys

Generate a key on your laptop (coordinator node eg your macbook):

```bash
ssh-keygen -t ed25519 -f ~/.ssh/pi_cluster
```

It'll ask for a passphrase:

```
Generating public/private ed25519 key pair.
Enter passphrase (empty for no passphrase):
```

Press Enter to leave it empty (recommended for cluster use so passwordless SSH works smoothly later):

```
Enter same passphrase again:
```

Press Enter again. You'll see:

```
Your identification has been saved in /Users/your_user/.ssh/pi_cluster
Your public key has been saved in /Users/your_user/.ssh/pi_cluster.pub
The key fingerprint is:
SHA256:abc123xyz... your_user@your_laptop
```

Key generated. Two files created: `pi_cluster` (private, never share) and `pi_cluster.pub` (public, goes on the Pis).

Copy the key to all 4 Pis using the private subnet IPs from Step 4b:

```bash
ssh-copy-id -i ~/.ssh/pi_cluster.pub pi@10.0.1.1
ssh-copy-id -i ~/.ssh/pi_cluster.pub pi@10.0.1.2
ssh-copy-id -i ~/.ssh/pi_cluster.pub pi@10.0.1.3
ssh-copy-id -i ~/.ssh/pi_cluster.pub pi@10.0.1.4
```

For each, you'll see:

```
/usr/bin/ssh-copy-id: INFO: attempting to log in with the key(s) from "/Users/your_user/.ssh/pi_cluster.pub" to see if they work
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
pi@10.0.1.1's password:
```

Enter the Pi's password. After success:

```
Number of key(s) added: 1

Now try logging in with:
  "ssh -i /Users/your_user/.ssh/pi_cluster 'pi@10.0.1.1'"

and check to make sure that only the key(s) you wanted were added.
```

Test passwordless login:

```bash
ssh -i ~/.ssh/pi_cluster pi@10.0.1.1
```

Should connect without a password. Type `exit` to disconnect.

---

## Step 7: Create SSH Config

Edit `~/.ssh/config` on your laptop:

```bash
nano ~/.ssh/config
```

Add (using the private subnet IPs from Step 4b):

```
Host pi4-1
    HostName 10.0.1.1
    User pi
    IdentityFile ~/.ssh/pi_cluster
    IdentitiesOnly yes

Host pi4-2
    HostName 10.0.1.2
    User pi
    IdentityFile ~/.ssh/pi_cluster
    IdentitiesOnly yes

Host pi4-3
    HostName 10.0.1.3
    User pi
    IdentityFile ~/.ssh/pi_cluster
    IdentitiesOnly yes

Host pi4-4
    HostName 10.0.1.4
    User pi
    IdentityFile ~/.ssh/pi_cluster
    IdentitiesOnly yes
```

Replace the IPs with your actual ones from Step 4b.

Save and exit. Now connect with:

```bash
ssh pi4-1
ssh pi4-2
ssh pi4-3
ssh pi4-4
```

Much cleaner.

---

## Step 8: Update All Pis

SSH into pi4-1:

```bash
ssh pi4-1
sudo apt update && sudo apt upgrade -y
sudo reboot
```

Wait 30 seconds and repeat for pi4-2, pi4-3, pi4-4.

Install Python and tools:

```bash
ssh pi4-1
sudo apt install -y python3-pip python3-venv python3-dev git htop
```

Create a venv:

```bash
python3 -m venv ~/cluster_env
source ~/cluster_env/bin/activate
```

Repeat on all 4 Pis.

---

## Step 9: Test Bandwidth

Real throughput test between pi4-1 and pi4-2 using `iperf3`.

First, install iperf3 on all Pis:

```bash
sudo apt install -y iperf3
```

On pi4-1, start the server:

```bash
ssh pi4-1
iperf3 -s
```

You'll see:

```
-----------------------------------------------------------
Server listening on 5201
-----------------------------------------------------------
```

On pi4-2, run the client:

```bash
ssh pi4-2
iperf3 -c 10.0.1.1 -t 20 -f m
```

Output:

Connecting to host 10.0.1.1, port 5201
[  5] local 10.0.1.2 port 54321 connected to 10.0.1.1 port 5201
[ ID] Interval           Transfer     Bitrate         Retr  Cwnd
[  5]  0.00-20.00  sec  22.8 MBytes  9.54 Mbits/sec  0   28.3 KBytes       sender
[  5]  0.00-20.35  sec  22.8 MBytes  9.38 Mbits/sec                  receiver
```


Test again between different pairs (pi4-1↔pi4-3, pi4-2↔pi4-4) to confirm consistency across all links.

---

## Step 11: Test Temperatures

Install `stress-ng` on all Pis:

```bash
sudo apt install -y stress-ng
```

Check baseline temperature before stressing:

```bash
vcgencmd measure_temp
```

Expected at idle:

```
temp=48.7'C
```

Idle range across all 4 nodes: **45–49°C**.

Now run all 4 cores at 100% on all Pis simultaneously (SSH into each and fire it):

```bash
stress-ng --cpu 4 --timeout 600s
```

On a separate terminal, watch the temperature every 5 seconds:

```bash
watch -n 5 'vcgencmd measure_temp && cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq'
```

Output at plateau (~2–3 minutes in):

```
temp=61.8'C
1800000
```

Expected under full 16-core cluster load:
- **Peak temp:** 60–62°C (pi4-1 ran hottest at 62.3°C)
- **Clock:** 1800 MHz throughout — no throttling
- **Thermal headroom:** ~8–10°C before the 70°C soft-throttle kicks in

After the test, verify no throttling events occurred:

```bash
vcgencmd get_throttled
```

Expected:

```
throttled=0x0
```

`0x0` means clean — no throttling, no undervoltage, nothing. If you see anything other than `0x0`, check the UCTRONICS fans are spinning and the PoE+ HAT power rail is stable.

> **Note:** pi4-4 ran 5–6°C cooler than the others throughout — likely better airflow position in the enclosure or slight heatsink contact variance. Normal.

---

## Step 12: Test Inter-Pi SSH (for distributed jobs)

From pi4-1, SSH to pi4-2 without a password:

```bash
ssh pi4-1
ssh pi4-2
```

Should work. If it asks for password, you need to set up keys between the Pis:

On pi4-1:

```bash
ssh-keygen -t ed25519
# Press Enter for all defaults
ssh-copy-id -i ~/.ssh/id_ed25519.pub pi@10.0.1.2
```

Then retry:

```bash
ssh pi4-2
```

Should work now.

---

## Debugging Commands

| What to Check | Command |
|---|---|
| Temperature | `vcgencmd measure_temp` |
| Throttle status | `vcgencmd get_throttled` |
| CPU frequency | `cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq` |
| IP address | `hostname -I` |
| Memory | `free -h` |
| Disk | `df -h` |
| Ping another Pi | `ping 10.0.1.2 -c 3` |
| SSH to another Pi | `ssh pi4-2` |
| Bandwidth test (server) | `iperf3 -s` |
| Bandwidth test (client) | `iperf3 -c <ip> -t 20 -f m` |

---

## Common Issues

### "PoE+ HAT LED is off / Pi won't power on"

- Is the Ethernet cable fully plugged in? (Listen for a click.)
- Is the switch powered and showing the PoE+ light?
- Try a different switch port.
- Try a different Ethernet cable.

### "Bandwidth is only ~9.5 Mbps"

This is a cable/port auto-negotiation issue, not a Pi limitation. The TP-Link LS110P is a **10/100 Mbps switch** — your link fell back to 10 Mbps instead of 100 Mbps. The Pi 4 NIC supports gigabit. Try: reseat both Cat 6 cable ends, try a different switch port, or swap to a known-good cable. That should get you to ~95 Mbps. To exceed 100 Mbps you'd need to replace the switch with a gigabit model.

### "Can't SSH from pi4-1 to pi4-2"

- Did you set up SSH keys between them? Run `ssh-keygen -t ed25519` on pi4-1, then `ssh-copy-id`.
- Check `cat ~/.ssh/authorized_keys` on pi4-2 to see if pi4-1's key is there.

### "Thermal throttling: CPU stuck below 1800 MHz"

- Run `vcgencmd get_throttled` — if it returns anything other than `0x0`, throttling has occurred.
- Ensure UCTRONICS fans are spinning.
- Open the case slightly for better airflow.
- Move the cluster away from heat sources.
- Under full 16-core load the cluster plateaus at ~62°C — there's 8–10°C headroom. If you're seeing throttling, something is blocking airflow.

---

## My Cluster Layout

| Node | Hostname | IP | Specs |
|---|---|---|---|
| pi4-1 | minilab-pi4-1 | 10.0.0.1 | RPi 4B 4GB Rev 1.5, PoE+ HAT |
| pi4-2 | minilab-pi4-2 | 10.0.0.2 | RPi 4B 4GB Rev 1.5, PoE+ HAT |
| pi4-3 | minilab-pi4-3 | 10.0.0.3 | RPi 4B 4GB Rev 1.5, PoE+ HAT |
| pi4-4 | minilab-pi4-4 | 10.0.0.4 | RPi 4B 4GB Rev 1.5, PoE+ HAT |

**Network:** TP-Link LS110P PoE+ switch, Cat 6 Ethernet cables, all on ports 1-4

---

## Final Checklist

- [ ] UCTRONICS enclosure assembled with all 4 Pis
- [ ] All 4 Pis boot via PoE (red LEDs light up)
- [ ] All Pis reachable via ping (<5ms latency)
- [ ] IPs found and noted (via `hostname -I`)
- [ ] SSH keys set up from your laptop
- [ ] Passwordless SSH works to all Pis
- [ ] SSH config created on your laptop
- [ ] Python 3 and PyTorch installed on all Pis
- [ ] Bandwidth test shows ~9.5 Mbps per link (10 Mbps link cap)
- [ ] Temperatures stable 50-60°C with fans

---

## What's Next?

You have a working 4-node Pi cluster. Ideas:

- **Run distributed inference:** Load a model on each Pi, batch requests across them (will do this next!)
- **Distributed preprocessing:** Split a dataset across 4 Pis for parallel ETL.
- **Learn systems:** Build a simple consensus or leader election protocol.
- **Edge monitoring:** Run a small LLM locally on the cluster (haha this is what smolcluster is for!).

---

You're ready. Build something.

**Built for [smolcluster](https://smolcluster.com)** — distributed training and inference from scratch, on your own hardware.