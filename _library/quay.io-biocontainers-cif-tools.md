---
layout: container
name:  "quay.io/biocontainers/cif-tools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cif-tools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cif-tools/container.yaml"
updated_at: "2025-09-16 04:49:08.128250"
latest: "1.0.12--h077b44d_0"
container_url: "https://biocontainers.pro/tools/cif-tools"
aliases:
 - "cif-diff"
 - "cif-grep"
 - "cif-merge"
 - "cif-validate"
 - "cif2pdb"
 - "mmCQL"
 - "pdb2cif"
versions:
 - "1.0.12--h077b44d_0"
description: "singularity registry hpc automated addition for cif-tools"
config: {"url": "https://biocontainers.pro/tools/cif-tools", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for cif-tools", "latest": {"1.0.12--h077b44d_0": "sha256:55e7990c00174aecca6204b87d4e2a8dc64dcc78f68e204b885c8dff7e6789ed"}, "tags": {"1.0.12--h077b44d_0": "sha256:55e7990c00174aecca6204b87d4e2a8dc64dcc78f68e204b885c8dff7e6789ed"}, "docker": "quay.io/biocontainers/cif-tools", "aliases": {"cif-diff": "/usr/local/bin/cif-diff", "cif-grep": "/usr/local/bin/cif-grep", "cif-merge": "/usr/local/bin/cif-merge", "cif-validate": "/usr/local/bin/cif-validate", "cif2pdb": "/usr/local/bin/cif2pdb", "mmCQL": "/usr/local/bin/mmCQL", "pdb2cif": "/usr/local/bin/pdb2cif"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cif-tools.
singularity registry hpc automated addition for cif-tools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cif-tools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cif-tools:1.0.12--h077b44d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cif-tools/1.0.12--h077b44d_0
$ module help quay.io/biocontainers/cif-tools/1.0.12--h077b44d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cif-tools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cif-tools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cif-tools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cif-tools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cif-tools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cif-tools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cif-diff

```bash
$ singularity exec <container> /usr/local/bin/cif-diff
$ podman run --it --rm --entrypoint /usr/local/bin/cif-diff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cif-diff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cif-grep

```bash
$ singularity exec <container> /usr/local/bin/cif-grep
$ podman run --it --rm --entrypoint /usr/local/bin/cif-grep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cif-grep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cif-merge

```bash
$ singularity exec <container> /usr/local/bin/cif-merge
$ podman run --it --rm --entrypoint /usr/local/bin/cif-merge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cif-merge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cif-validate

```bash
$ singularity exec <container> /usr/local/bin/cif-validate
$ podman run --it --rm --entrypoint /usr/local/bin/cif-validate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cif-validate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cif2pdb

```bash
$ singularity exec <container> /usr/local/bin/cif2pdb
$ podman run --it --rm --entrypoint /usr/local/bin/cif2pdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cif2pdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mmCQL

```bash
$ singularity exec <container> /usr/local/bin/mmCQL
$ podman run --it --rm --entrypoint /usr/local/bin/mmCQL   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mmCQL   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdb2cif

```bash
$ singularity exec <container> /usr/local/bin/pdb2cif
$ podman run --it --rm --entrypoint /usr/local/bin/pdb2cif   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdb2cif   -v ${PWD} -w ${PWD} <container> -c " $@"
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