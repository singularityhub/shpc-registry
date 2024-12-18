---
layout: container
name:  "quay.io/biocontainers/dms"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dms/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dms/container.yaml"
updated_at: "2024-12-18 03:08:37.865913"
latest: "1.1--hc9558a2_0"
container_url: "https://biocontainers.pro/tools/dms"
aliases:
 - "MS-comp-taxa"
 - "MS-comp-taxa-dynamic"
 - "MS-make-ref"
 - "MS-single-to-table"
 - "MS-table-to-single"
versions:
 - "1.1--hc9558a2_0"
description: "shpc-registry automated BioContainers addition for dms"
config: {"url": "https://biocontainers.pro/tools/dms", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dms", "latest": {"1.1--hc9558a2_0": "sha256:6f1b91fe03e79e3a509c8cf5ec275db845a741960233ec6abf36290307514486"}, "tags": {"1.1--hc9558a2_0": "sha256:6f1b91fe03e79e3a509c8cf5ec275db845a741960233ec6abf36290307514486"}, "docker": "quay.io/biocontainers/dms", "aliases": {"MS-comp-taxa": "/usr/local/bin/MS-comp-taxa", "MS-comp-taxa-dynamic": "/usr/local/bin/MS-comp-taxa-dynamic", "MS-make-ref": "/usr/local/bin/MS-make-ref", "MS-single-to-table": "/usr/local/bin/MS-single-to-table", "MS-table-to-single": "/usr/local/bin/MS-table-to-single"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dms.
shpc-registry automated BioContainers addition for dms
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dms
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dms:1.1--hc9558a2_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dms/1.1--hc9558a2_0
$ module help quay.io/biocontainers/dms/1.1--hc9558a2_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dms-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dms-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dms-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dms-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dms-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dms-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### MS-comp-taxa

```bash
$ singularity exec <container> /usr/local/bin/MS-comp-taxa
$ podman run --it --rm --entrypoint /usr/local/bin/MS-comp-taxa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MS-comp-taxa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MS-comp-taxa-dynamic

```bash
$ singularity exec <container> /usr/local/bin/MS-comp-taxa-dynamic
$ podman run --it --rm --entrypoint /usr/local/bin/MS-comp-taxa-dynamic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MS-comp-taxa-dynamic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MS-make-ref

```bash
$ singularity exec <container> /usr/local/bin/MS-make-ref
$ podman run --it --rm --entrypoint /usr/local/bin/MS-make-ref   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MS-make-ref   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MS-single-to-table

```bash
$ singularity exec <container> /usr/local/bin/MS-single-to-table
$ podman run --it --rm --entrypoint /usr/local/bin/MS-single-to-table   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MS-single-to-table   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MS-table-to-single

```bash
$ singularity exec <container> /usr/local/bin/MS-table-to-single
$ podman run --it --rm --entrypoint /usr/local/bin/MS-table-to-single   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MS-table-to-single   -v ${PWD} -w ${PWD} <container> -c " $@"
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