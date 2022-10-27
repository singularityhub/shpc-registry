---
layout: container
name:  "quay.io/biocontainers/kofamscan"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kofamscan/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/kofamscan/container.yaml"
updated_at: "2022-10-27 00:55:47.505695"
latest: "1.3.0--hdfd78af_2"
container_url: "https://biocontainers.pro/tools/kofamscan"
aliases:
 - ".kofamscan-post-link.sh"
 - "exec_annotation"
 - "racc"
 - "racc2y"
 - "y2racc"
versions:
 - "1.3.0--hdfd78af_2"
description: "shpc-registry automated BioContainers addition for kofamscan"
config: {"url": "https://biocontainers.pro/tools/kofamscan", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for kofamscan", "latest": {"1.3.0--hdfd78af_2": "sha256:afc460a9bdbc6dcd00ee37e40f2b6d4f35ac87e2d8e6b93a3353d6e5fa658c66"}, "tags": {"1.3.0--hdfd78af_2": "sha256:afc460a9bdbc6dcd00ee37e40f2b6d4f35ac87e2d8e6b93a3353d6e5fa658c66"}, "docker": "quay.io/biocontainers/kofamscan", "aliases": {".kofamscan-post-link.sh": "/usr/local/bin/.kofamscan-post-link.sh", "exec_annotation": "/usr/local/bin/exec_annotation", "racc": "/usr/local/bin/racc", "racc2y": "/usr/local/bin/racc2y", "y2racc": "/usr/local/bin/y2racc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/kofamscan.
shpc-registry automated BioContainers addition for kofamscan
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kofamscan
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kofamscan:1.3.0--hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kofamscan/1.3.0--hdfd78af_2
$ module help quay.io/biocontainers/kofamscan/1.3.0--hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kofamscan-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kofamscan-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kofamscan-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kofamscan-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kofamscan-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kofamscan-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .kofamscan-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.kofamscan-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.kofamscan-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.kofamscan-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exec_annotation

```bash
$ singularity exec <container> /usr/local/bin/exec_annotation
$ podman run --it --rm --entrypoint /usr/local/bin/exec_annotation   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exec_annotation   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### racc

```bash
$ singularity exec <container> /usr/local/bin/racc
$ podman run --it --rm --entrypoint /usr/local/bin/racc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/racc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### racc2y

```bash
$ singularity exec <container> /usr/local/bin/racc2y
$ podman run --it --rm --entrypoint /usr/local/bin/racc2y   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/racc2y   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### y2racc

```bash
$ singularity exec <container> /usr/local/bin/y2racc
$ podman run --it --rm --entrypoint /usr/local/bin/y2racc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/y2racc   -v ${PWD} -w ${PWD} <container> -c " $@"
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