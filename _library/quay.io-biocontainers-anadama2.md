---
layout: container
name:  "quay.io/biocontainers/anadama2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/anadama2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/anadama2/container.yaml"
updated_at: "2024-11-25 04:08:18.084351"
latest: "0.10.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/anadama2"
aliases:
 - "anadama2_aws_batch_task"
 - "ptangle"
 - "pweave"
 - "pweave-convert"
 - "pypublish"
 - "jupyter-nbconvert"
 - "jupyter-kernel"
 - "jupyter-kernelspec"
 - "jupyter-run"
 - "iptest3"
 - "curve_keygen"
 - "iptest"
 - "ipython3"
 - "ipython"
 - "jupyter-trust"
versions:
 - "0.8.0--pyhdfd78af_0"
 - "0.10.0--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for anadama2"
config: {"url": "https://biocontainers.pro/tools/anadama2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for anadama2", "latest": {"0.10.0--pyhdfd78af_0": "sha256:9347cfbb4ad18c32d157e6b296e7dbc18a55e9404f6f702911cbe82b9f4936e3"}, "tags": {"0.8.0--pyhdfd78af_0": "sha256:eb63964c5eda4d732e554f5aca4374f2f77e71e51dfc8311873a1f568e80cba4", "0.10.0--pyhdfd78af_0": "sha256:9347cfbb4ad18c32d157e6b296e7dbc18a55e9404f6f702911cbe82b9f4936e3"}, "docker": "quay.io/biocontainers/anadama2", "aliases": {"anadama2_aws_batch_task": "/usr/local/bin/anadama2_aws_batch_task", "ptangle": "/usr/local/bin/ptangle", "pweave": "/usr/local/bin/pweave", "pweave-convert": "/usr/local/bin/pweave-convert", "pypublish": "/usr/local/bin/pypublish", "jupyter-nbconvert": "/usr/local/bin/jupyter-nbconvert", "jupyter-kernel": "/usr/local/bin/jupyter-kernel", "jupyter-kernelspec": "/usr/local/bin/jupyter-kernelspec", "jupyter-run": "/usr/local/bin/jupyter-run", "iptest3": "/usr/local/bin/iptest3", "curve_keygen": "/usr/local/bin/curve_keygen", "iptest": "/usr/local/bin/iptest", "ipython3": "/usr/local/bin/ipython3", "ipython": "/usr/local/bin/ipython", "jupyter-trust": "/usr/local/bin/jupyter-trust"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/anadama2.
shpc-registry automated BioContainers addition for anadama2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/anadama2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/anadama2:0.10.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/anadama2/0.10.0--pyhdfd78af_0
$ module help quay.io/biocontainers/anadama2/0.10.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### anadama2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### anadama2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### anadama2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### anadama2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### anadama2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### anadama2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### anadama2_aws_batch_task

```bash
$ singularity exec <container> /usr/local/bin/anadama2_aws_batch_task
$ podman run --it --rm --entrypoint /usr/local/bin/anadama2_aws_batch_task   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/anadama2_aws_batch_task   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ptangle

```bash
$ singularity exec <container> /usr/local/bin/ptangle
$ podman run --it --rm --entrypoint /usr/local/bin/ptangle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ptangle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pweave

```bash
$ singularity exec <container> /usr/local/bin/pweave
$ podman run --it --rm --entrypoint /usr/local/bin/pweave   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pweave   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pweave-convert

```bash
$ singularity exec <container> /usr/local/bin/pweave-convert
$ podman run --it --rm --entrypoint /usr/local/bin/pweave-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pweave-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pypublish

```bash
$ singularity exec <container> /usr/local/bin/pypublish
$ podman run --it --rm --entrypoint /usr/local/bin/pypublish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pypublish   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-nbconvert

```bash
$ singularity exec <container> /usr/local/bin/jupyter-nbconvert
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-nbconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-nbconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-kernel

```bash
$ singularity exec <container> /usr/local/bin/jupyter-kernel
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-kernel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-kernel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-kernelspec

```bash
$ singularity exec <container> /usr/local/bin/jupyter-kernelspec
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-kernelspec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-kernelspec   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-run

```bash
$ singularity exec <container> /usr/local/bin/jupyter-run
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-run   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-run   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iptest3

```bash
$ singularity exec <container> /usr/local/bin/iptest3
$ podman run --it --rm --entrypoint /usr/local/bin/iptest3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iptest3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### curve_keygen

```bash
$ singularity exec <container> /usr/local/bin/curve_keygen
$ podman run --it --rm --entrypoint /usr/local/bin/curve_keygen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/curve_keygen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iptest

```bash
$ singularity exec <container> /usr/local/bin/iptest
$ podman run --it --rm --entrypoint /usr/local/bin/iptest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iptest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipython3

```bash
$ singularity exec <container> /usr/local/bin/ipython3
$ podman run --it --rm --entrypoint /usr/local/bin/ipython3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipython3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipython

```bash
$ singularity exec <container> /usr/local/bin/ipython
$ podman run --it --rm --entrypoint /usr/local/bin/ipython   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipython   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-trust

```bash
$ singularity exec <container> /usr/local/bin/jupyter-trust
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-trust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-trust   -v ${PWD} -w ${PWD} <container> -c " $@"
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