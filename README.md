# Agent Zero

[![Join our Discord](https://img.shields.io/badge/Discord-Join%20our%20server-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/B8KZKNsPpj) [![Subscribe on YouTube](https://img.shields.io/badge/YouTube-Subscribe-red?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@AgentZeroFW) [![Connect on LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jan-tomasek/) [![Follow on X.com](https://img.shields.io/badge/X.com-Follow-1DA1F2?style=for-the-badge&logo=x&logoColor=white)](https://x.com/JanTomasekDev)



[![Intro Video](/docs/intro_vid.jpg)](https://www.youtube.com/watch?v=C9n8zFpaV3I)

**Personal and organic AI framework**
- Agent Zero is not a predefined agentic framework. It is designed to be dynamic, organically growing, and learning as you use it.
- Agent Zero is fully transparent, readable, comprehensible, customizable and interactive.
- Agent Zero uses the computer as a tool to accomplish its (your) tasks.

## Key concepts
1. **General-purpose assistant**
- Agent Zero is not pre-programmed for specific tasks (but can be). It is meant to be a general-purpose personal assistant. Give it a task, and it will gather information, execute commands and code, cooperate with other agent instances, and do its best to accomplish it.
- It has a persistent memory, allowing it to memorize previous solutions, code, facts, instructions, etc., to solve tasks faster and more reliably in the future.

2. **Computer as a tool**
- Agent Zero uses the operating system as a tool to accomplish its tasks. It has no single-purpose tools pre-programmed. Instead, it can write its own code and use the terminal to create and use its own tools as needed.
- The only default tools in its arsenal are online search, memory features, communication (with the user and other agents), and code/terminal execution. Everything else is created by the agent itself or can be extended by the user.
- Tool usage functionality has been developed from scratch to be the most compatible and reliable, even with very small models.

3. **Multi-agent cooperation**
- Every agent has a superior agent giving it tasks and instructions. Every agent then reports back to its superior.
- In the case of the first agent, the superior is the human user; the agent sees no difference.
- Every agent can create its subordinate agent to help break down and solve subtasks. This helps all agents keep their context clean and focused.

4. **Completely customizable and extensible**
- Almost nothing in this framework is hard-coded. Nothing is hidden. Everything can be extended or changed by the user.
- The whole behavior is defined by a system prompt in the **prompts/agent.system.md** file. Change this prompt and change the framework dramatically.
- The framework does not guide or limit the agent in any way. There are no hard-coded rails that agents have to follow.
- Every prompt, every small message template sent to the agent in its communication loop, can be found in the **prompts/** folder and changed.
- Every default tool can be found in the **python/tools/** folder and changed or copied to create new predefined tools.
- Of course, it is open-source (except for some tools like Perplexity, but that will be replaced with an open-source alternative as well in the future).

5. **Communication is key**
- Give your agent a proper system prompt and instructions, and it can do miracles.
- Agents can communicate with their superiors and subordinates, asking questions, giving instructions, and providing guidance. Instruct your agents in the system prompt on how to communicate effectively.
- The terminal interface is real-time streamed and interactive. You can stop and intervene at any point. If you see your agent heading in the wrong direction, just stop and tell it right away.
- There is a lot of freedom in this framework. You can instruct your agents to regularly report back to superiors asking for permission to continue. You can instruct them to use point-scoring systems when deciding when to delegate subtasks. Superiors can double-check subordinates' results and dispute. The possibilities are endless.

![Agent Zero](docs/splash_wide.png)

## Nice features to have
- Output is very clean, colorful, readable and interactive; nothing is hidden.
- The same colorful output you see in the terminal is automatically saved to HTML file in **logs/** folder for every session.
- Agent output is streamed in real-time, allowing the user to read along and intervene at any time.
- No coding is required, only prompting and communication skills.
- With a solid system prompt, the framework is reliable even with small models, including precise tool usage.

## Keep in mind
1. **Agent Zero can be dangerous!**
With proper instruction, Agent Zero is capable of many things, even potentially dangerous to your computer, data, or accounts. Always run Agent Zero in an isolated environment (like the built in docker container) and be careful what you wish for.

2. **Agent Zero is not pre-programmed; it is prompt-based.**
The whole framework contains only a minimal amount of code and does not guide the agent in any way.
Everything lies in the system prompt in the **prompts/** folder. Here you can rewrite the whole framework behavior to your needs.
If your agent fails to communicate properly, use tools, reason, use memory, find answers - just instruct it better.

3. **If you cannot provide the ideal environment, let your agent know.**
Agent Zero is made to be used in an isolated virtual environment (for safety) with some tools preinstalled and configured.
If you cannot provide all the necessary conditions or API keys, just change the system prompt and tell your agent what operating system and tools are at its disposal. Nothing is hard-coded; if you do not tell your agent about a certain tool, it will not know about it and will not try to use it.

[![David Ondrej video](/docs/david_vid.jpg)](https://www.youtube.com/watch?v=_Pionjv4hGc)

## Known problems
1. The system prompt sucks. You can do better. If you do, help me please :)
2. The communication between agent and terminal in docker container via SSH can sometimes break and stop producing outputs. Sometimes it is because the agent runs something like "server.serve_forever()" which causes the terminal to hang, sometimes a random error can occur. Restarting the agent and/or the docker container helps.
3. The agent can break his operating system. Sometimes the agent can deactivate virtual environment, uninstall packages, change config etc. Again, removing the docker container and cleaning up the **work_dir/** is enough to fix that.

## Ideal environment
- **Docker container**: The perfect environment to run Agent Zero is the built-in docker container. The agent can download the image **frdel/agent-zero-exe** on its own and start the container, you only need to have docker running (like the Docker Desktop application).
- **Python**: Python has to be installed on the system to run the framework.
- **Internet access**: The agent will need internet access to use its online knowledge tool and execute commands and scripts requiring a connection. If you do not need your agent to be online, you can alter its prompts in the **prompts/** folder and make it fully local.

![Time example](docs/time_example.jpg)

## Setup

Update: [Guide by CheezChat for Windows](./docs/win_installation_guide.txt)

1. **Required API keys:**
- At the moment, the only recommended API key is for https://www.perplexity.ai/ API. Perplexity is used as a convenient web search tool and has not yet been replaced by an open-source alternative. If you do not have an API key for Perplexity, leave it empty in the .env file and Perplexity will not be used.
- Chat models and embedding models can be executed locally via Ollama and HuggingFace or via API as well.

2. **Enter your API keys:**
- You can enter your API keys into the **.env** file, which you can copy from **example.env**
- Or you can export your API keys in the terminal session:
~~~bash
export API_KEY_PERPLEXITY="your-api-key-here"
export API_KEY_OPENAI="your-api-key-here"
~~~

3. **Install dependencies with the following terminal command:**
~~~bash
pip install -r requirements.txt
~~~

3. **Choose your chat, utility and embeddings model:**
- In the **main.py** file, right at the start of the **chat()** function, you can see how the chat model and embedding model are set.
- You can choose between online models (OpenAI, Anthropic, Groq) or offline (Ollama, HuggingFace) for both.

4. **run Docker:**
- Easiest way is to install Docker Desktop application and just run it. The rest will be handled by the framework itself.

## Run the program
- Just run the **main.py** file in Python:
~~~bash
python main.py
~~~
- Or run it in debug mode in VS Code using the **debug** button in the top right corner of the editor. I have provided config files for VS Code for this purpose.

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
