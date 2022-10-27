---
layout: container
name:  "quay.io/biocontainers/staphb_toolkit"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/staphb_toolkit/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/staphb_toolkit/container.yaml"
updated_at: "2022-10-27 00:58:16.316580"
latest: "2.0.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/staphb_toolkit"
aliases:
 - "pyfiglet"
 - "pysemver"
 - "spython"
 - "staphb-tk"
 - "wsdump"
versions:
 - "2.0.0--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for staphb_toolkit"
config: {"url": "https://biocontainers.pro/tools/staphb_toolkit", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for staphb_toolkit", "latest": {"2.0.0--pyhdfd78af_0": "sha256:6d3b3371b8b029af19b919e842efc036cd74bf809f8a84a9aa027d8d25805ed0"}, "tags": {"2.0.0--pyhdfd78af_0": "sha256:6d3b3371b8b029af19b919e842efc036cd74bf809f8a84a9aa027d8d25805ed0"}, "docker": "quay.io/biocontainers/staphb_toolkit", "aliases": {"pyfiglet": "/usr/local/bin/pyfiglet", "pysemver": "/usr/local/bin/pysemver", "spython": "/usr/local/bin/spython", "staphb-tk": "/usr/local/bin/staphb-tk", "wsdump": "/usr/local/bin/wsdump"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/staphb_toolkit.
shpc-registry automated BioContainers addition for staphb_toolkit
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/staphb_toolkit
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/staphb_toolkit:2.0.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/staphb_toolkit/2.0.0--pyhdfd78af_0
$ module help quay.io/biocontainers/staphb_toolkit/2.0.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### staphb_toolkit-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### staphb_toolkit-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### staphb_toolkit-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### staphb_toolkit-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### staphb_toolkit-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### staphb_toolkit-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pyfiglet

```bash
$ singularity exec <container> /usr/local/bin/pyfiglet
$ podman run --it --rm --entrypoint /usr/local/bin/pyfiglet   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyfiglet   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pysemver

```bash
$ singularity exec <container> /usr/local/bin/pysemver
$ podman run --it --rm --entrypoint /usr/local/bin/pysemver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pysemver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spython

```bash
$ singularity exec <container> /usr/local/bin/spython
$ podman run --it --rm --entrypoint /usr/local/bin/spython   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spython   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### staphb-tk

```bash
$ singularity exec <container> /usr/local/bin/staphb-tk
$ podman run --it --rm --entrypoint /usr/local/bin/staphb-tk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/staphb-tk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wsdump

```bash
$ singularity exec <container> /usr/local/bin/wsdump
$ podman run --it --rm --entrypoint /usr/local/bin/wsdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wsdump   -v ${PWD} -w ${PWD} <container> -c " $@"
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