---
layout: container
name:  "quay.io/biocontainers/viral_consensus"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/viral_consensus/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/viral_consensus/container.yaml"
updated_at: "2025-10-07 03:08:28.184310"
latest: "1.0.0--hcf1f8c1_0"
container_url: "https://biocontainers.pro/tools/viral_consensus"
aliases:
 - "viral_consensus"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "0.0.4--h0033a41_0"
 - "0.0.5--h43eeafb_1"
 - "0.0.6--h43eeafb_1"
 - "1.0.0--hcf1f8c1_0"
description: "singularity registry hpc automated addition for viral_consensus"
config: {"url": "https://biocontainers.pro/tools/viral_consensus", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for viral_consensus", "latest": {"1.0.0--hcf1f8c1_0": "sha256:b13056a49003b4d4869b0656a841bc995193fac188504aca90d2c1763391b463"}, "tags": {"0.0.4--h0033a41_0": "sha256:1081f2581f356e22ebf2dee2097b36e3fb2b275f2c0af027896ef0fc077b75a6", "0.0.5--h43eeafb_1": "sha256:ad90e76e004e772440ca4a0bcf9c5ff26b37f60d804cfa81b026f8ce8c6a0b6e", "0.0.6--h43eeafb_1": "sha256:9302b322b5584987e06d34e97603a6038aeda0cd263d5befd94a6b8ec11ac2e0", "1.0.0--hcf1f8c1_0": "sha256:b13056a49003b4d4869b0656a841bc995193fac188504aca90d2c1763391b463"}, "docker": "quay.io/biocontainers/viral_consensus", "aliases": {"viral_consensus": "/usr/local/bin/viral_consensus", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/viral_consensus.
singularity registry hpc automated addition for viral_consensus
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/viral_consensus
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/viral_consensus:1.0.0--hcf1f8c1_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/viral_consensus/1.0.0--hcf1f8c1_0
$ module help quay.io/biocontainers/viral_consensus/1.0.0--hcf1f8c1_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### viral_consensus-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### viral_consensus-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### viral_consensus-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### viral_consensus-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### viral_consensus-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### viral_consensus-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### viral_consensus

```bash
$ singularity exec <container> /usr/local/bin/viral_consensus
$ podman run --it --rm --entrypoint /usr/local/bin/viral_consensus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/viral_consensus   -v ${PWD} -w ${PWD} <container> -c " $@"
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