---
layout: container
name:  "quay.io/biocontainers/shapeit4"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/shapeit4/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/shapeit4/container.yaml"
updated_at: "2024-07-01 03:40:15.064832"
latest: "4.2.2--h95d4b32_4"
container_url: "https://biocontainers.pro/tools/shapeit4"
aliases:
 - "shapeit4"
 - "shapeit4.2"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "4.2.2--h24bf969_1"
 - "4.2.2--h3fe290a_3"
 - "4.2.2--h95d4b32_4"
description: "shpc-registry automated BioContainers addition for shapeit4"
config: {"url": "https://biocontainers.pro/tools/shapeit4", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for shapeit4", "latest": {"4.2.2--h95d4b32_4": "sha256:90f225faef7cefbe7c65031e16b7c84ac26dba76a3754c021faf2e4337b51a94"}, "tags": {"4.2.2--h24bf969_1": "sha256:99027f00d2dabd6151f01612cc17d06c1a8731a04473bc2ad24a4cb1f734a861", "4.2.2--h3fe290a_3": "sha256:5f48c74a5cf6ce180071ec080b7ec88ef196a8477d8b9c1e0d71dc5a5ae54edd", "4.2.2--h95d4b32_4": "sha256:90f225faef7cefbe7c65031e16b7c84ac26dba76a3754c021faf2e4337b51a94"}, "docker": "quay.io/biocontainers/shapeit4", "aliases": {"shapeit4": "/usr/local/bin/shapeit4", "shapeit4.2": "/usr/local/bin/shapeit4.2", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/shapeit4.
shpc-registry automated BioContainers addition for shapeit4
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/shapeit4
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/shapeit4:4.2.2--h95d4b32_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/shapeit4/4.2.2--h95d4b32_4
$ module help quay.io/biocontainers/shapeit4/4.2.2--h95d4b32_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### shapeit4-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### shapeit4-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### shapeit4-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### shapeit4-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### shapeit4-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### shapeit4-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### shapeit4

```bash
$ singularity exec <container> /usr/local/bin/shapeit4
$ podman run --it --rm --entrypoint /usr/local/bin/shapeit4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shapeit4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shapeit4.2

```bash
$ singularity exec <container> /usr/local/bin/shapeit4.2
$ podman run --it --rm --entrypoint /usr/local/bin/shapeit4.2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shapeit4.2   -v ${PWD} -w ${PWD} <container> -c " $@"
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