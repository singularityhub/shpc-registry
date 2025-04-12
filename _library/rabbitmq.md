---
layout: container
name:  "rabbitmq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/rabbitmq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/rabbitmq/container.yaml"
updated_at: "2025-04-12 02:59:45.561723"
latest: "4.1-rc"
container_url: "https://hub.docker.com/r/_/rabbitmq"
aliases:
 - "rabbitmq-defaults"
 - "rabbitmq-diagnostics"
 - "rabbitmq-env"
 - "rabbitmq-plugins"
 - "rabbitmq-queues"
 - "rabbitmq-server"
 - "rabbitmq-upgrade"
 - "rabbitmqctl"
versions:
 - "3.8.15-rc.2-alpine"
 - "3.8.16-alpine"
 - "3.8.17-alpine"
 - "3.8.17-rc.1-alpine"
 - "3.8.18-beta.1-alpine"
 - "3.9.0-beta.2-alpine"
 - "3.9.5"
 - "3.9.8"
 - "3.9.10"
 - "3.9.11"
 - "3.9.13"
 - "latest"
 - "3"
 - "3.10-rc"
 - "3.9"
 - "3.8"
 - "3.10"
 - "3.11"
 - "3.12-rc"
 - "3.12"
 - "3.13-rc"
 - "3.13"
 - "4.0-rc"
 - "4"
 - "4.0"
 - "4.1-rc"
description: "RabbitMQ is an open source multi-protocol messaging broker."
config: {"docker": "rabbitmq", "url": "https://hub.docker.com/r/_/rabbitmq", "maintainer": "@vsoch", "description": "RabbitMQ is an open source multi-protocol messaging broker.", "latest": {"4.1-rc": "sha256:ce50907ff07df656bf109f37122705d18ae4ec9cb0567ad671234b08b9b615de"}, "tags": {"3.8.15-rc.2-alpine": "sha256:56682567544860464b89625edbd28b524ca12aa5cae4e76ee9e5b887a2db7a06", "3.8.16-alpine": "sha256:87f7fde78fb62b1aa145efe7d81c0b450f8c13e608ee322794c872956380f90e", "3.8.17-alpine": "sha256:3033061a6e7e48897fb79d6922e282d92c8ced016721aaadee9a67cb25c9b03c", "3.8.17-rc.1-alpine": "sha256:a33f53d57c9c35999aa352b67c4e53ce956d147c38d50a809ed19da7783358ac", "3.8.18-beta.1-alpine": "sha256:341d8787808c860599bf6a87e482ccc9efbd69aa3a246554d924a693ad64d9ff", "3.9.0-beta.2-alpine": "sha256:b1a3a20958ddbbd2ad7c169c8d40c7a2d0d6a23d53380ff2b9aee876e14f8630", "3.9.5": "sha256:3b3f7b55be78e1b3c7330671ffc3f5e3670f66f040a4a429109a7f56c90464dc", "3.9.8": "sha256:19e69a7a65fa6b1d0a5c658bad8ec03d2c9900a98ebbc744c34d49179ff517bf", "3.9.10": "sha256:0d862496f77a3bd377eb5de437411a4388885f0f0c2452291e97a85bc89df87a", "3.9.11": "sha256:884146137011519524d506a12687127f3d2c7c37c2cc11206dc72c59bedea5e2", "3.9.13": "sha256:f5c8c7fd99e4c88527276df319556fdcb56e4d289614c5fefda5ee8d17c5ea89", "latest": "sha256:7b7728ef12151bcb06a1f28cc60caeba1e2c621547d25e79b8f86c4d8777a9cf", "3": "sha256:4c11b9cf2a66d42414be74516018d1118bd7606ce48865652d4ed137cc9eab7f", "3.10-rc": "sha256:8bc95a99b637276b8cebda5c4d8bf0cbac8ea5cc0ac9410f71c1d570e799c9c6", "3.9": "sha256:ff02642ec7b0d1e23a2cf4172c2c1d4a82f39e7b79762414f0c1ac41618b8458", "3.8": "sha256:5e859a09297ff0532312d5a95d4cf87b524991b265df0b7e3111be0db1391360", "3.10": "sha256:0c60abebb44a80791cc03cd2204f0871879ffeeaf903e0f53543053fe3461361", "3.11": "sha256:d3a929ba16d0da7f3e495949139f73ee1c79ad4f87821ce8b43514f2c376d4fd", "3.12-rc": "sha256:370cda42768ccc1139d70a66666391ac2b37f96315d01b98de127ca44f7e4c9c", "3.12": "sha256:4dc5d5a5076f7c458b7f3468e2282f329a8911cc3c31c4ed4aefcedb27917da2", "3.13-rc": "sha256:779df7e2ba678d97cf33032c77e29baac9fb7dd2f5df930b768170870ca8fd9d", "3.13": "sha256:4c11b9cf2a66d42414be74516018d1118bd7606ce48865652d4ed137cc9eab7f", "4.0-rc": "sha256:965acfc6c377d25368228289f083ac6f65c672037eb819345d6e191f8af30e42", "4": "sha256:7b7728ef12151bcb06a1f28cc60caeba1e2c621547d25e79b8f86c4d8777a9cf", "4.0": "sha256:7b7728ef12151bcb06a1f28cc60caeba1e2c621547d25e79b8f86c4d8777a9cf", "4.1-rc": "sha256:ce50907ff07df656bf109f37122705d18ae4ec9cb0567ad671234b08b9b615de"}, "aliases": {"rabbitmq-defaults": "/opt/rabbitmq/sbin/rabbitmq-defaults", "rabbitmq-diagnostics": "/opt/rabbitmq/sbin/rabbitmq-diagnostics", "rabbitmq-env": "/opt/rabbitmq/sbin/rabbitmq-env", "rabbitmq-plugins": "/opt/rabbitmq/sbin/rabbitmq-plugins", "rabbitmq-queues": "/opt/rabbitmq/sbin/rabbitmq-queues", "rabbitmq-server": "/opt/rabbitmq/sbin/rabbitmq-server", "rabbitmq-upgrade": "/opt/rabbitmq/sbin/rabbitmq-upgrade", "rabbitmqctl": "/opt/rabbitmq/sbin/rabbitmqctl"}}
---

This module is a singularity container wrapper for rabbitmq.
RabbitMQ is an open source multi-protocol messaging broker.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install rabbitmq
```

Or a specific version:

```bash
$ shpc install rabbitmq:4.1-rc
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load rabbitmq/4.1-rc
$ module help rabbitmq/4.1-rc
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rabbitmq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rabbitmq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rabbitmq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rabbitmq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rabbitmq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rabbitmq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### rabbitmq-defaults

```bash
$ singularity exec <container> /opt/rabbitmq/sbin/rabbitmq-defaults
$ podman run --it --rm --entrypoint /opt/rabbitmq/sbin/rabbitmq-defaults   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/rabbitmq/sbin/rabbitmq-defaults   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rabbitmq-diagnostics

```bash
$ singularity exec <container> /opt/rabbitmq/sbin/rabbitmq-diagnostics
$ podman run --it --rm --entrypoint /opt/rabbitmq/sbin/rabbitmq-diagnostics   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/rabbitmq/sbin/rabbitmq-diagnostics   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rabbitmq-env

```bash
$ singularity exec <container> /opt/rabbitmq/sbin/rabbitmq-env
$ podman run --it --rm --entrypoint /opt/rabbitmq/sbin/rabbitmq-env   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/rabbitmq/sbin/rabbitmq-env   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rabbitmq-plugins

```bash
$ singularity exec <container> /opt/rabbitmq/sbin/rabbitmq-plugins
$ podman run --it --rm --entrypoint /opt/rabbitmq/sbin/rabbitmq-plugins   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/rabbitmq/sbin/rabbitmq-plugins   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rabbitmq-queues

```bash
$ singularity exec <container> /opt/rabbitmq/sbin/rabbitmq-queues
$ podman run --it --rm --entrypoint /opt/rabbitmq/sbin/rabbitmq-queues   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/rabbitmq/sbin/rabbitmq-queues   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rabbitmq-server

```bash
$ singularity exec <container> /opt/rabbitmq/sbin/rabbitmq-server
$ podman run --it --rm --entrypoint /opt/rabbitmq/sbin/rabbitmq-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/rabbitmq/sbin/rabbitmq-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rabbitmq-upgrade

```bash
$ singularity exec <container> /opt/rabbitmq/sbin/rabbitmq-upgrade
$ podman run --it --rm --entrypoint /opt/rabbitmq/sbin/rabbitmq-upgrade   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/rabbitmq/sbin/rabbitmq-upgrade   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rabbitmqctl

```bash
$ singularity exec <container> /opt/rabbitmq/sbin/rabbitmqctl
$ podman run --it --rm --entrypoint /opt/rabbitmq/sbin/rabbitmqctl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/rabbitmq/sbin/rabbitmqctl   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>

### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)