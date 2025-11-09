#!/usr/bin/env python3
"""
Custom Security Check Script
Performs additional DAST/SAST checks during pre-commit
"""
import subprocess
import sys
import os
from pathlib import Path


def run_prospector():
    """Run prospector for static code analysis"""
    print("Running prospector for static code analysis...")
    try:
        result = subprocess.run([
            sys.executable, "-m", "prospector",
            "--tool", "pylint",
            "--tool", "pycodestyle",
            "--tool", "mccabe",
            "--output-format", "json",
            "--max-line-length", "100"
        ], capture_output=True, text=True, check=False)
        
        if result.returncode != 0:
            print("Prospector found issues:")
            print(result.stdout)
            if result.stderr:
                print(result.stderr)
            return False
        else:
            print("Prospector passed")
            return True
    except FileNotFoundError:
        print("Prospector not found. Install with: pip install prospector")
        return False


def run_opengrep():
    """Run opengrep for security analysis"""
    print("Running opengrep for security analysis...")
    try:
        result = subprocess.run([
            "opengrep",
            "--config", "opengrep.yaml"
        ], capture_output=True, text=True, check=False)
        
        if result.returncode != 0:
            print("OpenGrep found security issues:")
            print(result.stdout)
            if result.stderr:
                print(result.stderr)
            return False
        else:
            print("OpenGrep security scan passed")
            return True
    except FileNotFoundError:
        print("OpenGrep not found. Install with: pip install opengrep")
        return False


def check_dependencies():
    """Check if required tools are installed"""
    deps = ['prospector', 'opengrep']
    missing = []
    
    for dep in deps:
        try:
            # Try to run the command to see if it's available
            subprocess.run([dep, '--help'], 
                         capture_output=True, 
                         check=False)
        except FileNotFoundError:
            missing.append(dep)
    
    if missing:
        print(f"Missing dependencies: {', '.join(missing)}")
        print("Install with: pip install " + " ".join(missing))
        return False
    
    return True


def main():
    """Main security check function"""
    print("Starting custom security checks...")
    
    # Check if required tools are available
    if not check_dependencies():
        return 1
    
    # Run the security checks
    prospector_ok = run_prospector()
    opengrep_ok = run_opengrep()
    
    # Return appropriate exit code
    if prospector_ok and opengrep_ok:
        print("All security checks passed!")
        return 0
    else:
        print("Some security checks failed!")
        return 1


if __name__ == "__main__":
    sys.exit(main())