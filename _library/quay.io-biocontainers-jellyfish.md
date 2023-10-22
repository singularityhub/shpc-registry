---
layout: container
name:  "quay.io/biocontainers/jellyfish"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/jellyfish/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/jellyfish/container.yaml"
updated_at: "2023-10-22 02:41:38.190682"
latest: "2.2.10--h6bb024c_1"
container_url: "https://biocontainers.pro/tools/jellyfish"
aliases:
 - "jellyfish"
versions:
 - "2.2.6--0"
 - "2.2.10--h6bb024c_1"
description: "shpc-registry automated BioContainers addition for jellyfish"
config: {"url": "https://biocontainers.pro/tools/jellyfish", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for jellyfish", "latest": {"2.2.10--h6bb024c_1": "sha256:2f55a16d4c96f366f9287e1d4fe6d10ae63974afee1e2e0627b90dab651c35f4"}, "tags": {"2.2.6--0": "sha256:2fa06e6c6afe001df9a96b14617c5faa4e43e3d6c5df094b21be3052c7496f2d", "2.2.10--h6bb024c_1": "sha256:2f55a16d4c96f366f9287e1d4fe6d10ae63974afee1e2e0627b90dab651c35f4"}, "docker": "quay.io/biocontainers/jellyfish", "aliases": {"jellyfish": "/usr/local/bin/jellyfish"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/jellyfish.
shpc-registry automated BioContainers addition for jellyfish
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/jellyfish
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/jellyfish:2.2.10--h6bb024c_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/jellyfish/2.2.10--h6bb024c_1
$ module help quay.io/biocontainers/jellyfish/2.2.10--h6bb024c_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### jellyfish-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### jellyfish-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### jellyfish-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### jellyfish-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### jellyfish-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### jellyfish-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### jellyfish

```bash
$ singularity exec <container> /usr/local/bin/jellyfish
$ podman run --it --rm --entrypoint /usr/local/bin/jellyfish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jellyfish   -v ${PWD} -w ${PWD} <container> -c " $@"
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