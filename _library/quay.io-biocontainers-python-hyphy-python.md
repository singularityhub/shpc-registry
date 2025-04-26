---
layout: container
name:  "quay.io/biocontainers/python-hyphy-python"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/python-hyphy-python/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/python-hyphy-python/container.yaml"
updated_at: "2025-04-26 03:18:51.589345"
latest: "0.1.12--py312h351e35f_3"
container_url: "https://biocontainers.pro/tools/python-hyphy-python"
aliases:
 - "python2-config"
 - "python2.7-config"
 - "python2"
 - "python2.7"
 - "idle"
 - "python-config"
 - "smtpd.py"
versions:
 - "0.1.9--py27hfae33f2_4"
 - "0.1.10--py38hb572783_2"
 - "0.1.10--py38hbcae7b6_5"
 - "0.1.11--py38hb572783_0"
 - "0.1.11--py39ha6f86ea_1"
 - "0.1.12--py310h3a3b00a_1"
 - "0.1.12--py311h76ae45d_2"
 - "0.1.12--py312h351e35f_3"
description: "shpc-registry automated BioContainers addition for python-hyphy-python"
config: {"url": "https://biocontainers.pro/tools/python-hyphy-python", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for python-hyphy-python", "latest": {"0.1.12--py312h351e35f_3": "sha256:43a6e26fd78eeef03ec0d4d945b7792896152254088e1c74c5e49eda4c2b4ea7"}, "tags": {"0.1.9--py27hfae33f2_4": "sha256:134aa20159e65218ca6b46c3d4fd31fd7ba9f1530f16201dd10c485da72b95b2", "0.1.10--py38hb572783_2": "sha256:f84e1e078d0941aeab7ef51cd2a61f59489273f89f7c0a4e034cca76ddd95236", "0.1.10--py38hbcae7b6_5": "sha256:3f09b08506010937b8e69d6174a89dabffa37bc2c322dc8de560225113d2ad88", "0.1.11--py38hb572783_0": "sha256:c69bfbb78a5833dc2992fa1b25b581d99ac4bfaf183e71797917a8b99b9f110b", "0.1.11--py39ha6f86ea_1": "sha256:5eff42fbab8c5241a21e1576d349d3358beac8651aefc96afdcad0dbc4b346ea", "0.1.12--py310h3a3b00a_1": "sha256:148f3c9924a198d682ddc1b93c4e422b2f25de0f3f45c073f0cf4950545da686", "0.1.12--py311h76ae45d_2": "sha256:745426c75009c09aa3bb2cfd0093157129d2023fa4bca84247ff64aec88dbca6", "0.1.12--py312h351e35f_3": "sha256:43a6e26fd78eeef03ec0d4d945b7792896152254088e1c74c5e49eda4c2b4ea7"}, "docker": "quay.io/biocontainers/python-hyphy-python", "aliases": {"python2-config": "/usr/local/bin/python2-config", "python2.7-config": "/usr/local/bin/python2.7-config", "python2": "/usr/local/bin/python2", "python2.7": "/usr/local/bin/python2.7", "idle": "/usr/local/bin/idle", "python-config": "/usr/local/bin/python-config", "smtpd.py": "/usr/local/bin/smtpd.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/python-hyphy-python.
shpc-registry automated BioContainers addition for python-hyphy-python
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/python-hyphy-python
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/python-hyphy-python:0.1.12--py312h351e35f_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/python-hyphy-python/0.1.12--py312h351e35f_3
$ module help quay.io/biocontainers/python-hyphy-python/0.1.12--py312h351e35f_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### python-hyphy-python-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### python-hyphy-python-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### python-hyphy-python-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### python-hyphy-python-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### python-hyphy-python-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### python-hyphy-python-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### python2-config

```bash
$ singularity exec <container> /usr/local/bin/python2-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.7-config

```bash
$ singularity exec <container> /usr/local/bin/python2.7-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2

```bash
$ singularity exec <container> /usr/local/bin/python2
$ podman run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.7

```bash
$ singularity exec <container> /usr/local/bin/python2.7
$ podman run --it --rm --entrypoint /usr/local/bin/python2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle

```bash
$ singularity exec <container> /usr/local/bin/idle
$ podman run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python-config

```bash
$ singularity exec <container> /usr/local/bin/python-config
$ podman run --it --rm --entrypoint /usr/local/bin/python-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### smtpd.py

```bash
$ singularity exec <container> /usr/local/bin/smtpd.py
$ podman run --it --rm --entrypoint /usr/local/bin/smtpd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smtpd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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