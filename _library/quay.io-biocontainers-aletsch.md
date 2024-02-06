---
layout: container
name:  "quay.io/biocontainers/aletsch"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/aletsch/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/aletsch/container.yaml"
updated_at: "2024-02-06 02:34:15.778654"
latest: "1.0.3--h5642b88_6"
container_url: "https://biocontainers.pro/tools/aletsch"
aliases:
 - "aletsch"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "1.0.3--hefd527f_4"
 - "1.0.3--h66ab1b6_5"
 - "1.0.3--h5642b88_6"
description: "shpc-registry automated BioContainers addition for aletsch"
config: {"url": "https://biocontainers.pro/tools/aletsch", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for aletsch", "latest": {"1.0.3--h5642b88_6": "sha256:979a4313a822a4e1e4164ad3119bb9a984e4c38cd569062c2283ebeb91d8b743"}, "tags": {"1.0.3--hefd527f_4": "sha256:70878181b401760d539c273170eb44b0b37984dc6b3db33977265024001db755", "1.0.3--h66ab1b6_5": "sha256:990b58274b1419c87200feed353a842384329364c1eca3e984475dcfe3b91eb0", "1.0.3--h5642b88_6": "sha256:979a4313a822a4e1e4164ad3119bb9a984e4c38cd569062c2283ebeb91d8b743"}, "docker": "quay.io/biocontainers/aletsch", "aliases": {"aletsch": "/usr/local/bin/aletsch", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/aletsch.
shpc-registry automated BioContainers addition for aletsch
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/aletsch
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/aletsch:1.0.3--h5642b88_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/aletsch/1.0.3--h5642b88_6
$ module help quay.io/biocontainers/aletsch/1.0.3--h5642b88_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### aletsch-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### aletsch-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### aletsch-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### aletsch-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### aletsch-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### aletsch-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### aletsch

```bash
$ singularity exec <container> /usr/local/bin/aletsch
$ podman run --it --rm --entrypoint /usr/local/bin/aletsch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aletsch   -v ${PWD} -w ${PWD} <container> -c " $@"
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