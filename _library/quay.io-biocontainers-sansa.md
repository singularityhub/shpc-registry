---
layout: container
name:  "quay.io/biocontainers/sansa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sansa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sansa/container.yaml"
updated_at: "2024-04-04 04:07:53.498767"
latest: "0.2.1--hb7e2ac5_0"
container_url: "https://biocontainers.pro/tools/sansa"
aliases:
 - "sansa"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "0.0.8--h2e9000e_4"
 - "0.0.8--hc64ef6e_5"
 - "0.0.8--hdc14858_6"
 - "0.2.1--hb7e2ac5_0"
 - "0.1.1--hb7e2ac5_0"
description: "shpc-registry automated BioContainers addition for sansa"
config: {"url": "https://biocontainers.pro/tools/sansa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sansa", "latest": {"0.2.1--hb7e2ac5_0": "sha256:156906d965d3df5951dabb422faa034c00d9829705d377cab5ed8a25f43bd05c"}, "tags": {"0.0.8--h2e9000e_4": "sha256:97631d721171c37c444d137a28c4f0f518c1a6cf91da62de40101093ce4c260a", "0.0.8--hc64ef6e_5": "sha256:c9b27364965d92d66ab6ae8ca72f2b6455202c9990f30fabcae59116cca34e95", "0.0.8--hdc14858_6": "sha256:202785b6f062d3783595457db046c8920e13d90383863f6bbe5cd5b0d89b401c", "0.2.1--hb7e2ac5_0": "sha256:156906d965d3df5951dabb422faa034c00d9829705d377cab5ed8a25f43bd05c", "0.1.1--hb7e2ac5_0": "sha256:18f09e8b19842fdc5fa89ceda8f322ff3a4c2eaa64ac9ac91b030cc16ac07dd7"}, "docker": "quay.io/biocontainers/sansa", "aliases": {"sansa": "/usr/local/bin/sansa", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sansa.
shpc-registry automated BioContainers addition for sansa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sansa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sansa:0.2.1--hb7e2ac5_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sansa/0.2.1--hb7e2ac5_0
$ module help quay.io/biocontainers/sansa/0.2.1--hb7e2ac5_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sansa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sansa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sansa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sansa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sansa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sansa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sansa

```bash
$ singularity exec <container> /usr/local/bin/sansa
$ podman run --it --rm --entrypoint /usr/local/bin/sansa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sansa   -v ${PWD} -w ${PWD} <container> -c " $@"
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