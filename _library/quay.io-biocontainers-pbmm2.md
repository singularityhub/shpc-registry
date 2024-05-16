---
layout: container
name:  "quay.io/biocontainers/pbmm2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pbmm2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pbmm2/container.yaml"
updated_at: "2024-05-16 02:46:48.965466"
latest: "1.13.1--h9ee0642_0"
container_url: "https://biocontainers.pro/tools/pbmm2"
aliases:
 - "pbmm2"
versions:
 - "1.9.0--h9ee0642_0"
 - "1.10.0--h9ee0642_0"
 - "1.12.0--h9ee0642_0"
 - "1.13.0--h9ee0642_0"
 - "1.13.1--h9ee0642_0"
description: "shpc-registry automated BioContainers addition for pbmm2"
config: {"url": "https://biocontainers.pro/tools/pbmm2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pbmm2", "latest": {"1.13.1--h9ee0642_0": "sha256:5e8ae8904d2e493bcd397293df4a59496afb6f82ee749e6d890ed4a115d080a0"}, "tags": {"1.9.0--h9ee0642_0": "sha256:0393f964d064053459ae410a0c8d313bbf5cd06b74906c53d13c094cb327ee79", "1.10.0--h9ee0642_0": "sha256:f00bb97c3e6fcec879acb3c5c485a154eae8a0582b84b5a43a3b2dbd168a4b38", "1.12.0--h9ee0642_0": "sha256:d16e5df5bfab75ff2defd2984ec6cb7665473e383045e2a075ea1261ae188861", "1.13.0--h9ee0642_0": "sha256:05cc02e1c9d211430f3862f305ba064af4f3b393ee3bbafd585f49adaef89fb0", "1.13.1--h9ee0642_0": "sha256:5e8ae8904d2e493bcd397293df4a59496afb6f82ee749e6d890ed4a115d080a0"}, "docker": "quay.io/biocontainers/pbmm2", "aliases": {"pbmm2": "/usr/local/bin/pbmm2"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pbmm2.
shpc-registry automated BioContainers addition for pbmm2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pbmm2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pbmm2:1.13.1--h9ee0642_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pbmm2/1.13.1--h9ee0642_0
$ module help quay.io/biocontainers/pbmm2/1.13.1--h9ee0642_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pbmm2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pbmm2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pbmm2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pbmm2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pbmm2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pbmm2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pbmm2

```bash
$ singularity exec <container> /usr/local/bin/pbmm2
$ podman run --it --rm --entrypoint /usr/local/bin/pbmm2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbmm2   -v ${PWD} -w ${PWD} <container> -c " $@"
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