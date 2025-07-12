This guide provides a comprehensive collection of Linux commands tailored for cybersecurity professionals, focusing on system monitoring, network analysis, file system investigation, and incident response. The commands are organized into logical sections, with complete and properly formatted code blocks for clarity and usability. Best practices are included to ensure non-disruptive execution on production systems.

## Table of Contents

- [Initial Incident Response Triage](#initial-incident-response-triage)
    - [Incident Response Workflow](#incident-response-workflow)
- [Detecting Cryptocurrency Mining Malware](#detecting-cryptocurrency-mining-malware)
    - [CPU Usage Analysis](#cpu-usage-analysis)
    - [Network Connection Analysis](#network-connection-analysis)
    - [File System Indicators](#file-system-indicators)
    - [Process Name Analysis](#process-name-analysis)
    - [Memory Analysis](#memory-analysis)
    - [Automated Detection Script](#automated-detection-script)
- [Network Analysis and Security Commands](#network-analysis-and-security-commands)
    - [Advanced Network Analysis](#advanced-network-analysis)
    - [Network Traffic Analysis with tcpdump](#network-traffic-analysis-with-tcpdump)
    - [iptables for Traffic Analysis](#iptables-for-traffic-analysis)
- [File System Security and Analysis](#file-system-security-and-analysis)
    - [File System Timeline Analysis](#file-system-timeline-analysis)
- [Permission and Ownership Analysis](#permission-and-ownership-analysis)
- [Process Analysis and System Monitoring](#process-analysis-and-system-monitoring)
    - [File Descriptor and Open File Analysis](#file-descriptor-and-open-file-analysis)
- [Memory Analysis and Forensics](#memory-analysis-and-forensics)
- [System Performance and Resource Monitoring](#system-performance-and-resource-monitoring)
- [Log Analysis and Security Monitoring](#log-analysis-and-security-monitoring)
    - [Advanced Log Correlation](#advanced-log-correlation)
- [SSH Security Configuration Analysis](#ssh-security-configuration-analysis)
- [User Account Analysis and Auditing](#user-account-analysis-and-auditing)
- [System Security Auditing](#system-security-auditing)
- [Package and Software Integrity Verification](#package-and-software-integrity-verification)
- [System Hardening Automation](#system-hardening-automation)
- [Command Logging and Audit Trail](#command-logging-and-audit-trail)
- [Performance and Resource Considerations](#performance-and-resource-considerations)
- [Combining Commands for Comprehensive Analysis](#combining-commands-for-comprehensive-analysis)
- [Automated Security Monitoring Script](#automated-security-monitoring-script)
- [Advanced Forensics and Timeline Analysis](#advanced-forensics-and-timeline-analysis)
    - [Data Recovery](#data-recovery)
- [Best Practices for Non-Disruptive Command Usage](#best-practices-for-non-disruptive-command-usage)
- [Conclusion](#conclusion)



## Initial Incident Response Triage

When responding to a security incident, a structured approach is essential. Below is a triage script that collects critical system information without disrupting operations.

```bash
#!/bin/bash
# incident_triage.sh - Initial incident response triage

INCIDENT_DIR="/tmp/incident_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$INCIDENT_DIR"

echo "Starting incident response triage..."

# System information
{
  echo "=== System Information ==="
  uname -a
  uptime
  date
} > "$INCIDENT_DIR/system_info.txt"

# Network connections
{
  echo "=== Network Connections ==="
  ss -tunap
  echo -e "\n=== Listening Services ==="
  ss -tlnp
  echo -e "\n=== Established Connections ==="
  ss -tnp state established
} > "$INCIDENT_DIR/network_connections.txt"

# Running processes
{
  echo "=== Process List ==="
  ps auxwwf
  echo -e "\n=== Process Tree ==="
  pstree -p
} > "$INCIDENT_DIR/processes.txt"

# User activity
{
  echo "=== Currently Logged In Users ==="
  w
  echo -e "\n=== Last Logins ==="
  last -20
  echo -e "\n=== Failed Login Attempts ==="
  grep "Failed password" /var/log/auth.log | tail -50
} > "$INCIDENT_DIR/user_activity.txt"

# File system changes
{
  echo "=== Recently Modified System Files ==="
  find /etc /bin /sbin /usr/bin /usr/sbin -type f -mtime -1 -ls 2>/dev/null
  echo -e "\n=== SUID/SGID Files ==="
  find / -type f \( -perm -4000 -o -perm -2000 \) -ls 2>/dev/null
} > "$INCIDENT_DIR/filesystem_changes.txt"

# Create archive
tar czf "incident_triage_$(date +%Y%m%d_%H%M%S).tar.gz" -C /tmp "$(basename $INCIDENT_DIR)"

echo "Triage complete. Results saved to $INCIDENT_DIR"
````

### Incident Response Workflow

1. **Containment Commands:**
    
    - Isolate affected systems or block malicious IPs to limit damage.
    
    ```bash
    iptables -A INPUT -s [malicious_ip] -j DROP
    ip link set eth0 down
    ```
    
2. **Investigation Commands:**
    
    - Collect logs, network connections, and process details for analysis.
    
    ```bash
    grep "suspicious_activity" /var/log/auth.log
    ss -tunap
    lsof -i
    ```
    
3. **Eradication Commands:**
    
    - Remove malicious files or terminate rogue processes.
    
    ```bash
    rm /path/to/malicious_file
    kill -9 [malicious_pid]
    ```
    
4. **Recovery & Lessons:**
    
    - Restore from clean backups and document findings.
    
    ```bash
    rsync -av --delete /backup/ /production/
    echo "Incident Summary: Details of what happened and how it was resolved" >> /path/to/documentation.txt
    ```
    

## Detecting Cryptocurrency Mining Malware

Cryptocurrency mining malware is a common threat that consumes system resources. The following commands help detect and analyze such activities.

### CPU Usage Analysis

```bash
# Identify high CPU processes
top -b -n 1 | awk '$9 > 80.0 {print $0}'

# Monitor CPU usage over time
sar -u 1 60 | grep -v Average | awk '$8 < 20 {print "High CPU: " $0}'

# High CPU processes with details
ps aux | awk '$3 > 80 {print $2, $3, $11}' | grep -v "COMMAND"
```

### Network Connection Analysis

```bash
# Check for mining pool connections
ss -tnp | grep -E ":3333|:4444|:5555|:7777|:8333|:9999"

# Monitor for Stratum protocol
tcpdump -i any -A -s 0 'port 3333 or port 4444' | grep -i "stratum"
```

### File System Indicators

```bash
# Find mining configuration files
find / -name "*.json" -exec grep -l "pool\|wallet\|mining" {} \; 2>/dev/null

# Look for hidden mining directories
find / -type d -name ".*" -exec ls -la {} \; 2>/dev/null | grep -i "xmr\|mine"
```

### Process Name Analysis

```bash
# Look for common miner process names
ps aux | grep -E "xmrig|minerd|cminer|xmr-stak|minergate|nanopool"

# Find processes trying to hide
ps aux | grep -E "\[\]|\^ *\[|^$"
```

### Memory Analysis

```bash
# Search process memory for mining indicators
for pid in $(ps aux | awk '$3 > 80 {print $2}'); do
  strings /proc/$pid/cmdline 2>/dev/null | grep -i "pool\|stratum"
done
```

### Automated Detection Script

```bash
#!/bin/bash
# mining_detector.sh - Detect potential cryptocurrency mining activity
echo "Checking for cryptocurrency mining indicators..."

LOGFILE="/var/log/mining_detection.log"
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Starting mining detection..." >> "$LOGFILE"

# Check CPU usage
ps aux | awk '$3 > 80 {print $2, $3, $11}' | grep -v "COMMAND" >> "$LOGFILE"

# Check network connections
ss -tnp | grep -E ":3333|:4444|:5555|:7777|:8333|:9999" >> "$LOGFILE"

# Check for mining configs
find / -name "*.json" -exec grep -l "pool\|wallet\|mining" {} \; 2>/dev/null >> "$LOGFILE"

echo "Detection complete. Results saved to $LOGFILE"
```

## Network Analysis and Security Commands

The `ss` command is a modern replacement for `netstat`, offering faster and more detailed network analysis.

```bash
# Display all TCP connections with process information
ss -tnp

# Show listening ports with detailed socket information
ss -tlnp

# Display established connections
ss -tnp state established

# Show all UDP sockets
ss -uanp

# Filter connections by destination network
ss -tn state established dst 192.168.1.0/24

# Display socket memory usage (useful for DoS detection)
ss -tm

# Show connections to specific port
ss -tn sport = :22

# Real-time monitoring of connection states
watch -n 1 'ss -s'
```

### Advanced Network Analysis

```bash
# Identify processes making external connections
ss -tnp | grep -v "127.0.0.1" | awk '{print $6}' | sort | uniq -c | sort -rn

# Monitor connections to specific ports over time
while true; do
  echo "=== $(date) ==="
  ss -tn state established '( dport = :443 or dport = :80 )'
  sleep 5
done
```

### Network Traffic Analysis with tcpdump

```bash
# Capture traffic on specific interface
tcpdump -i eth0 -nn -vvv -X

# Save suspicious traffic
tcpdump -i any -w suspicious_traffic.pcap 'port 4444 or port 1337'

# Monitor DNS queries
tcpdump -i any -nn port 53

# Detect ARP spoofing
tcpdump -i eth0 -nn arp

# Capture HTTP traffic
tcpdump -i any -A -s 0 'tcp port 80 and (((ip[2:2] - ((ip[0]&0xf)<<2)) - ((tcp[12]&0xf0)>>2)) != 0)'

# Detect SYN flood attacks
tcpdump -i any -nn 'tcp[tcpflags] & (tcp-syn) != 0 and tcp[tcpflags] & (tcp-ack) == 0'

# Capture traffic from specific IP excluding SSH
tcpdump -i any -nn src 192.168.1.100 and not port 22
```

### iptables for Traffic Analysis

```bash
# Log all incoming connections
iptables -I INPUT -j LOG --log-prefix "INPUT: " --log-level 4

# Track new connections
iptables -A INPUT -m conntrack --ctstate NEW -j LOG --log-prefix "NEW_CONN: "

# Monitor SSH access attempts
iptables -A INPUT -p tcp --dport 22 -j LOG --log-prefix "SSH_ATTEMPT: "

# Create honeypot rules for telnet
iptables -A INPUT -p tcp --dport 23 -j LOG --log-prefix "TELNET_HONEYPOT: "
iptables -A INPUT -p tcp --dport 23 -j DROP

# Rate limit for DoS protection
iptables -A INPUT -p tcp --dport 80 -m limit --limit 25/minute --limit-burst 100 -j ACCEPT

# Track outbound connections
iptables -A OUTPUT -m state --state NEW -j LOG --log-prefix "OUTBOUND_NEW: "
```

## File System Security and Analysis

File system analysis is critical for identifying compromises and backdoors.

```bash
# Find recently modified files
find / -type f -mtime -1 -ls 2>/dev/null | grep -v "/proc\|/sys"

# Locate SUID/SGID files
find / -type f \( -perm -4000 -o -perm -2000 \) -ls 2>/dev/null

# Search for world-writable files
find / -type f -perm -o+w -ls 2>/dev/null | grep -v "/proc\|/sys\|/dev"

# Detect files with multiple hard links
find / -type f -links +1 -ls 2>/dev/null | grep -v "/proc\|/sys"

# Find hidden files and directories
find / -name ".*" -type f -ls 2>/dev/null | grep -v "/proc\|/sys"

# Locate files with spaces (evasion technique)
find / -name "* " -o -name " *.*" -ls 2>/dev/null

# Search for credentials in files
grep -r "password\|passwd\|pwd" /etc 2>/dev/null

# File integrity checking
find /bin /sbin /usr/bin /usr/sbin -type f -exec sha256sum {} \; > system_binaries.sha256

# Advanced file attribute analysis
find / -type f -exec lsattr {} \; 2>/dev/null | grep -E "^----i|^----a"
```

### File System Timeline Analysis

```bash
# Generate comprehensive timeline
find / -type f -printf "%T@ %Tc %p\n" 2>/dev/null | sort -n > filesystem_timeline.txt

# Create MAC time timeline
find / -printf "%A@ %Ay-%Am-%Ad %AH:%AM:%AS %p (atime)\n" -o \
-printf "%T@ %Ty-%Tm-%Td %TH:%TM:%TS %p (mtime)\n" -o \
-printf "%C@ %Cy-%Cm-%Cd %CH:%CM:%CS %p (ctime)\n" 2>/dev/null | \
sort -n > mac_timeline.txt

# Analyze file changes in specific timeframe
find / -type f -newermt "2024-01-01" ! -newermt "2024-01-02" -ls 2>/dev/null

# Track file system changes in real-time
inotifywait -m -r /etc --format '%w%f %e %T' --timefmt '%Y-%m-%d %H:%M:%S'
```

## Permission and Ownership Analysis

```bash
# Find world-writable directories
find / -type d -perm -0002 -ls 2>/dev/null | grep -v "/proc\|/sys"

# Locate files without proper ownership
find / -nouser -o -nogroup -ls 2>/dev/null

# Check executable permissions in home directories
find /home -type f -executable -ls 2>/dev/null

# Audit sudo permissions
cat /etc/sudoers /etc/sudoers.d/* 2>/dev/null | grep -v "^#\|^$"

# Analyze capability-enhanced binaries
getcap -r / 2>/dev/null

# Review ACL permissions
getfacl -R /sensitive/directory 2>/dev/null | grep -v "^#"
```

## Process Analysis and System Monitoring

```bash
# Comprehensive process listing
ps auxwwf

# Show process tree
ps -ejH

# Display processes with SELinux contexts
ps -eZ

# Monitor real-time process creation
while true; do
  ps aux | tail -n +2 | awk '{print $2}' > /tmp/ps.new
  diff /tmp/ps.old /tmp/ps.new 2>/dev/null | grep "^>" | awk '{print $2}' | while read pid; do
    ps -p $pid -o pid,ppid,user,cmd 2>/dev/null
  done
  mv /tmp/ps.new /tmp/ps.old
  sleep 1
done

# Find hidden processes (rootkit detection)
for pid in $(ls /proc | grep -E '^[0-9]+$'); do
  if ! ps -p $pid > /dev/null 2>&1; then
    echo "Hidden process found: PID $pid"
    ls -la /proc/$pid/ 2>/dev/null
  fi
done

# Analyze process memory maps
for pid in $(ps aux | awk '{print $2}' | grep -E '^[0-9]+$'); do
  if [ -r /proc/$pid/maps ]; then
    echo "=== PID: $pid ==="
    grep -E 'rwxp|r-xp.*\[' /proc/$pid/maps 2>/dev/null
  fi
done
```

### File Descriptor and Open File Analysis

```bash
# List open files by user
lsof -u username

# Display all network connections
lsof -i

# Show processes listening on specific ports
lsof -i :80,443

# Find deleted files still in use
lsof | grep deleted

# Monitor file access in real-time
watch -n 1 'lsof +D /sensitive/directory'

# Identify processes with many open files
lsof | awk '{print $2}' | sort | uniq -c | sort -rn | head -20

# Track network connections by process
lsof -i -n -P | grep ESTABLISHED

# Find processes using raw sockets
lsof | grep -E 'raw|packet'
```

## Memory Analysis and Forensics

```bash
# Dump process memory
gcore -o /tmp/process_dump $(pgrep suspicious_process)

# Analyze process memory strings
strings /proc/$(pgrep suspicious_process)/mem | grep -E "password|secret|key"

# Check kernel modules
lsmod | grep -v "Module"
modinfo $(lsmod | awk '{print $1}' | tail -n +2)

# Detect hidden kernel modules
cat /proc/modules > /tmp/modules_proc
lsmod | awk '{print $1}' | sort > /tmp/modules_lsmod
diff /tmp/modules_proc /tmp/modules_lsmod

# Memory usage by process
ps aux --sort=-%mem | head -20

# Shared memory analysis
ipcs -m
for i in $(ipcs -m | awk '/0x/ {print $2}'); do
  echo "=== Shared Memory Segment $i ==="
  ipcs -m -i $i
done

# Check for memory-resident malware
cat /proc/*/maps | grep -E "deleted|memfd:" | sort -u
```

## System Performance and Resource Monitoring

```bash
# Real-time system performance
vmstat

# Detailed CPU usage by process
top -b -n 1 | head -20

# Memory usage analysis
free -m && echo "===" && ps aux --sort=-%mem | head -10

# Disk I/O monitoring
iotop -b -n 1

# Network I/O by process
nethogs -t

# System call statistics
perf stat -a sleep 10

# Advanced performance analysis
sar -u -r -d -n DEV 1 10
```

## Log Analysis and Security Monitoring

```bash
# Monitor authentication attempts
journalctl -u ssh.service -f

# Analyze failed login attempts
grep "Failed password" /var/log/auth.log | awk '{print $11}' | sort | uniq -c | sort -rn

# Track sudo usage
grep sudo /var/log/auth.log | grep -v "session opened\|session closed"

# Monitor system messages in real-time
tail -f /var/log/syslog | grep -E "error|fail|denied|invalid"

# Analyze kernel messages
dmesg | grep -E "denied|blocked|detected"

# Extract IP addresses from logs
grep -E -o "([0-9]{1,3}\.){3}[0-9]{1,3}" /var/log/auth.log | sort | uniq -c | sort -rn
```

### Advanced Log Correlation

```bash
# Correlate authentication with network connections
for ip in $(ss -tn state established | awk '{print $4}' | grep -oE '[0-9]{1,3}(\.[0-9]{1,3}){3}' | sort -u); do
  echo "=== Connections from $ip ==="
  ss -tn | grep $ip
  echo "=== Auth logs for $ip ==="
  grep $ip /var/log/auth.log | tail -5
  echo
done

# Create security event summary
{
  echo "=== Failed Login Attempts ==="
  grep "Failed password" /var/log/auth.log | wc -l
  echo -e "\n=== Successful Logins ==="
  grep "Accepted password" /var/log/auth.log | wc -l
  echo -e "\n=== New User Sessions ==="
  grep "session opened" /var/log/auth.log | wc -l
  echo -e "\n=== Sudo Commands ==="
  grep "COMMAND=" /var/log/auth.log | wc -l
} > security_summary.txt
```

## SSH Security Configuration Analysis

```bash
# Check SSH configuration
grep -E "^[^#].*(PermitRootLogin|PasswordAuthentication|PubkeyAuthentication|PermitEmptyPasswords|X11Forwarding)" /etc/ssh/sshd_config

# Analyze SSH keys
find / -name "authorized_keys" -o -name "id_rsa*" -o -name "id_dsa*" 2>/dev/null

# Check for weak SSH host keys
ssh-keygen -lf /etc/ssh/ssh_host_*_key.pub

# Monitor SSH connection attempts
journalctl -u sshd -f

# Analyze SSH key fingerprints
for key in /etc/ssh/ssh_host_*_key.pub; do
  echo "=== $key ==="
  ssh-keygen -lf "$key"
  ssh-keygen -lf -E md5 "$key"
done

# Check SSH config issues
sshd -T | grep -E "permitrootlogin|passwordauthentication|pubkeyauthentication"
```

## User Account Analysis and Auditing

```bash
# List user accounts with details
getent passwd | awk -F: '$3 >= 1000 {print $1, $3, $6, $7}'

# Find users with empty passwords
awk -F: '($2 == "") {print $1}' /etc/shadow

# Identify users with UID 0
awk -F: '($3 == "0") {print}' /etc/passwd

# Check password aging settings
for user in $(cut -d: -f1 /etc/passwd); do
  echo -n "$user: "
  chage -l $user 2>/dev/null | grep "Password expires" || echo "No aging info"
done

# Find recently created/modified users
ls -la /home | grep -v "total\|^d"
stat /etc/passwd /etc/shadow /etc/group

# Analyze user login history
last -F | head -20
lastlog | grep -v "Never logged in"

# Check for users without home directories
while IFS=: read -r user _ _ _ home _; do
  [ ! -d "$home" ] && echo "User $user has no home directory: $home"
done < /etc/passwd

# Review user group memberships
for user in $(cut -d: -f1 /etc/passwd); do
  groups $user 2>/dev/null
done | sort -u
```

## System Security Auditing

```bash
# Check running services
systemctl list-units --type=service --state=running

# Analyze listening services
ss -tlnp | grep LISTEN

# Review firewall rules
iptables -L -n -v

# Check for unnecessary packages
deborphan

# Check for insecure services
dpkg -l | grep -E "telnet|rsh|rlogin|ftp" # Debian/Ubuntu
rpm -qa | grep -E "telnet|rsh|rlogin|ftp" # RedHat/CentOS

# Kernel parameter security check
sysctl -a 2>/dev/null | grep -E "forwarding|redirects|source_route|accept_ra|secure_redirects"

# SELinux/AppArmor status
sestatus # SELinux
aa-status # AppArmor

# Check for core dumps
find / -name "core.*" -o -name "*.core" 2>/dev/null

# Review cron jobs for all users
for user in $(cut -d: -f1 /etc/passwd); do
  echo "=== Crontab for $user ==="
  crontab -l -u $user 2>/dev/null | grep -v "^#"
done
```

## Package and Software Integrity Verification

```bash
# Verify package integrity (Debian/Ubuntu)
debsums -c 2>/dev/null | grep -v "0K$"

# Verify package integrity (RedHat/CentOS)
rpm -Va | grep -E "^..5"

# Check for rootkits
chkrootkit
rkhunter --check --skip-keypress

# Generate software inventory
dpkg -l > installed_packages_$(date +%Y%m%d).txt # Debian/Ubuntu
rpm -qa > installed_packages_$(date +%Y%m%d).txt # RedHat/CentOS

# Find unusual libraries
ldd /bin/* /usr/bin/* 2>/dev/null | grep -v "linux-vdso\|ld-linux" | awk '{print $3}' | sort -u
```

## System Hardening Automation

```bash
#!/bin/bash
# harden_system.sh - Automated system hardening

echo "Starting system hardening..."

# Kernel parameter hardening
cat > /etc/sysctl.d/99-security.conf << EOF
# IP Spoofing protection
net.ipv4.conf.all.rp_filter = 1
net.ipv4.conf.default.rp_filter = 1

# Ignore ICMP redirects
net.ipv4.conf.all.accept_redirects = 0
net.ipv6.conf.all.accept_redirects = 0

# Ignore send redirects
net.ipv4.conf.all.send_redirects = 0

# Disable source packet routing
net.ipv4.conf.all.accept_source_route = 0
net.ipv6.conf.all.accept_source_route = 0

# Log Martians
net.ipv4.conf.all.log_martians = 1

# Ignore ICMP ping requests
net.ipv4.icmp_echo_ignore_broadcasts = 1

# Disable IPv6 if not needed
net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.default.disable_ipv6 = 1

# Enable TCP/IP SYN cookies
net.ipv4.tcp_syncookies = 1
net.ipv4.tcp_max_syn_backlog = 2048
net.ipv4.tcp_synack_retries = 2
net.ipv4.tcp_syn_retries = 5

# Increase system file descriptor limit
fs.file-max = 65535

# Enable ExecShield
kernel.exec-shield = 1
kernel.randomize_va_space = 2
EOF

# Apply configurations
sysctl -p /etc/sysctl.d/99-security.conf

# Secure shared memory
echo "tmpfs /run/shm tmpfs defaults,noexec,nosuid 0 0" >> /etc/fstab

# Disable unnecessary services
systemctl disable avahi-daemon
systemctl disable cups
systemctl disable bluetooth

# Set secure permissions
chmod 644 /etc/passwd
chmod 644 /etc/group
chmod 600 /etc/shadow
chmod 600 /etc/gshadow

# Configure password policies
sed -i 's/^PASS_MAX_DAYS.*/PASS_MAX_DAYS 90/' /etc/login.defs
sed -i 's/^PASS_MIN_DAYS.*/PASS_MIN_DAYS 7/' /etc/login.defs
sed -i 's/^PASS_WARN_AGE.*/PASS_WARN_AGE 14/' /etc/login.defs

echo "System hardening complete."
```

## Command Logging and Audit Trail

```bash
# Enable comprehensive command logging
echo 'HISTTIMEFORMAT="%F %T "' >> /etc/profile
echo 'HISTSIZE=10000' >> /etc/profile
echo 'HISTFILESIZE=10000' >> /etc/profile

# Log all commands to syslog
echo 'PROMPT_COMMAND="history -a >(logger -t cmd -p local6.info)"' >> /etc/profile

# Create security command wrapper
cat > /usr/local/bin/sec_wrapper << 'EOF'
#!/bin/bash
COMMAND="$@"
LOGFILE="/var/log/security_commands.log"
echo "[$(date '+%Y-%m-%d %H:%M:%S')] User: $(whoami) Command: $COMMAND" >> "$LOGFILE"
exec $COMMAND
EOF
chmod +x /usr/local/bin/sec_wrapper

# Configure sudo logging
echo "Defaults log_output" >> /etc/sudoers
echo "Defaults!/usr/bin/sudoreplay !log_output" >> /etc/sudoers
echo "Defaults!/sbin/reboot !log_output" >> /etc/sudoers
```

## Performance and Resource Considerations

```bash
# Limit resource usage for find
nice -n 19 ionice -c 3 find / -type f -mtime -1

# Use timeout to prevent hanging
timeout 300 tcpdump -i any -w capture.pcap

# Implement resource limits
ulimit -t 3600 # CPU time limit
ulimit -v 1048576 # Virtual memory limit

# Monitor command resource usage
/usr/bin/time -v command_to_monitor

# Background intensive tasks
nohup find / -type f -exec sha256sum {} \; > checksums.txt 2>&1 &
```

## Combining Commands for Comprehensive Analysis

```bash
# Combine network and process analysis
ss -tnp | grep ESTABLISHED | awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -rn | head -10

# Analyze files accessed by suspicious processes
lsof -p $(ps aux | grep suspicious | grep -v grep | awk '{print $2}' | tr '\n' ',')

# Check all user crontabs
for user in $(cut -d: -f1 /etc/passwd); do
  echo "=== $user ==="
  crontab -l -u $user 2>/dev/null | grep -v "^#"
done

# Parallel file integrity checking
find /bin /sbin -type f | parallel -j 4 sha256sum {} > integrity_check.txt
```

## Automated Security Monitoring Script

```bash
#!/bin/bash
# security_monitor.sh - Continuous security monitoring

LOGFILE="/var/log/security_monitor.log"
ALERT_EMAIL="security@example.com"

log_event() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOGFILE"
}

check_failed_logins() {
  local threshold=10
  local failed_count=$(grep "Failed password" /var/log/auth.log | \
    awk -v d="$(date -d '5 minutes ago' '+%b %d %H:%M')" '$0 > d' | wc -l)
  if [ "$failed_count" -gt "$threshold" ]; then
    log_event "ALERT: $failed_count failed login attempts in the last 5 minutes"
    echo "Failed login surge detected: $failed_count attempts" | \
    mail -s "Security Alert: Failed Logins" "$ALERT_EMAIL"
  fi
}

check_new_users() {
  local current_users="/tmp/users_current.txt"
  local previous_users="/tmp/users_previous.txt"
  cut -d: -f1 /etc/passwd | sort > "$current_users"
  if [ -f "$previous_users" ]; then
    new_users=$(comm -13 "$previous_users" "$current_users")
    if [ -n "$new_users" ]; then
      log_event "ALERT: New users detected: $new_users"
      echo "New users created: $new_users" | \
      mail -s "Security Alert: New Users" "$ALERT_EMAIL"
    fi
  fi
  mv "$current_users" "$previous_users"
}

check_listening_ports() {
  local current_ports="/tmp/ports_current.txt"
  local previous_ports="/tmp/ports_previous.txt"
  ss -tlnp 2>/dev/null | awk '{print $4}' | grep -E ":[0-9]+" | sort -u > "$current_ports"
  if [ -f "$previous_ports" ]; then
    new_ports=$(comm -13 "$previous_ports" "$current_ports")
    if [ -n "$new_ports" ]; then
      log_event "ALERT: New listening ports detected: $new_ports"
      echo "New ports opened: $new_ports" | \
      mail -s "Security Alert: New Ports" "$ALERT_EMAIL"
    fi
  fi
  mv "$current_ports" "$previous_ports"
}

check_outbound_connections() {
  local suspicious_ports="4444 31337 1337 6667"
  for port in $suspicious_ports; do
    if ss -tn state established | grep -q ":$port"; then
      log_event "ALERT: Suspicious outbound connection on port $port"
      ss -tnp | grep ":$port" | \
      mail -s "Security Alert: Suspicious Connection" "$ALERT_EMAIL"
    fi
  done
}

while true; do
  check_failed_logins
  check_new_users
  check_listening_ports
  check_outbound_connections
  sleep 300 # Check every 5 minutes
done
```

## Advanced Forensics and Timeline Analysis

```bash
# Create master timeline
find / -printf "%T@ %Tc %11s %M %u %g %p\n" 2>/dev/null | sort -n > master_timeline.txt

# Extract specific timeframe
awk -v start="$(date -d '2024-01-01' +%s)" -v end="$(date -d '2024-01-31' +%s)" \
'$1 >= start && $1 <= end' master_timeline.txt

# Correlate file changes with log events
while read timestamp file; do
  echo "=== File: $file ==="
  log_time=$(date -d "@$timestamp" "+%b %d %H:%M")
  grep "$log_time" /var/log/auth.log /var/log/syslog 2>/dev/null
done < <(find /etc -type f -mtime -1 -printf "%T@ %p\n")

# Process execution timeline
journalctl --since "1 day ago" -o json | \
jq -r '.[] | select(.MESSAGE | contains("Exec")) | "\(.__REALTIME_TIMESTAMP) \(.MESSAGE)"' | \
sort
```

### Data Recovery

```bash
# Recover deleted files
extundelete /dev/sda1 --restore-all

# Search for strings in unallocated space
dd if=/dev/sda1 | strings -n 10 | grep -i "password\|confidential"

# Create forensic image
dd if=/dev/sda of=/external/forensic_image.dd bs=4M conv=sync,noerror

# Calculate hash for integrity
sha256sum /external/forensic_image.dd > forensic_image.sha256

# Mount image for analysis
mkdir /mnt/forensic
mount -o loop,ro /external/forensic_image.dd /mnt/forensic

# Extract metadata from files
exiftool -r /suspicious/directory

# Analyze browser history
sqlite3 ~/.mozilla/firefox/*.default*/places.sqlite \
"SELECT datetime(visit_date/1000000, 'unixepoch'), url FROM moz_places ORDER BY visit_date DESC LIMIT 100"
```

## Best Practices for Non-Disruptive Command Usage

- **Portability:** Account for differences across Linux distributions.
    
    ```bash
    # Distribution detection
    if [ -f /etc/debian_version ]; then
      DISTRO="debian"
    elif [ -f /etc/redhat-release ]; then
      DISTRO="redhat"
    fi
    
    # Command availability checking
    command -v systemctl > /dev/null 2>&1 && USE_SYSTEMD=true
    
    # Portable package listing
    get_installed_packages() {
      if command -v dpkg > /dev/null; then
        dpkg -l
      elif command -v rpm > /dev/null; then
        rpm -qa
      fi
    }
    ```
    
- **Resource Management:** Use `nice`, `ionice`, `timeout`, and `ulimit` to limit resource usage.
- **Logging:** Enable command logging to maintain an audit trail.
- **Testing:** Test commands in a non-production environment first.

## Conclusion

The Linux command line is a powerful tool for cybersecurity professionals. This guide organizes essential commands into clear categories, ensuring proper formatting and completeness. Regular use of these commands, combined with automation and best practices, enhances system security, incident response, and forensic analysis capabilities.  

Credit: `@_0b1d1`
