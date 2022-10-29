---
layout: container
name:  "quay.io/biocontainers/biobb_adapters"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/biobb_adapters/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/biobb_adapters/container.yaml"
updated_at: "2022-10-29 05:32:34.556623"
latest: "3.7.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/biobb_adapters"
aliases:
 - "black-primer"
 - "2to3-3.8"
 - "activate-global-python-argcomplete"
 - "acyclic"
 - "annotate"
 - "aserver"
 - "assistant"
 - "bagit.py"
 - "bcomps"
 - "bdftogd"
 - "black"
versions:
 - "3.7.0--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for biobb_adapters"
config: {"url": "https://biocontainers.pro/tools/biobb_adapters", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for biobb_adapters", "latest": {"3.7.0--pyhdfd78af_0": "sha256:4d8ee7daa23a452321524f2ad7c6f3cadc41bc490670a6d02bfdf03afb990c85"}, "tags": {"3.7.0--pyhdfd78af_0": "sha256:4d8ee7daa23a452321524f2ad7c6f3cadc41bc490670a6d02bfdf03afb990c85"}, "docker": "quay.io/biocontainers/biobb_adapters", "aliases": {"black-primer": "/usr/local/bin/black-primer", "2to3-3.8": "/usr/local/bin/2to3-3.8", "activate-global-python-argcomplete": "/usr/local/bin/activate-global-python-argcomplete", "acyclic": "/usr/local/bin/acyclic", "annotate": "/usr/local/bin/annotate", "aserver": "/usr/local/bin/aserver", "assistant": "/usr/local/bin/assistant", "bagit.py": "/usr/local/bin/bagit.py", "bcomps": "/usr/local/bin/bcomps", "bdftogd": "/usr/local/bin/bdftogd", "black": "/usr/local/bin/black"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/biobb_adapters.
shpc-registry automated BioContainers addition for biobb_adapters
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/biobb_adapters
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/biobb_adapters:3.7.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/biobb_adapters/3.7.0--pyhdfd78af_0
$ module help quay.io/biocontainers/biobb_adapters/3.7.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### biobb_adapters-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### biobb_adapters-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### biobb_adapters-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### biobb_adapters-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### biobb_adapters-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### biobb_adapters-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### black-primer

```bash
$ singularity exec <container> /usr/local/bin/black-primer
$ podman run --it --rm --entrypoint /usr/local/bin/black-primer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/black-primer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.8

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.8
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### activate-global-python-argcomplete

```bash
$ singularity exec <container> /usr/local/bin/activate-global-python-argcomplete
$ podman run --it --rm --entrypoint /usr/local/bin/activate-global-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/activate-global-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### acyclic

```bash
$ singularity exec <container> /usr/local/bin/acyclic
$ podman run --it --rm --entrypoint /usr/local/bin/acyclic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/acyclic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotate

```bash
$ singularity exec <container> /usr/local/bin/annotate
$ podman run --it --rm --entrypoint /usr/local/bin/annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aserver

```bash
$ singularity exec <container> /usr/local/bin/aserver
$ podman run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### assistant

```bash
$ singularity exec <container> /usr/local/bin/assistant
$ podman run --it --rm --entrypoint /usr/local/bin/assistant   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/assistant   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bagit.py

```bash
$ singularity exec <container> /usr/local/bin/bagit.py
$ podman run --it --rm --entrypoint /usr/local/bin/bagit.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bagit.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bcomps

```bash
$ singularity exec <container> /usr/local/bin/bcomps
$ podman run --it --rm --entrypoint /usr/local/bin/bcomps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bcomps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bdftogd

```bash
$ singularity exec <container> /usr/local/bin/bdftogd
$ podman run --it --rm --entrypoint /usr/local/bin/bdftogd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bdftogd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### black

```bash
$ singularity exec <container> /usr/local/bin/black
$ podman run --it --rm --entrypoint /usr/local/bin/black   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/black   -v ${PWD} -w ${PWD} <container> -c " $@"
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