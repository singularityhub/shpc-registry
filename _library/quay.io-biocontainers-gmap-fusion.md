---
layout: container
name:  "quay.io/biocontainers/gmap-fusion"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gmap-fusion/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/gmap-fusion/container.yaml"
updated_at: "2022-10-27 00:18:29.909486"
latest: "0.4.0--2"
container_url: "https://biocontainers.pro/tools/gmap-fusion"
aliases:
 - ".gmap-fusion-post-link.sh"
 - "GMAP-fusion"
 - "gmap_compress"
 - "gmap_reassemble"
 - "gmap_uncompress"
versions:
 - "0.4.0--2"
description: "shpc-registry automated BioContainers addition for gmap-fusion"
config: {"url": "https://biocontainers.pro/tools/gmap-fusion", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gmap-fusion", "latest": {"0.4.0--2": "sha256:40465100fd9563473496cc6d56e303b77cc691079a934db0e1b65b4a3f677e4f"}, "tags": {"0.4.0--2": "sha256:40465100fd9563473496cc6d56e303b77cc691079a934db0e1b65b4a3f677e4f"}, "docker": "quay.io/biocontainers/gmap-fusion", "aliases": {".gmap-fusion-post-link.sh": "/usr/local/bin/.gmap-fusion-post-link.sh", "GMAP-fusion": "/usr/local/bin/GMAP-fusion", "gmap_compress": "/usr/local/bin/gmap_compress", "gmap_reassemble": "/usr/local/bin/gmap_reassemble", "gmap_uncompress": "/usr/local/bin/gmap_uncompress"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gmap-fusion.
shpc-registry automated BioContainers addition for gmap-fusion
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gmap-fusion
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gmap-fusion:0.4.0--2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gmap-fusion/0.4.0--2
$ module help quay.io/biocontainers/gmap-fusion/0.4.0--2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gmap-fusion-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gmap-fusion-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gmap-fusion-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gmap-fusion-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gmap-fusion-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gmap-fusion-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .gmap-fusion-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.gmap-fusion-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.gmap-fusion-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.gmap-fusion-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GMAP-fusion

```bash
$ singularity exec <container> /usr/local/bin/GMAP-fusion
$ podman run --it --rm --entrypoint /usr/local/bin/GMAP-fusion   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GMAP-fusion   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmap_compress

```bash
$ singularity exec <container> /usr/local/bin/gmap_compress
$ podman run --it --rm --entrypoint /usr/local/bin/gmap_compress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmap_compress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmap_reassemble

```bash
$ singularity exec <container> /usr/local/bin/gmap_reassemble
$ podman run --it --rm --entrypoint /usr/local/bin/gmap_reassemble   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmap_reassemble   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gmap_uncompress

```bash
$ singularity exec <container> /usr/local/bin/gmap_uncompress
$ podman run --it --rm --entrypoint /usr/local/bin/gmap_uncompress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gmap_uncompress   -v ${PWD} -w ${PWD} <container> -c " $@"
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