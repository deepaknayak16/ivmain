
# This is the actual memoization function that takes a function `f` as input and returns a decorated version of `f` that caches the results of previous calls to `f`.
def memoize(f):
    cache = {}
    def decorated_function(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorated_function

#This decorates the function to use a cache! Woohoo
@memoize
def fib(n):
    if n ==0:
        return 0
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

import os, platform, subprocess

# Quick check
is_remote = any(var in os.environ for var in ['SSH_CONNECTION', 'SSH_CLIENT', 'REMOTE_SESSION'])
if not is_remote and platform.system() == "Windows":
    try:
        result = subprocess.run(['query', 'session'], capture_output=True, text=True, shell=True)
        is_remote = "rdp-tcp" in result.stdout.lower()
    except: pass

print("Remote:" if is_remote else "Local:")

import os
import platform
import subprocess

def check_remote_system():
    """Check if system is remote without any external dependencies"""
    
    print("🔍 Checking if system is remote or local...")
    print(f"Platform: {platform.system()}")
    print(f"Hostname: {platform.node()}")
    
    # Check environment variables
    remote_env_vars = ['SSH_CONNECTION', 'SSH_CLIENT', 'REMOTE_SESSION', 'TMUX']
    found_vars = []
    
    for var in remote_env_vars:
        if var in os.environ:
            found_vars.append(f"{var}={os.environ[var]}")
    
    if found_vars:
        print("🚨 REMOTE SYSTEM DETECTED")
        print("Environment variables found:")
        for var in found_vars:
            print(f"  - {var}")
        return True
    
    # Windows specific checks
    if platform.system() == "Windows":
        try:
            # Check for RDP sessions
            result = subprocess.run(
                ['query', 'session'], 
                capture_output=True, text=True, shell=True
            )
            if "rdp-tcp" in result.stdout.lower():
                print("🚨 REMOTE SYSTEM DETECTED")
                print("Windows RDP session found")
                return True
        except:
            pass
    
    # Linux/Mac specific checks  
    else:
        try:
            # Check who command for remote sessions
            result = subprocess.run(['who'], capture_output=True, text=True)
            for line in result.stdout.split('\n'):
                if line.strip() and '(' in line and ')' in line:
                    if ':0' not in line and ':1' not in line:
                        print("🚨 REMOTE SYSTEM DETECTED")
                        print(f"Remote session: {line}")
                        return True
        except:
            pass
    
    print("✅ LOCAL SYSTEM - No remote indicators found")
    return False

if __name__ == "__main__":
    check_remote_system()




import os
import platform
import socket
import subprocess
import psutil
from typing import Dict, List, Tuple

class SystemIdentityChecker:
    def __init__(self):
        self.system_info = {}
        self.is_remote = False
        self.connection_type = "Local"
        self.confidence_level = "Unknown"
        
    def collect_system_info(self) -> Dict:
        """Collect comprehensive system information"""
        info = {}
        
        # Basic system info
        info['hostname'] = socket.gethostname()
        info['platform'] = platform.system()
        info['platform_release'] = platform.release()
        info['platform_version'] = platform.version()
        info['architecture'] = platform.machine()
        info['processor'] = platform.processor()
        
        # Network info
        info['local_ip'] = socket.gethostbyname(socket.gethostname())
        try:
            info['fqdn'] = socket.getfqdn()
        except:
            info['fqdn'] = info['hostname']
            
        return info
    
    def check_environment_variables(self) -> Tuple[bool, str]:
        """Check environment variables for remote session indicators"""
        env_checks = {
            'SESSIONNAME': {
                'values': ['rdp-tcp', 'console'],
                'remote_if': 'rdp-tcp'
            },
            'SSH_CONNECTION': {
                'exists': True,
                'remote_if': True
            },
            'SSH_CLIENT': {
                'exists': True,
                'remote_if': True
            },
            'REMOTE_SESSION': {
                'values': ['1', 'true'],
                'remote_if': True
            },
            'XDG_SESSION_TYPE': {
                'values': ['x11', 'wayland'],
                'remote_if': None  # Not definitive for remote
            },
            'TERM': {
                'values': ['xterm-256color', 'screen', 'tmux'],
                'remote_if': None  # Could be local or remote
            },
            'TMUX': {
                'exists': True,
                'remote_if': True
            }
        }
        
        for var, conditions in env_checks.items():
            if var in os.environ:
                var_value = os.environ[var].lower()
                print(f"  Environment {var}: {os.environ[var]}")
                
                if 'values' in conditions and conditions['remote_if']:
                    if var_value in [v.lower() for v in conditions['values']]:
                        return True, f"Environment variable {var}"
                
                if 'exists' in conditions and conditions['exists']:
                    if conditions['remote_if']:
                        return True, f"Environment variable {var} exists"
        
        return False, "No remote indicators in environment"
    
    def check_windows_remote(self) -> Tuple[bool, str]:
        """Check for Windows remote desktop sessions"""
        if platform.system() != "Windows":
            return False, "Not Windows system"
            
        methods = [
            self._check_windows_registry,
            self._check_windows_services,
            self._check_windows_sessions,
            self._check_windows_processes,
            self._check_windows_systeminfo
        ]
        
        for method in methods:
            is_remote, reason = method()
            if is_remote:
                return True, reason
                
        return False, "No Windows remote indicators found"
    
    def _check_windows_registry(self) -> Tuple[bool, str]:
        """Check Windows registry for RDP settings"""
        try:
            # Check if RDP is enabled
            result = subprocess.run(
                ['reg', 'query', 'HKLM\\SYSTEM\\CurrentControlSet\\Control\\Terminal Server', 
                 '/v', 'fDenyTSConnections'], 
                capture_output=True, text=True, shell=True
            )
            if result.returncode == 0 and "0x0" in result.stdout:
                return True, "RDP enabled in registry"
        except:
            pass
        return False, ""
    
    def _check_windows_services(self) -> Tuple[bool, str]:
        """Check if RDP services are running"""
        try:
            services = ['TermService', 'UmRdpService', 'SessionEnv']
            for service in services:
                result = subprocess.run(
                    ['sc', 'query', service], 
                    capture_output=True, text=True, shell=True
                )
                if "RUNNING" in result.stdout:
                    return True, f"RDP service {service} running"
        except:
            pass
        return False, ""
    
    def _check_windows_sessions(self) -> Tuple[bool, str]:
        """Check terminal server sessions"""
        try:
            # Try qwinsta first
            result = subprocess.run(['qwinsta'], capture_output=True, text=True, shell=True)
            if "rdp-tcp" in result.stdout.lower():
                return True, "RDP session active (qwinsta)"
        except:
            try:
                # Fallback to query session
                result = subprocess.run(['query', 'session'], capture_output=True, text=True, shell=True)
                if "rdp-tcp" in result.stdout.lower():
                    return True, "RDP session active (query session)"
            except:
                pass
        return False, ""
    
    def _check_windows_processes(self) -> Tuple[bool, str]:
        """Check for RDP-related processes"""
        rdp_processes = ['rdpclip.exe', 'rdpapp.exe', 'mstsc.exe']
        try:
            result = subprocess.run(['tasklist'], capture_output=True, text=True, shell=True)
            for process in rdp_processes:
                if process in result.stdout.lower():
                    return True, f"RDP process {process} running"
        except:
            pass
        return False, ""
    
    def _check_windows_systeminfo(self) -> Tuple[bool, str]:
        """Check systeminfo for remote desktop status"""
        try:
            result = subprocess.run(['systeminfo'], capture_output=True, text=True, shell=True)
            for line in result.stdout.split('\n'):
                if "Remote Desktop" in line and "Yes" in line:
                    return True, "Remote Desktop enabled (systeminfo)"
        except:
            pass
        return False, ""
    
    def check_linux_remote(self) -> Tuple[bool, str]:
        """Check for Linux remote sessions"""
        if platform.system() not in ["Linux", "Darwin"]:
            return False, "Not Linux/macOS system"
            
        methods = [
            self._check_linux_who,
            self._check_linux_processes,
            self._check_linux_ssh,
            self._check_linux_display
        ]
        
        for method in methods:
            is_remote, reason = method()
            if is_remote:
                return True, reason
                
        return False, "No Linux remote indicators found"
    
    def _check_linux_who(self) -> Tuple[bool, str]:
        """Check who command for remote sessions"""
        try:
            result = subprocess.run(['who'], capture_output=True, text=True)
            lines = result.stdout.strip().split('\n')
            
            for line in lines:
                if '(' in line and ')' in line:
                    return True, f"Remote session detected: {line}"
                if ':0' not in line and ':1' not in line:
                    return True, f"Non-local session: {line}"
                    
        except:
            pass
        return False, ""
    
    def _check_linux_processes(self) -> Tuple[bool, str]:
        """Check for remote desktop processes on Linux"""
        try:
            result = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
            remote_indicators = [
                'vnc', 'xrdp', 'tightvnc', 'tigervnc', 'remote-desktop',
                'ssh:', 'x11vnc', 'vinagre', 'remmina'
            ]
            
            for line in result.stdout.split('\n'):
                line_lower = line.lower()
                if any(indicator in line_lower for indicator in remote_indicators):
                    return True, f"Remote process: {line[:50]}..."
                    
        except:
            pass
        return False, ""
    
    def _check_linux_ssh(self) -> Tuple[bool, str]:
        """Check for SSH connections"""
        try:
            # Check SSH environment variables
            if 'SSH_CONNECTION' in os.environ or 'SSH_CLIENT' in os.environ:
                return True, "SSH connection detected"
                
            # Check SSH processes
            result = subprocess.run(['netstat', '-an'], capture_output=True, text=True)
            if ':22' in result.stdout and 'ESTABLISHED' in result.stdout:
                return True, "SSH port connection detected"
                        
        except:
            pass
        return False, ""
    
    def _check_linux_display(self) -> Tuple[bool, str]:
        """Check DISPLAY variable for remote X11"""
        if 'DISPLAY' in os.environ:
            display = os.environ['DISPLAY']
            if ':' in display and not display.startswith(':0'):
                return True, f"Remote X11 display: {display}"
        return False, ""
    
    def check_network_connections(self) -> Tuple[bool, str]:
        """Check network connections for remote session indicators"""
        remote_ports = {
            3389: "RDP",
            5900: "VNC",
            5901: "VNC",
            22: "SSH",
            23: "Telnet",
            5939: "TeamViewer"
        }
        
        try:
            # Use netstat to check connections
            if platform.system() == "Windows":
                result = subprocess.run(['netstat', '-an'], capture_output=True, text=True, shell=True)
            else:
                result = subprocess.run(['netstat', '-an'], capture_output=True, text=True)
            
            for port, service in remote_ports.items():
                if f":{port}" in result.stdout and "ESTABLISHED" in result.stdout:
                    return True, f"Remote {service} connection detected"
                        
        except Exception as e:
            return False, f"Error checking network: {e}"
            
        return False, "No remote network connections detected"
    
    def determine_confidence(self, indicators: List[Tuple[bool, str]]) -> str:
        """Determine confidence level based on indicators found"""
        remote_count = sum(1 for is_remote, _ in indicators if is_remote)
        total_checks = len(indicators)
        
        if remote_count == 0:
            return "High - Local"
        elif remote_count >= 3:
            return "High - Remote"
        elif remote_count >= 2:
            return "Medium - Remote"
        elif remote_count == 1:
            return "Low - Possible Remote"
        else:
            return "Unknown"
    
    def analyze_system(self):
        """Main analysis function"""
        print("🔍 Analyzing System Identity...")
        print("=" * 60)
        
        # Collect basic info
        self.system_info = self.collect_system_info()
        print(f"System: {self.system_info['platform']} {self.system_info['platform_release']}")
        print(f"Hostname: {self.system_info['hostname']}")
        print(f"IP Address: {self.system_info['local_ip']}")
        
        print("\n🧩 Running Detection Methods...")
        print("-" * 40)
        
        # Run all detection methods
        indicators = []
        
        # Environment variables check
        env_remote, env_reason = self.check_environment_variables()
        indicators.append((env_remote, f"Environment: {env_reason}"))
        print(f"Environment Check: {env_reason}")
        
        # Platform-specific checks
        if platform.system() == "Windows":
            win_remote, win_reason = self.check_windows_remote()
            indicators.append((win_remote, f"Windows: {win_reason}"))
            print(f"Windows RDP Check: {win_reason}")
        else:
            linux_remote, linux_reason = self.check_linux_remote()
            indicators.append((linux_remote, f"Linux: {linux_reason}"))
            print(f"Linux/Mac Check: {linux_reason}")
        
        # Network connections check
        net_remote, net_reason = self.check_network_connections()
        indicators.append((net_remote, f"Network: {net_reason}"))
        print(f"Network Check: {net_reason}")
        
        # Determine final result
        remote_indicators = [reason for is_remote, reason in indicators if is_remote]
        
        if remote_indicators:
            self.is_remote = True
            self.connection_type = " | ".join(remote_indicators)
        else:
            self.is_remote = False
            self.connection_type = "Local Session"
        
        self.confidence_level = self.determine_confidence(indicators)
        
        # Display final results
        self.display_results(remote_indicators)
    
    def display_results(self, remote_indicators: List[str]):
        """Display final analysis results"""
        print("\n" + "=" * 60)
        print("🎯 SYSTEM IDENTITY ANALYSIS RESULTS")
        print("=" * 60)
        
        if self.is_remote:
            print("🚨 STATUS: REMOTE SYSTEM")
            print(f"🔗 Connection Type: {self.connection_type}")
            print(f"📊 Confidence: {self.confidence_level}")
            print("\n📋 Remote Indicators Found:")
            for indicator in remote_indicators:
                print(f"   • {indicator}")
        else:
            print("✅ STATUS: LOCAL SYSTEM")
            print(f"📊 Confidence: {self.confidence_level}")
            print("\n💡 No remote session indicators detected")
        
        print("\n🔧 System Information:")
        print(f"   Hostname: {self.system_info['hostname']}")
        print(f"   Platform: {self.system_info['platform']} {self.system_info['platform_release']}")
        print(f"   Architecture: {self.system_info['architecture']}")
        print("=" * 60)

# Simple one-line check function
def is_remote_system() -> bool:
    """Quick check to determine if system is remote"""
    # Check common environment variables
    remote_env_vars = ['SSH_CONNECTION', 'SSH_CLIENT', 'REMOTE_SESSION']
    if any(var in os.environ for var in remote_env_vars):
        return True
    
    # Check Windows RDP
    if platform.system() == "Windows":
        try:
            result = subprocess.run(['query', 'session'], capture_output=True, text=True, shell=True)
            return "rdp-tcp" in result.stdout.lower()
        except:
            pass
    
    # Check Linux/Mac
    else:
        try:
            result = subprocess.run(['who'], capture_output=True, text=True)
            return any('(' in line and ')' in line for line in result.stdout.split('\n'))
        except:
            pass
    
    return False

# Quick check function
def quick_remote_check():
    """Simple one-function remote system check"""
    
    # Check environment variables
    remote_env = ['SSH_CONNECTION', 'SSH_CLIENT', 'REMOTE_SESSION', 'TMUX']
    for var in remote_env:
        if var in os.environ:
            return True, f"Environment variable: {var}"
    
    # Platform-specific checks
    if platform.system() == "Windows":
        try:
            # Check RDP session
            result = subprocess.run(
                ['query', 'session'], 
                capture_output=True, text=True, shell=True
            )
            if "rdp-tcp" in result.stdout.lower():
                return True, "Windows RDP Session"
        except:
            pass
    else:
        # Linux/Mac
        try:
            result = subprocess.run(['who'], capture_output=True, text=True)
            for line in result.stdout.split('\n'):
                if '(' in line and ')' in line and ':0' not in line:
                    return True, f"Remote session: {line.split()[0]}"
        except:
            pass
    
    return False, "Local session"

# Usage
if __name__ == "__main__":
    # Method 1: Comprehensive analysis
    print("Comprehensive System Identity Analysis")
    print("=" * 50)
    checker = SystemIdentityChecker()
    checker.analyze_system()
    
    print("\n" + "=" * 50)
    
    # Method 2: Quick check
    print("Quick Check:")
    if is_remote_system():
        print("🔴 This appears to be a REMOTE system")
    else:
        print("🟢 This appears to be a LOCAL system")