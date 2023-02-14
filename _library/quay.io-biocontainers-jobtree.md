---
layout: container
name:  "quay.io/biocontainers/jobtree"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/jobtree/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/jobtree/container.yaml"
updated_at: "2023-02-14 03:26:24.296497"
latest: "09.04.2017--py_2"
container_url: "https://biocontainers.pro/tools/jobtree"
aliases:
 - "jobTreeKill"
 - "jobTreeRestarts"
 - "jobTreeStats"
 - "jobTreeStatus"
 - "multijob"
 - "python2-config"
 - "python2.7-config"
 - "python2"
 - "python2.7"
 - "idle"
 - "python-config"
 - "smtpd.py"
versions:
 - "3.0.3--py_1"
 - "09.04.2017--py_2"
description: "shpc-registry automated BioContainers addition for jobtree"
config: {"url": "https://biocontainers.pro/tools/jobtree", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for jobtree", "latest": {"09.04.2017--py_2": "sha256:677e9b91813920c5f4800a71a66a883df62fd991994f3a0ea6b37631a0cb8ab8"}, "tags": {"3.0.3--py_1": "sha256:24f864da7a79fc9c78e1ef134623878e05452242ae81ff8813fb8d683790e6b2", "09.04.2017--py_2": "sha256:677e9b91813920c5f4800a71a66a883df62fd991994f3a0ea6b37631a0cb8ab8"}, "docker": "quay.io/biocontainers/jobtree", "aliases": {"jobTreeKill": "/usr/local/bin/jobTreeKill", "jobTreeRestarts": "/usr/local/bin/jobTreeRestarts", "jobTreeStats": "/usr/local/bin/jobTreeStats", "jobTreeStatus": "/usr/local/bin/jobTreeStatus", "multijob": "/usr/local/bin/multijob", "python2-config": "/usr/local/bin/python2-config", "python2.7-config": "/usr/local/bin/python2.7-config", "python2": "/usr/local/bin/python2", "python2.7": "/usr/local/bin/python2.7", "idle": "/usr/local/bin/idle", "python-config": "/usr/local/bin/python-config", "smtpd.py": "/usr/local/bin/smtpd.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/jobtree.
shpc-registry automated BioContainers addition for jobtree
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/jobtree
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/jobtree:09.04.2017--py_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/jobtree/09.04.2017--py_2
$ module help quay.io/biocontainers/jobtree/09.04.2017--py_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### jobtree-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### jobtree-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### jobtree-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### jobtree-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### jobtree-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### jobtree-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### jobTreeKill

```bash
$ singularity exec <container> /usr/local/bin/jobTreeKill
$ podman run --it --rm --entrypoint /usr/local/bin/jobTreeKill   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jobTreeKill   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jobTreeRestarts

```bash
$ singularity exec <container> /usr/local/bin/jobTreeRestarts
$ podman run --it --rm --entrypoint /usr/local/bin/jobTreeRestarts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jobTreeRestarts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jobTreeStats

```bash
$ singularity exec <container> /usr/local/bin/jobTreeStats
$ podman run --it --rm --entrypoint /usr/local/bin/jobTreeStats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jobTreeStats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jobTreeStatus

```bash
$ singularity exec <container> /usr/local/bin/jobTreeStatus
$ podman run --it --rm --entrypoint /usr/local/bin/jobTreeStatus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jobTreeStatus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### multijob

```bash
$ singularity exec <container> /usr/local/bin/multijob
$ podman run --it --rm --entrypoint /usr/local/bin/multijob   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/multijob   -v ${PWD} -w ${PWD} <container> -c " $@"
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