---
layout: container
name:  "quay.io/biocontainers/gencore"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gencore/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gencore/container.yaml"
updated_at: "2025-07-29 03:55:25.049386"
latest: "0.17.2--he5ce664_3"
container_url: "https://biocontainers.pro/tools/gencore"
aliases:
 - "gencore"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "0.17.2--h12f7fa2_1"
 - "0.17.2--h122430f_2"
 - "0.17.2--he5ce664_3"
description: "shpc-registry automated BioContainers addition for gencore"
config: {"url": "https://biocontainers.pro/tools/gencore", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gencore", "latest": {"0.17.2--he5ce664_3": "sha256:306e96b52edf573f101ce2899249dffbfcff5c421dc3b2179d4418f78f411744"}, "tags": {"0.17.2--h12f7fa2_1": "sha256:3dd2342c4121701cd9b56c1b39e1f558b33b361ae9c5497e8c0df4210a83fe46", "0.17.2--h122430f_2": "sha256:7e39bc1a1e3d525183ba1fcef515c5bbdda71d110569f70eec8b3fb4680833b9", "0.17.2--he5ce664_3": "sha256:306e96b52edf573f101ce2899249dffbfcff5c421dc3b2179d4418f78f411744"}, "docker": "quay.io/biocontainers/gencore", "aliases": {"gencore": "/usr/local/bin/gencore", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gencore.
shpc-registry automated BioContainers addition for gencore
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gencore
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gencore:0.17.2--he5ce664_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gencore/0.17.2--he5ce664_3
$ module help quay.io/biocontainers/gencore/0.17.2--he5ce664_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gencore-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gencore-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gencore-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gencore-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gencore-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gencore-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gencore

```bash
$ singularity exec <container> /usr/local/bin/gencore
$ podman run --it --rm --entrypoint /usr/local/bin/gencore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gencore   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsfile

```bash
$ singularity exec <container> /usr/local/bin/htsfile
$ podman run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix

```bash
$ singularity exec <container> /usr/local/bin/tabix
$ podman run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
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