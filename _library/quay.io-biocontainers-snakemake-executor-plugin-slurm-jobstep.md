---
layout: container
name:  "quay.io/biocontainers/snakemake-executor-plugin-slurm-jobstep"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/snakemake-executor-plugin-slurm-jobstep/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/snakemake-executor-plugin-slurm-jobstep/container.yaml"
updated_at: "2026-01-28 04:21:27.365659"
latest: "0.3.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/snakemake-executor-plugin-slurm-jobstep"
aliases:
 - "2to3-3.12"
 - "idle3.12"
 - "pydoc3.12"
 - "python3.12"
 - "python3.12-config"
versions:
 - "0.1.8--pyhdfd78af_0"
 - "0.1.10--pyhdfd78af_0"
 - "0.1.11--pyhdfd78af_0"
 - "0.2.1--pyhdfd78af_0"
 - "0.3.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for snakemake-executor-plugin-slurm-jobstep"
config: {"url": "https://biocontainers.pro/tools/snakemake-executor-plugin-slurm-jobstep", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for snakemake-executor-plugin-slurm-jobstep", "latest": {"0.3.0--pyhdfd78af_0": "sha256:ff511c1ef28771bf70cc6c8c8917eff53ab7f8acceecae3314e9db1404381322"}, "tags": {"0.1.8--pyhdfd78af_0": "sha256:877fba61de3da80da06b7c51859b437d96a3dccf6cdc3b0dbaf839bde3fe1724", "0.1.10--pyhdfd78af_0": "sha256:6f6dc5bd6bd2d3670a24cbe539aced0a41843c28c51e8bce714c1ef406502764", "0.1.11--pyhdfd78af_0": "sha256:46a3ee753d34bb1aac3c068289b53cb84294a81916607054731baf1dd8fd0b8e", "0.2.1--pyhdfd78af_0": "sha256:7ee6cab7680ecd5c4759ba1ecfa8372c5296c6d49a2323a385778b86fb283b84", "0.3.0--pyhdfd78af_0": "sha256:ff511c1ef28771bf70cc6c8c8917eff53ab7f8acceecae3314e9db1404381322"}, "docker": "quay.io/biocontainers/snakemake-executor-plugin-slurm-jobstep", "aliases": {"2to3-3.12": "/usr/local/bin/2to3-3.12", "idle3.12": "/usr/local/bin/idle3.12", "pydoc3.12": "/usr/local/bin/pydoc3.12", "python3.12": "/usr/local/bin/python3.12", "python3.12-config": "/usr/local/bin/python3.12-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/snakemake-executor-plugin-slurm-jobstep.
singularity registry hpc automated addition for snakemake-executor-plugin-slurm-jobstep
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/snakemake-executor-plugin-slurm-jobstep
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/snakemake-executor-plugin-slurm-jobstep:0.3.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/snakemake-executor-plugin-slurm-jobstep/0.3.0--pyhdfd78af_0
$ module help quay.io/biocontainers/snakemake-executor-plugin-slurm-jobstep/0.3.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### snakemake-executor-plugin-slurm-jobstep-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### snakemake-executor-plugin-slurm-jobstep-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### snakemake-executor-plugin-slurm-jobstep-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### snakemake-executor-plugin-slurm-jobstep-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### snakemake-executor-plugin-slurm-jobstep-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### snakemake-executor-plugin-slurm-jobstep-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 2to3-3.12

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.12
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.12

```bash
$ singularity exec <container> /usr/local/bin/idle3.12
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.12

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.12
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12

```bash
$ singularity exec <container> /usr/local/bin/python3.12
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12-config

```bash
$ singularity exec <container> /usr/local/bin/python3.12-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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