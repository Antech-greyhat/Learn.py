#!/usr/bin/env python3
import socket
import argparse
import sys
import concurrent.futures
from datetime import datetime


def resolve_target(target: str) -> str:
    try:
        ip = socket.gethostbyname(target)
        if ip != target:
            print(f"[*] Resolved {target} -> {ip}")
        return ip
    except socket.gaierror:
        print(f"[!] Could not resolve {target}.")
        sys.exit(1)


def scan_port(ip: str, port: int, timeout: float, grab_banner: bool):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            if sock.connect_ex((ip, port)) != 0:
                return (port, "closed", "")
            banner = ""
            if grab_banner:
                try:
                    sock.settimeout(0.8)
                    banner = sock.recv(1024).decode(errors="ignore").strip()
                except (socket.timeout, ConnectionResetError):
                    banner = ""
            return (port, "open", banner)
    except (socket.error, OSError):
        return (port, "error", "")


def parse_ports(spec: str):
    ports = set()
    for chunk in spec.split(","):
        chunk = chunk.strip()
        if "-" in chunk:
            start, end = chunk.split("-", 1)
            ports.update(range(int(start), int(end) + 1))
        else:
            ports.add(int(chunk))
    return sorted(p for p in ports if 1 <= p <= 65535)


def sweep(ip: str, ports, threads: int, timeout: float, grab_banner: bool):
    open_ports = []
    print(f"[*] Sweeping {len(ports)} ports on {ip} with {threads} threads...\n")
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as pool:
        futures = {pool.submit(scan_port, ip, p, timeout, grab_banner): p for p in ports}
        for future in concurrent.futures.as_completed(futures):
            port, state, banner = future.result()
            if state == "open":
                label = f"port {port:<6} OPEN"
                if banner:
                    label += f"  |  {banner[:80]}"
                print(f"[+] {label}")
                open_ports.append((port, banner))
    return open_ports


def main():
    parser = argparse.ArgumentParser(description="IP + open-port scraper")
    parser.add_argument("host")
    parser.add_argument("--ports", default="1-1024")
    parser.add_argument("--threads", type=int, default=100)
    parser.add_argument("--timeout", type=float, default=1.0)
    parser.add_argument("--banner", action="store_true")
    args = parser.parse_args()

    start = datetime.now()
    ip = resolve_target(args.host)
    ports = parse_ports(args.ports)
    results = sweep(ip, ports, args.threads, args.timeout, args.banner)
    elapsed = (datetime.now() - start).total_seconds()
    print(f"\n[=] Done. {len(results)} open port(s) on {ip} in {elapsed:.2f}s.")


if __name__ == "__main__":
    main()
