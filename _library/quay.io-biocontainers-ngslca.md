---
layout: container
name:  "quay.io/biocontainers/ngslca"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ngslca/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ngslca/container.yaml"
updated_at: "2025-06-26 04:16:10.480456"
latest: "1.0.5--h13024bc_4"
container_url: "https://biocontainers.pro/tools/ngslca"
aliases:
 - "ngsLCA"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "1.0.5--h470d46e_0"
 - "1.0.5--h6448e42_1"
 - "1.0.5--hce60e53_2"
 - "1.0.5--hf5e1c6e_3"
 - "1.0.5--h13024bc_4"
description: "singularity registry hpc automated addition for ngslca"
config: {"url": "https://biocontainers.pro/tools/ngslca", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for ngslca", "latest": {"1.0.5--h13024bc_4": "sha256:8a769e41fe3ed878ad64df9bc0edaa70d72177df3e62cd7c6c64c8faa5032963"}, "tags": {"1.0.5--h470d46e_0": "sha256:34ebdc114757332e611bff8eb000d88b12300c0380feea73be815580722ab38d", "1.0.5--h6448e42_1": "sha256:17eb034ec154c54ba581460913fb5da4a83a22885bd1c53f8648a84fcb7778b3", "1.0.5--hce60e53_2": "sha256:8a20b09ba2f66dc0ecd00ab24dab3eb9cc4e02cf7ee57e911f6f500a3e32f5de", "1.0.5--hf5e1c6e_3": "sha256:bf99407a757f00407c563a2a33a1c73b98ce9c6f239dec14309c44e787c161f0", "1.0.5--h13024bc_4": "sha256:8a769e41fe3ed878ad64df9bc0edaa70d72177df3e62cd7c6c64c8faa5032963"}, "docker": "quay.io/biocontainers/ngslca", "aliases": {"ngsLCA": "/usr/local/bin/ngsLCA", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ngslca.
singularity registry hpc automated addition for ngslca
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ngslca
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ngslca:1.0.5--h13024bc_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ngslca/1.0.5--h13024bc_4
$ module help quay.io/biocontainers/ngslca/1.0.5--h13024bc_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ngslca-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ngslca-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ngslca-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ngslca-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ngslca-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ngslca-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ngsLCA

```bash
$ singularity exec <container> /usr/local/bin/ngsLCA
$ podman run --it --rm --entrypoint /usr/local/bin/ngsLCA   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngsLCA   -v ${PWD} -w ${PWD} <container> -c " $@"
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