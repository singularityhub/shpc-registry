---
layout: container
name:  "quay.io/biocontainers/malva"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/malva/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/malva/container.yaml"
updated_at: "2023-02-22 03:42:12.199914"
latest: "2.0.0--h5c2bb63_1"
container_url: "https://biocontainers.pro/tools/malva"
aliases:
 - "MALVA"
 - "malva-geno"
 - "kmc"
 - "kmc_dump"
 - "kmc_tools"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "2.0.0--h5c2bb63_1"
description: "shpc-registry automated BioContainers addition for malva"
config: {"url": "https://biocontainers.pro/tools/malva", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for malva", "latest": {"2.0.0--h5c2bb63_1": "sha256:d3170db053aa6b3852fd760b2c5ab9a14585ace709dd4f50785f74ab6dab85d8"}, "tags": {"2.0.0--h5c2bb63_1": "sha256:d3170db053aa6b3852fd760b2c5ab9a14585ace709dd4f50785f74ab6dab85d8"}, "docker": "quay.io/biocontainers/malva", "aliases": {"MALVA": "/usr/local/bin/MALVA", "malva-geno": "/usr/local/bin/malva-geno", "kmc": "/usr/local/bin/kmc", "kmc_dump": "/usr/local/bin/kmc_dump", "kmc_tools": "/usr/local/bin/kmc_tools", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/malva.
shpc-registry automated BioContainers addition for malva
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/malva
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/malva:2.0.0--h5c2bb63_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/malva/2.0.0--h5c2bb63_1
$ module help quay.io/biocontainers/malva/2.0.0--h5c2bb63_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### malva-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### malva-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### malva-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### malva-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### malva-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### malva-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### MALVA

```bash
$ singularity exec <container> /usr/local/bin/MALVA
$ podman run --it --rm --entrypoint /usr/local/bin/MALVA   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MALVA   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### malva-geno

```bash
$ singularity exec <container> /usr/local/bin/malva-geno
$ podman run --it --rm --entrypoint /usr/local/bin/malva-geno   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/malva-geno   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmc

```bash
$ singularity exec <container> /usr/local/bin/kmc
$ podman run --it --rm --entrypoint /usr/local/bin/kmc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmc_dump

```bash
$ singularity exec <container> /usr/local/bin/kmc_dump
$ podman run --it --rm --entrypoint /usr/local/bin/kmc_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmc_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmc_tools

```bash
$ singularity exec <container> /usr/local/bin/kmc_tools
$ podman run --it --rm --entrypoint /usr/local/bin/kmc_tools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmc_tools   -v ${PWD} -w ${PWD} <container> -c " $@"
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