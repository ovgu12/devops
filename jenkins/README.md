# jenkins

## Debian agent

Launch agent container

```sh
docker run -d --name=agent --publish 22:22 -e "JENKINS_AGENT_SSH_PUBKEY=<PUB_KEY>" jenkins/ssh-agent
```

Python install in agent

```sh
apt update
apt install python3 python3-pip
```

Build new image and then push to hub

```sh
docker container commit -a "ovgu12" -m "Add python3 to container" agent ovgu12/linux:latest
docker push ovgu12/linux:latest
```
