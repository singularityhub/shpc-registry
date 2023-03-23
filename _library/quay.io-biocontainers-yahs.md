---
layout: container
name:  "quay.io/biocontainers/yahs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/yahs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/yahs/container.yaml"
updated_at: "2023-03-23 02:46:10.882979"
latest: "1.2a.2--h7132678_0"
container_url: "https://biocontainers.pro/tools/yahs"
aliases:
 - "agp_to_fasta"
 - "juicer"
 - "yahs"
versions:
 - "1.2a.2--h7132678_0"
description: "shpc-registry automated BioContainers addition for yahs"
config: {"url": "https://biocontainers.pro/tools/yahs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for yahs", "latest": {"1.2a.2--h7132678_0": "sha256:c946489c2a3b5f18f55f8a48059f544db6aed5f94fdde4f712f21210be861f98"}, "tags": {"1.2a.2--h7132678_0": "sha256:c946489c2a3b5f18f55f8a48059f544db6aed5f94fdde4f712f21210be861f98"}, "docker": "quay.io/biocontainers/yahs", "aliases": {"agp_to_fasta": "/usr/local/bin/agp_to_fasta", "juicer": "/usr/local/bin/juicer", "yahs": "/usr/local/bin/yahs"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/yahs.
shpc-registry automated BioContainers addition for yahs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/yahs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/yahs:1.2a.2--h7132678_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/yahs/1.2a.2--h7132678_0
$ module help quay.io/biocontainers/yahs/1.2a.2--h7132678_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### yahs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### yahs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### yahs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### yahs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### yahs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### yahs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### agp_to_fasta

```bash
$ singularity exec <container> /usr/local/bin/agp_to_fasta
$ podman run --it --rm --entrypoint /usr/local/bin/agp_to_fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/agp_to_fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### juicer

```bash
$ singularity exec <container> /usr/local/bin/juicer
$ podman run --it --rm --entrypoint /usr/local/bin/juicer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/juicer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### yahs

```bash
$ singularity exec <container> /usr/local/bin/yahs
$ podman run --it --rm --entrypoint /usr/local/bin/yahs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yahs   -v ${PWD} -w ${PWD} <container> -c " $@"
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