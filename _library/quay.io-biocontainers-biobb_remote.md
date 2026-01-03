---
layout: container
name:  "quay.io/biocontainers/biobb_remote"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/biobb_remote/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/biobb_remote/container.yaml"
updated_at: "2026-01-03 04:12:59.115122"
latest: "1.2.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/biobb_remote"
aliases:
 - "credentials"
 - "scp_service"
 - "slurm_test"
 - "ssh_command"
 - "2to3-3.7"
 - "idle3.7"
 - "pydoc3.7"
 - "python3.7"
 - "python3.7-config"
 - "python3.7m"
 - "python3.7m-config"
 - "pyvenv-3.7"
 - "pyvenv"
versions:
 - "1.2.2--pyhdfd78af_0"
description: "singularity registry hpc automated addition for biobb_remote"
config: {"url": "https://biocontainers.pro/tools/biobb_remote", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for biobb_remote", "latest": {"1.2.2--pyhdfd78af_0": "sha256:8da75d082f0f78e1976277b6eaa5a128e616e5137ee46dfc7275686adf28ef35"}, "tags": {"1.2.2--pyhdfd78af_0": "sha256:8da75d082f0f78e1976277b6eaa5a128e616e5137ee46dfc7275686adf28ef35"}, "docker": "quay.io/biocontainers/biobb_remote", "aliases": {"credentials": "/usr/local/bin/credentials", "scp_service": "/usr/local/bin/scp_service", "slurm_test": "/usr/local/bin/slurm_test", "ssh_command": "/usr/local/bin/ssh_command", "2to3-3.7": "/usr/local/bin/2to3-3.7", "idle3.7": "/usr/local/bin/idle3.7", "pydoc3.7": "/usr/local/bin/pydoc3.7", "python3.7": "/usr/local/bin/python3.7", "python3.7-config": "/usr/local/bin/python3.7-config", "python3.7m": "/usr/local/bin/python3.7m", "python3.7m-config": "/usr/local/bin/python3.7m-config", "pyvenv-3.7": "/usr/local/bin/pyvenv-3.7", "pyvenv": "/usr/local/bin/pyvenv"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/biobb_remote.
singularity registry hpc automated addition for biobb_remote
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/biobb_remote
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/biobb_remote:1.2.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/biobb_remote/1.2.2--pyhdfd78af_0
$ module help quay.io/biocontainers/biobb_remote/1.2.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### biobb_remote-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### biobb_remote-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### biobb_remote-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### biobb_remote-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### biobb_remote-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### biobb_remote-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### credentials

```bash
$ singularity exec <container> /usr/local/bin/credentials
$ podman run --it --rm --entrypoint /usr/local/bin/credentials   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/credentials   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scp_service

```bash
$ singularity exec <container> /usr/local/bin/scp_service
$ podman run --it --rm --entrypoint /usr/local/bin/scp_service   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scp_service   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### slurm_test

```bash
$ singularity exec <container> /usr/local/bin/slurm_test
$ podman run --it --rm --entrypoint /usr/local/bin/slurm_test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/slurm_test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ssh_command

```bash
$ singularity exec <container> /usr/local/bin/ssh_command
$ podman run --it --rm --entrypoint /usr/local/bin/ssh_command   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ssh_command   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.7

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.7

```bash
$ singularity exec <container> /usr/local/bin/idle3.7
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.7

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.7
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7

```bash
$ singularity exec <container> /usr/local/bin/python3.7
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7-config

```bash
$ singularity exec <container> /usr/local/bin/python3.7-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7m

```bash
$ singularity exec <container> /usr/local/bin/python3.7m
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7m   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7m-config

```bash
$ singularity exec <container> /usr/local/bin/python3.7m-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv-3.7

```bash
$ singularity exec <container> /usr/local/bin/pyvenv-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv

```bash
$ singularity exec <container> /usr/local/bin/pyvenv
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv   -v ${PWD} -w ${PWD} <container> -c " $@"
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