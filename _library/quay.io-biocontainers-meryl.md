---
layout: container
name:  "quay.io/biocontainers/meryl"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/meryl/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/meryl/container.yaml"
updated_at: "2023-03-08 03:21:30.009463"
latest: "1.3--h87f3376_1"
container_url: "https://biocontainers.pro/tools/meryl"
aliases:
 - "meryl"
 - "meryl-import"
 - "meryl-lookup"
 - "sequence"
versions:
 - "v1.0--hc9558a2_0"
 - "1.3--h87f3376_1"
 - "1.2--h1b792b2_1"
description: "shpc-registry automated BioContainers addition for meryl"
config: {"url": "https://biocontainers.pro/tools/meryl", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for meryl", "latest": {"1.3--h87f3376_1": "sha256:09d885c2ff293aff190cf2b8f8d022bbb5d590c4b3af8805d9c0536ba4a59faa"}, "tags": {"v1.0--hc9558a2_0": "sha256:09fb2dd161e0f96f755dd567d59d12b802fb757af1cc9642c5b851903dbb6099", "1.3--h87f3376_1": "sha256:09d885c2ff293aff190cf2b8f8d022bbb5d590c4b3af8805d9c0536ba4a59faa", "1.2--h1b792b2_1": "sha256:69343475b90a3401e09a4358365ee8c1d807b5ec534b628e324a95ac8d39731f"}, "docker": "quay.io/biocontainers/meryl", "aliases": {"meryl": "/usr/local/bin/meryl", "meryl-import": "/usr/local/bin/meryl-import", "meryl-lookup": "/usr/local/bin/meryl-lookup", "sequence": "/usr/local/bin/sequence"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/meryl.
shpc-registry automated BioContainers addition for meryl
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/meryl
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/meryl:1.3--h87f3376_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/meryl/1.3--h87f3376_1
$ module help quay.io/biocontainers/meryl/1.3--h87f3376_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### meryl-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### meryl-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### meryl-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### meryl-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### meryl-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### meryl-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### meryl

```bash
$ singularity exec <container> /usr/local/bin/meryl
$ podman run --it --rm --entrypoint /usr/local/bin/meryl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/meryl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### meryl-import

```bash
$ singularity exec <container> /usr/local/bin/meryl-import
$ podman run --it --rm --entrypoint /usr/local/bin/meryl-import   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/meryl-import   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### meryl-lookup

```bash
$ singularity exec <container> /usr/local/bin/meryl-lookup
$ podman run --it --rm --entrypoint /usr/local/bin/meryl-lookup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/meryl-lookup   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sequence

```bash
$ singularity exec <container> /usr/local/bin/sequence
$ podman run --it --rm --entrypoint /usr/local/bin/sequence   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sequence   -v ${PWD} -w ${PWD} <container> -c " $@"
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