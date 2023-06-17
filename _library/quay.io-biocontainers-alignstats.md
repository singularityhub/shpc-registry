---
layout: container
name:  "quay.io/biocontainers/alignstats"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/alignstats/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/alignstats/container.yaml"
updated_at: "2023-06-17 02:45:38.795482"
latest: "0.10--h031d066_1"
container_url: "https://biocontainers.pro/tools/alignstats"
aliases:
 - "alignstats"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "0.9.1--hec16e2b_2"
 - "0.10--hec16e2b_0"
 - "0.10--h031d066_1"
description: "shpc-registry automated BioContainers addition for alignstats"
config: {"url": "https://biocontainers.pro/tools/alignstats", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for alignstats", "latest": {"0.10--h031d066_1": "sha256:bf89356d81547c963452f3147a69b36401a9d2475c3a7958f371d69ed0c28978"}, "tags": {"0.9.1--hec16e2b_2": "sha256:06e06fc0252d6bf34b254ef0b4cef75f868e5e0b25f522e75f1f784c0014700b", "0.10--hec16e2b_0": "sha256:65a233cc97cc1a5437ff5fdeb5f2d4e7888cb4d347574a55cfda1e62ea76548b", "0.10--h031d066_1": "sha256:bf89356d81547c963452f3147a69b36401a9d2475c3a7958f371d69ed0c28978"}, "docker": "quay.io/biocontainers/alignstats", "aliases": {"alignstats": "/usr/local/bin/alignstats", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/alignstats.
shpc-registry automated BioContainers addition for alignstats
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/alignstats
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/alignstats:0.10--h031d066_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/alignstats/0.10--h031d066_1
$ module help quay.io/biocontainers/alignstats/0.10--h031d066_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### alignstats-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### alignstats-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### alignstats-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### alignstats-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### alignstats-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### alignstats-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### alignstats

```bash
$ singularity exec <container> /usr/local/bin/alignstats
$ podman run --it --rm --entrypoint /usr/local/bin/alignstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alignstats   -v ${PWD} -w ${PWD} <container> -c " $@"
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