---
layout: container
name:  "quay.io/biocontainers/ancestry_hmm-s"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ancestry_hmm-s/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ancestry_hmm-s/container.yaml"
updated_at: "2024-11-21 03:06:23.368280"
latest: "0.9.0.2--h4ac6f70_5"
container_url: "https://biocontainers.pro/tools/ancestry_hmm-s"
aliases:
 - "ahmm-s"
versions:
 - "0.9.0.2--h9f5acd7_2"
 - "0.9.0.2--h4ac6f70_4"
 - "0.9.0.2--h4ac6f70_5"
description: "shpc-registry automated BioContainers addition for ancestry_hmm-s"
config: {"url": "https://biocontainers.pro/tools/ancestry_hmm-s", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ancestry_hmm-s", "latest": {"0.9.0.2--h4ac6f70_5": "sha256:42287b7e0aa78a58f612ec980f5b145f1e291ae2a5cfe9cd39c9ca0497c23704"}, "tags": {"0.9.0.2--h9f5acd7_2": "sha256:45389bb27d51b1db2b38ebc2f39cc8cc0f40b6e3c0e40aeace2b199fa0ef4d18", "0.9.0.2--h4ac6f70_4": "sha256:80b8b5a56b3a3400d1c53df8b517d8a56fbe1f1f41f0c2e4ffe82d38ca41a879", "0.9.0.2--h4ac6f70_5": "sha256:42287b7e0aa78a58f612ec980f5b145f1e291ae2a5cfe9cd39c9ca0497c23704"}, "docker": "quay.io/biocontainers/ancestry_hmm-s", "aliases": {"ahmm-s": "/usr/local/bin/ahmm-s"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ancestry_hmm-s.
shpc-registry automated BioContainers addition for ancestry_hmm-s
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ancestry_hmm-s
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ancestry_hmm-s:0.9.0.2--h4ac6f70_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ancestry_hmm-s/0.9.0.2--h4ac6f70_5
$ module help quay.io/biocontainers/ancestry_hmm-s/0.9.0.2--h4ac6f70_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ancestry_hmm-s-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ancestry_hmm-s-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ancestry_hmm-s-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ancestry_hmm-s-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ancestry_hmm-s-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ancestry_hmm-s-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ahmm-s

```bash
$ singularity exec <container> /usr/local/bin/ahmm-s
$ podman run --it --rm --entrypoint /usr/local/bin/ahmm-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ahmm-s   -v ${PWD} -w ${PWD} <container> -c " $@"
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