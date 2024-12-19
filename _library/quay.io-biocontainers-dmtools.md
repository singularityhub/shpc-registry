---
layout: container
name:  "quay.io/biocontainers/dmtools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dmtools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dmtools/container.yaml"
updated_at: "2024-12-19 04:45:23.671989"
latest: "0.2.6--hda3def1_0"
container_url: "https://biocontainers.pro/tools/dmtools"
aliases:
 - "bam2dm"
 - "dmDMR"
 - "dmalign"
 - "dmtools"
 - "genome2cg"
 - "genomebinLen"
 - "annot-tsv"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "0.2.6--hda3def1_0"
description: "singularity registry hpc automated addition for dmtools"
config: {"url": "https://biocontainers.pro/tools/dmtools", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for dmtools", "latest": {"0.2.6--hda3def1_0": "sha256:3d356c6f9c44f5fc4d30cb4f9a4507bc07423fb7aaa81965b3625076620b054b"}, "tags": {"0.2.6--hda3def1_0": "sha256:3d356c6f9c44f5fc4d30cb4f9a4507bc07423fb7aaa81965b3625076620b054b"}, "docker": "quay.io/biocontainers/dmtools", "aliases": {"bam2dm": "/usr/local/bin/bam2dm", "dmDMR": "/usr/local/bin/dmDMR", "dmalign": "/usr/local/bin/dmalign", "dmtools": "/usr/local/bin/dmtools", "genome2cg": "/usr/local/bin/genome2cg", "genomebinLen": "/usr/local/bin/genomebinLen", "annot-tsv": "/usr/local/bin/annot-tsv", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dmtools.
singularity registry hpc automated addition for dmtools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dmtools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dmtools:0.2.6--hda3def1_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dmtools/0.2.6--hda3def1_0
$ module help quay.io/biocontainers/dmtools/0.2.6--hda3def1_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dmtools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dmtools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dmtools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dmtools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dmtools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dmtools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bam2dm

```bash
$ singularity exec <container> /usr/local/bin/bam2dm
$ podman run --it --rm --entrypoint /usr/local/bin/bam2dm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2dm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dmDMR

```bash
$ singularity exec <container> /usr/local/bin/dmDMR
$ podman run --it --rm --entrypoint /usr/local/bin/dmDMR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dmDMR   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dmalign

```bash
$ singularity exec <container> /usr/local/bin/dmalign
$ podman run --it --rm --entrypoint /usr/local/bin/dmalign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dmalign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dmtools

```bash
$ singularity exec <container> /usr/local/bin/dmtools
$ podman run --it --rm --entrypoint /usr/local/bin/dmtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dmtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genome2cg

```bash
$ singularity exec <container> /usr/local/bin/genome2cg
$ podman run --it --rm --entrypoint /usr/local/bin/genome2cg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genome2cg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genomebinLen

```bash
$ singularity exec <container> /usr/local/bin/genomebinLen
$ podman run --it --rm --entrypoint /usr/local/bin/genomebinLen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genomebinLen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annot-tsv

```bash
$ singularity exec <container> /usr/local/bin/annot-tsv
$ podman run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
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