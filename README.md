# GVM / OpenVAS Packaging Project 

The GVM (formerly OpenVAS) packaging project is an Atomicorp-maintained distribution to install, configure, and maintain the [Greenbone Vulnerability Management](https://www.greenbone.net) suite (Version 26.43) on modern Enterprise Linux and Fedora platforms.

Visit our website for the latest information: [www.atomicorp.com](https://www.atomicorp.com)

---

## Currently Supported Platforms

### Primary / Current Release (GVM 26.43)
* **Enterprise Linux 10** (RHEL 10, Rocky Linux 10) — `x86_64`
* **Fedora 44** — `x86_64`
* **Fedora 45** — `x86_64`

### Legacy / Archived Platforms
* **Enterprise Linux 8 & 9** (GVM 21.04 / 22.04 legacy releases)
* **Fedora 36 & 37** (End of Life)

---

## Stack Architecture & Components

The Atomicorp GVM 26.43 packaging bundles and coordinates the modern Greenbone stack:

| Component | Upstream Package | Description |
|---|---|---|
| **GVMD** | `gvmd 26.43` | Greenbone Vulnerability Manager daemon |
| **OpenVAS Scanner** | `openvas-scanner 23.52` | Vulnerability assessment scanner & NASL interpreter |
| **GVM Libraries** | `gvm-libs 23.16` | Core networking, protocol, and utility libraries |
| **GSA / GSAD** | `gsad 27.7` | Greenbone Security Assistant (React Web UI & HTTP daemon) |
| **GVM Tools** | `gvm-tools 26.1` | CLI automation tools (`gvm-cli`, `python-gvm 27.10`) |
| **OSPd-OpenVAS** | `ospd-openvas 22.10` | Open Scanner Protocol daemon wrapper |
| **SMB Support** | `openvas-smb 22.5` | Authenticated Windows SMB/WMI scanning engine |
| **PostgreSQL Extension** | `pg-gvm 22.6` | Custom PostgreSQL functions for GVM |
| **Feed Sync** | `greenbone-feed-sync 25.5` | Vulnerability feed synchronization utility |
| **Cache & DB** | Valkey 8 & PostgreSQL 16 | High-performance in-memory cache and relational database |
| **Broker** | Mosquitto 2.0+ | MQTT publish/subscribe messaging broker |

---

## DNF Installation (Enterprise Linux 10 & Fedora)

### 1) Enable Prerequisites

**For RHEL 10 / Rocky Linux 10:**
```bash
sudo dnf config-manager --set-enabled crb
sudo dnf install -y epel-release
```

**For Fedora 44 & 45:**
No additional prerequisite repositories are required.

### 2) Install the Atomicorp Repository

```bash
wget -q -O - https://updates.atomicorp.com/installers/atomic | sudo sh
```

### 3) Install the GVM Metapackage

```bash
sudo dnf install -y gvm
```

### 4) Configure and Initialize GVM

Run the automated setup utility to initialize PostgreSQL, Valkey, feed keys, vulnerability feeds, and administrative accounts:

```bash
sudo gvm-setup
```

Once configuration completes, access the Greenbone Security Assistant (GSA) web interface at:
`https://<your-server-ip>:9392` or `https://<your-server-ip>`

---

## Docker Installation

The [Atomicorp OpenVAS Docker Project](https://github.com/atomicorp/openvas-docker) provides a pre-configured, self-contained container based on Rocky Linux 10:

```bash
# Pull the latest image
docker pull atomicorp/openvas:latest

# Create persistent storage volumes
docker volume create gvm_data
docker volume create gvm_plugins
docker volume create gvm_db

# Run the container
docker run -d \
  --name openvas \
  -p 443:443 \
  -v gvm_data:/var/lib/gvm \
  -v gvm_plugins:/var/lib/openvas \
  -v gvm_db:/var/lib/pgsql \
  atomicorp/openvas
```

For full container documentation, visit [Atomicorp/openvas-docker](https://github.com/Atomicorp/openvas-docker).

---

## Community & Support

* **Atomicorp Community Support:** [https://atomicorp.com/support/](https://atomicorp.com/support/)
* **Issue Tracker:** [GitHub Issues](https://github.com/Atomicorp/gvm/issues)
* **Greenbone Community Portal:** [https://community.greenbone.net/](https://community.greenbone.net/)

---

## Credits and Thanks

* Michael Meyer @Greenbone
* Jan-Oliver Wagner @Greenbone
* Everyone at Greenbone who makes the open-source GVM project possible
* Fredrik Hilmersson (https://libellux.com)
* Cody Woods @hcw2016
