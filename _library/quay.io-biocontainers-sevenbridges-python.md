---
layout: container
name:  "quay.io/biocontainers/sevenbridges-python"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sevenbridges-python/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sevenbridges-python/container.yaml"
updated_at: "2025-02-21 03:33:39.228030"
latest: "2.11.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/sevenbridges-python"
aliases:
 - "chardetect"
 - "python2-config"
 - "python2.7-config"
 - "python2"
 - "python2.7"
 - "idle"
 - "python-config"
 - "smtpd.py"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "0.7.2--py27_1"
 - "0.20.3--py27_0"
 - "0.18.2--py36_1"
 - "0.17.7--py27_0"
 - "0.16.0--py36_0"
 - "0.15.2--py27_0"
 - "2.11.0--pyhdfd78af_0"
 - "2.10.3--pyhdfd78af_0"
 - "2.9.2--pyhdfd78af_0"
 - "2.8.1--pyhdfd78af_0"
 - "2.7.0--pyhdfd78af_0"
 - "2.11.1--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for sevenbridges-python"
config: {"url": "https://biocontainers.pro/tools/sevenbridges-python", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sevenbridges-python", "latest": {"2.11.1--pyhdfd78af_0": "sha256:4f00121801504a2f91f642f162764e35e97137bca2f2912d3fc4e0290add7c03"}, "tags": {"0.7.2--py27_1": "sha256:0e8fdef0018806ce28c6b3f491c0486c453073b6af8fd3cae5eed8dca7ee998b", "0.20.3--py27_0": "sha256:e65f1f6ce462592ea2b007d39044ddfe97396721892529fb49586ad76ac0d570", "0.18.2--py36_1": "sha256:cf0662bec6a952d910cbc96cc7efe2b1d09fcc53685e0f836b5dd24c6be503f3", "0.17.7--py27_0": "sha256:67c3ef35df6972359744d7fada6a6b1d2723c5a3c7b7095d78a260c261df2aa6", "0.16.0--py36_0": "sha256:770fc1f46edaebc006e622ed93b559c800b4d5ddbb06ee675d986cdcfee3ada1", "0.15.2--py27_0": "sha256:701efc2077118722ba70700d4c834b7b0a020b7a94822c94b74feb9fb66fa1fe", "2.11.0--pyhdfd78af_0": "sha256:3ac0d943f1d03054aa785b7b6777c6983b11454c8389e869b0adb2c833b62800", "2.10.3--pyhdfd78af_0": "sha256:e34b779a4c257c161249206202bca7ae4ba37a3960779cb443baf7df1af23246", "2.9.2--pyhdfd78af_0": "sha256:b62dda9ad87b2093e8af2d048533e302311314ae3df91dcd1cebec5d18834b57", "2.8.1--pyhdfd78af_0": "sha256:63e71091e20e8e1c176dae318376397c441f9e3cd041ce92dbd6ae067b4c3b96", "2.7.0--pyhdfd78af_0": "sha256:6b30ee4a278035d1433b58edfaebd7784b26bf01b0088a66d3c151ef48410674", "2.11.1--pyhdfd78af_0": "sha256:4f00121801504a2f91f642f162764e35e97137bca2f2912d3fc4e0290add7c03"}, "docker": "quay.io/biocontainers/sevenbridges-python", "aliases": {"chardetect": "/usr/local/bin/chardetect", "python2-config": "/usr/local/bin/python2-config", "python2.7-config": "/usr/local/bin/python2.7-config", "python2": "/usr/local/bin/python2", "python2.7": "/usr/local/bin/python2.7", "idle": "/usr/local/bin/idle", "python-config": "/usr/local/bin/python-config", "smtpd.py": "/usr/local/bin/smtpd.py", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sevenbridges-python.
shpc-registry automated BioContainers addition for sevenbridges-python
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sevenbridges-python
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sevenbridges-python:2.11.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sevenbridges-python/2.11.1--pyhdfd78af_0
$ module help quay.io/biocontainers/sevenbridges-python/2.11.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sevenbridges-python-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sevenbridges-python-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sevenbridges-python-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sevenbridges-python-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sevenbridges-python-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sevenbridges-python-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### chardetect

```bash
$ singularity exec <container> /usr/local/bin/chardetect
$ podman run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### ncurses5-config

```bash
$ singularity exec <container> /usr/local/bin/ncurses5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncursesw5-config

```bash
$ singularity exec <container> /usr/local/bin/ncursesw5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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