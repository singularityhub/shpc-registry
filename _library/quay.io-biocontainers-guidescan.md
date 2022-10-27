---
layout: container
name:  "quay.io/biocontainers/guidescan"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/guidescan/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/guidescan/container.yaml"
updated_at: "2022-10-27 00:45:10.616185"
latest: "1.2--0"
container_url: "https://biocontainers.pro/tools/guidescan"
aliases:
 - "guidescan_bamdata"
 - "guidescan_cutting_efficiency_processer"
 - "guidescan_cutting_specificity_processer"
 - "guidescan_guidequery"
 - "guidescan_processer"
versions:
 - "1.2--0"
description: "shpc-registry automated BioContainers addition for guidescan"
config: {"url": "https://biocontainers.pro/tools/guidescan", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for guidescan", "latest": {"1.2--0": "sha256:129aa8ba50df3be5a28a4411a12a4a39c2e0804017545e83713b8dc8882620d4"}, "tags": {"1.2--0": "sha256:129aa8ba50df3be5a28a4411a12a4a39c2e0804017545e83713b8dc8882620d4"}, "docker": "quay.io/biocontainers/guidescan", "aliases": {"guidescan_bamdata": "/usr/local/bin/guidescan_bamdata", "guidescan_cutting_efficiency_processer": "/usr/local/bin/guidescan_cutting_efficiency_processer", "guidescan_cutting_specificity_processer": "/usr/local/bin/guidescan_cutting_specificity_processer", "guidescan_guidequery": "/usr/local/bin/guidescan_guidequery", "guidescan_processer": "/usr/local/bin/guidescan_processer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/guidescan.
shpc-registry automated BioContainers addition for guidescan
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/guidescan
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/guidescan:1.2--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/guidescan/1.2--0
$ module help quay.io/biocontainers/guidescan/1.2--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### guidescan-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### guidescan-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### guidescan-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### guidescan-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### guidescan-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### guidescan-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### guidescan_bamdata

```bash
$ singularity exec <container> /usr/local/bin/guidescan_bamdata
$ podman run --it --rm --entrypoint /usr/local/bin/guidescan_bamdata   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/guidescan_bamdata   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### guidescan_cutting_efficiency_processer

```bash
$ singularity exec <container> /usr/local/bin/guidescan_cutting_efficiency_processer
$ podman run --it --rm --entrypoint /usr/local/bin/guidescan_cutting_efficiency_processer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/guidescan_cutting_efficiency_processer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### guidescan_cutting_specificity_processer

```bash
$ singularity exec <container> /usr/local/bin/guidescan_cutting_specificity_processer
$ podman run --it --rm --entrypoint /usr/local/bin/guidescan_cutting_specificity_processer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/guidescan_cutting_specificity_processer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### guidescan_guidequery

```bash
$ singularity exec <container> /usr/local/bin/guidescan_guidequery
$ podman run --it --rm --entrypoint /usr/local/bin/guidescan_guidequery   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/guidescan_guidequery   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### guidescan_processer

```bash
$ singularity exec <container> /usr/local/bin/guidescan_processer
$ podman run --it --rm --entrypoint /usr/local/bin/guidescan_processer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/guidescan_processer   -v ${PWD} -w ${PWD} <container> -c " $@"
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