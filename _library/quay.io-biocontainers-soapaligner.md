---
layout: container
name:  "quay.io/biocontainers/soapaligner"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/soapaligner/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/soapaligner/container.yaml"
updated_at: "2023-05-18 03:13:35.832068"
latest: "2.21--0"
container_url: "https://biocontainers.pro/tools/soapaligner"
aliases:
 - "2bwt-builder"
 - "soap"
versions:
 - "2.21--0"
description: "shpc-registry automated BioContainers addition for soapaligner"
config: {"url": "https://biocontainers.pro/tools/soapaligner", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for soapaligner", "latest": {"2.21--0": "sha256:122859073608baebdd363c7f2bdd2818615a77a6c384bf348807e70dd5e0421e"}, "tags": {"2.21--0": "sha256:122859073608baebdd363c7f2bdd2818615a77a6c384bf348807e70dd5e0421e"}, "docker": "quay.io/biocontainers/soapaligner", "aliases": {"2bwt-builder": "/usr/local/bin/2bwt-builder", "soap": "/usr/local/bin/soap"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/soapaligner.
shpc-registry automated BioContainers addition for soapaligner
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/soapaligner
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/soapaligner:2.21--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/soapaligner/2.21--0
$ module help quay.io/biocontainers/soapaligner/2.21--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### soapaligner-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### soapaligner-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### soapaligner-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### soapaligner-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### soapaligner-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### soapaligner-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 2bwt-builder

```bash
$ singularity exec <container> /usr/local/bin/2bwt-builder
$ podman run --it --rm --entrypoint /usr/local/bin/2bwt-builder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2bwt-builder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### soap

```bash
$ singularity exec <container> /usr/local/bin/soap
$ podman run --it --rm --entrypoint /usr/local/bin/soap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/soap   -v ${PWD} -w ${PWD} <container> -c " $@"
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