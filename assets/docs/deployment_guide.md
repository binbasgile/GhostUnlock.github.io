# GhostUnlock SaaS - Quick Deploy Guide

## Prerequisites
- Ubuntu 20.04 / Debian 11+ Server (DigitalOcean, Vultr, AWS EC2).
- Python 3.10 installed (`sudo apt-get install python3-pip python3-venv`).
- Git installed for cloning the repository.

## Step 1: Clone & Configure
```bash
git clone <your_github_repo> 
cd ghostunlock

# Edit config.yaml if changing default ports or DB types
nano assets/config.yaml # Change port from 8000 to 81/82 if using Nginx reverse proxy later
