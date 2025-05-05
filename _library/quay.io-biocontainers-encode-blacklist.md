---
layout: container
name:  "quay.io/biocontainers/encode-blacklist"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/encode-blacklist/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/encode-blacklist/container.yaml"
updated_at: "2025-05-05 03:20:25.933242"
latest: "2.0--h06902ac_6"
container_url: "https://biocontainers.pro/tools/encode-blacklist"
aliases:
 - "Blacklist"
 - "bamtools"
versions:
 - "2.0--ha7703dc_3"
 - "2.0--hf393df8_4"
 - "2.0--h7a259b3_5"
 - "2.0--h06902ac_6"
description: "shpc-registry automated BioContainers addition for encode-blacklist"
config: {"url": "https://biocontainers.pro/tools/encode-blacklist", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for encode-blacklist", "latest": {"2.0--h06902ac_6": "sha256:061e0b96e9e588ecb67169c7b434b536f1764f06fe6c88563411123714d5f55f"}, "tags": {"2.0--ha7703dc_3": "sha256:adc639d3f09c500df9b82edf3f7f1f7ec636d84c7259036757a5625334323a45", "2.0--hf393df8_4": "sha256:417fe57ca178257398981453e4d21f17c466b5c2e2cde47796b7ed232706684d", "2.0--h7a259b3_5": "sha256:92d085211ffd760ed49948249122b1444c0e32c18f0fc30aeb93baeccba47927", "2.0--h06902ac_6": "sha256:061e0b96e9e588ecb67169c7b434b536f1764f06fe6c88563411123714d5f55f"}, "docker": "quay.io/biocontainers/encode-blacklist", "aliases": {"Blacklist": "/usr/local/bin/Blacklist", "bamtools": "/usr/local/bin/bamtools"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/encode-blacklist.
shpc-registry automated BioContainers addition for encode-blacklist
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/encode-blacklist
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/encode-blacklist:2.0--h06902ac_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/encode-blacklist/2.0--h06902ac_6
$ module help quay.io/biocontainers/encode-blacklist/2.0--h06902ac_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### encode-blacklist-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### encode-blacklist-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### encode-blacklist-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### encode-blacklist-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### encode-blacklist-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### encode-blacklist-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Blacklist

```bash
$ singularity exec <container> /usr/local/bin/Blacklist
$ podman run --it --rm --entrypoint /usr/local/bin/Blacklist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Blacklist   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamtools

```bash
$ singularity exec <container> /usr/local/bin/bamtools
$ podman run --it --rm --entrypoint /usr/local/bin/bamtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamtools   -v ${PWD} -w ${PWD} <container> -c " $@"
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