# Comprehensive NVIDIA Docker Setup on Ubuntu WSL2

This guide provides detailed instructions for setting up NVIDIA Docker on Ubuntu within WSL2 (Windows Subsystem for Linux 2). It's designed for users of all experience levels, including those new to Ubuntu and Docker.

## Prerequisites

Before you start, ensure you have:

- **Windows 11** with WSL2 enabled
- An **NVIDIA GPU** with the latest drivers installed on Windows
- **Docker Desktop** installed and configured to use WSL2

## Installation Steps

### 1. Install Ubuntu on WSL2

Install Ubuntu from the Microsoft Store if you haven't already.

### 2. Install NVIDIA Docker Toolkit

#### Add NVIDIA Docker Repository Key

```bash
sudo curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg
```

#### Set Up the CUDA Repository

Due to issues with the 22.04 repository, use the 18.04 repository:

```bash
echo "deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://nvidia.github.io/libnvidia-container/stable/ubuntu18.04/amd64 /" | sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
```

#### Update and Install NVIDIA Docker

```bash
sudo apt-get update
sudo apt-get install -y nvidia-docker2
```

#### Restart Docker Daemon

```bash
sudo systemctl restart docker
```

#### Add User to Docker Group

```bash
sudo usermod -aG docker $USER
```

Log out and back in for this change to take effect.

### 3. Configure Docker for NVIDIA Runtime

Edit the Docker daemon configuration:

```bash
sudo nano /etc/docker/daemon.json
```

Add or update the following configuration:

```json
{
  "default-runtime": "nvidia",
  "runtimes": {
    "nvidia": {
      "path": "nvidia-container-runtime",
      "runtimeArgs": []
    }
  }
}
```

Save and exit, then restart Docker:

```bash
sudo systemctl restart docker
```

### 4. Verify NVIDIA Docker Installation

Run this command to check if NVIDIA Docker is set up correctly:

```bash
docker run --rm --gpus all nvidia/cuda:11.0.3-base-ubuntu20.04 nvidia-smi
```

You should see information about your NVIDIA GPU.

### 5. Enable Docker to Start on Boot

```bash
sudo systemctl enable docker
```

### 6. Ensure Persistence of NVIDIA Runtime

To make sure the NVIDIA runtime remains the default across restarts:

#### Create a Startup Script

```bash
nano ~/.docker_startup.sh
```

Add the following content:

```bash
#!/bin/bash
sudo ln -sf /usr/libexec/docker/cli-plugins/docker-buildx /usr/local/lib/docker/cli-plugins/
sudo ln -sf /usr/libexec/docker/cli-plugins/docker-compose /usr/local/lib/docker/cli-plugins/
sudo service docker restart
```

#### Make the Script Executable

```bash
chmod +x ~/.docker_startup.sh
```

#### Edit .bashrc

```bash
nano ~/.bashrc
```

Add this line at the end:

```bash
[ -f ~/.docker_startup.sh ] && ~/.docker_startup.sh
```

### 7. Configure WSL2 for Systemd

Edit or create the WSL configuration file:

```bash
sudo nano /etc/wsl.conf
```

Add the following content:

```
[boot]
systemd=true
```

Save and exit the editor.

### 8. Configure Docker Desktop

To prevent Docker Desktop from overriding your WSL2 settings:

1. Open Docker Desktop settings
2. Go to the "Docker Engine" configuration tab
3. Update the configuration to include:

```json
{
  "builder": {
    "gc": {
      "defaultKeepStorage": "20GB",
      "enabled": true
    }
  },
  "experimental": false,
  "runtimes": {
    "nvidia": {
      "path": "/usr/bin/nvidia-container-runtime",
      "runtimeArgs": []
    }
  },
  "default-runtime": "nvidia"
}
```

4. Apply changes and restart Docker Desktop

## Verifying Setup

After completing all steps:

1. Restart your WSL2 instance:
   In a Windows PowerShell (run as administrator):
   ```
   wsl --shutdown
   ```
   Then reopen your Ubuntu terminal.

2. Check Docker runtime:
   ```bash
   docker info | grep -i runtime
   ```

3. Verify NVIDIA is still the default runtime and no warnings appear about missing plugins.

## Troubleshooting

If you encounter issues during setup or operation, follow these steps:

### 1. Check Current Docker Runtime Settings

```bash
docker info | grep -i runtime
```

Ensure `nvidia` is listed as a runtime and set as default.

### 2. Reinstall NVIDIA Docker Components

If runtime settings are incorrect, try reinstalling:

```bash
sudo apt-get remove --purge docker-ce docker-ce-cli containerd.io nvidia-docker2
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io nvidia-docker2
```

### 3. Update Docker Daemon Configuration

Ensure `/etc/docker/daemon.json` contains the correct configuration as shown in step 3 of the installation process.

### 4. Restart Docker and Verify

After making changes:

```bash
sudo systemctl restart docker
docker info | grep -i runtime
```

### 5. Test GPU Access

```bash
docker run --rm --gpus all nvidia/cuda:11.0.3-base-ubuntu20.04 nvidia-smi
```

### 6. Resolving Plugin Warnings

If you see warnings about missing Docker plugins:

```bash
ls -l /usr/local/lib/docker/cli-plugins/
ls -l /usr/libexec/docker/cli-plugins/
```

If the symlinks are incorrect or missing, recreate them:

```bash
sudo rm /usr/local/lib/docker/cli-plugins/docker-buildx
sudo rm /usr/local/lib/docker/cli-plugins/docker-compose
sudo ln -s /usr/libexec/docker/cli-plugins/docker-buildx /usr/local/lib/docker/cli-plugins/
sudo ln -s /usr/libexec/docker/cli-plugins/docker-compose /usr/local/lib/docker/cli-plugins/
```

### 7. Docker Desktop and WSL2 Sync Issues

If Docker Desktop isn't syncing properly with Ubuntu WSL2:

1. Verify WSL2 integration is enabled in Docker Desktop settings.
2. Restart Docker Desktop and WSL2 (`wsl --shutdown` in Windows PowerShell).
3. Ensure Docker Desktop is set to use the WSL2 backend.
4. Disable any local Docker distributions, leaving only the Ubuntu WSL2 distribution enabled.
5. Check file sharing permissions for accessed directories.
6. Consider reinstalling Docker Desktop if issues persist.

## Additional Resources

- [NVIDIA Docker Documentation](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/overview.html)
- [Docker Documentation](https://docs.docker.com/)
- [Microsoft WSL2 Documentation](https://docs.microsoft.com/en-us/windows/wsl/)

Remember to always check for the latest updates and best practices in the official documentation.
