# jenkins

## Debian agent

Launch agent container

```sh
docker run -d --name=agent --publish 22:22 -e "JENKINS_AGENT_SSH_PUBKEY=ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCmbRvCQzt7Z28XAGVhaEH5kbe9lHEMH6h3eZ+yTncOlSj1R7gq9Rhai3dLiZkM2Oi5ccU4/Zp1O1WTGxJ0m1H0Jr89mxaQ2Geov8EQ2NMt07YBiuXbNRdC6u33t0HhXoWQyJcd1X0nJTypHHjxPOrVF62QFc21/mOF9nTeUdoGF2Uef3cQPgI7ySf6Q0/r8AiBSUS2decYaMd1sVjh70VirUVo6ciVAv/+KoNs7D7qN5u1Nqu+swTmWzJWawappyzX72Se2NfpCe8W3D6x9lh9FfDa4nlbm4ytiIh2Cpu2bbyscUG3RFDVBwZ36cZUJ51A1az9QWbpRtMs74WdU1ORH3jy3G70hGU+kxwi8MpBBD3MoVGUzYfgKpD+ez7F4xcuyXSIbjASvjaaAbdp7kR3ZM3Y+/ttR5vb7ukeFCBoEd8CnjhnCaokDNT3hUgUUXVmnXxIC4bEAUUEzo6IZOAoN3WKTkOobd/1Sf69bOpjzwWsUOExErcevqqUUcapJv0= hoangvu@dehvu12.local" jenkins/ssh-agent
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

Start agent1

```sh
docker run -d --name=agent1 --publish 2200:22 -e "JENKINS_AGENT_SSH_PUBKEY=ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCmbRvCQzt7Z28XAGVhaEH5kbe9lHEMH6h3eZ+yTncOlSj1R7gq9Rhai3dLiZkM2Oi5ccU4/Zp1O1WTGxJ0m1H0Jr89mxaQ2Geov8EQ2NMt07YBiuXbNRdC6u33t0HhXoWQyJcd1X0nJTypHHjxPOrVF62QFc21/mOF9nTeUdoGF2Uef3cQPgI7ySf6Q0/r8AiBSUS2decYaMd1sVjh70VirUVo6ciVAv/+KoNs7D7qN5u1Nqu+swTmWzJWawappyzX72Se2NfpCe8W3D6x9lh9FfDa4nlbm4ytiIh2Cpu2bbyscUG3RFDVBwZ36cZUJ51A1az9QWbpRtMs74WdU1ORH3jy3G70hGU+kxwi8MpBBD3MoVGUzYfgKpD+ez7F4xcuyXSIbjASvjaaAbdp7kR3ZM3Y+/ttR5vb7ukeFCBoEd8CnjhnCaokDNT3hUgUUXVmnXxIC4bEAUUEzo6IZOAoN3WKTkOobd/1Sf69bOpjzwWsUOExErcevqqUUcapJv0= hoangvu@dehvu12.local" ovgu12/linux
```
