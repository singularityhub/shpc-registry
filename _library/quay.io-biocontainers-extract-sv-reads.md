---
layout: container
name:  "quay.io/biocontainers/extract-sv-reads"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/extract-sv-reads/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/extract-sv-reads/container.yaml"
updated_at: "2024-09-05 03:25:55.429123"
latest: "1.3.0--pl5321h4ac6f70_5"
container_url: "https://biocontainers.pro/tools/extract-sv-reads"
aliases:
 - "extract-sv-reads"
 - "htsfile"
 - "bgzip"
 - "tabix"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "1.3.0--pl5321h2df963e_3"
 - "1.3.0--pl5321h376f1d3_4"
 - "1.3.0--pl5321h4ac6f70_5"
description: "shpc-registry automated BioContainers addition for extract-sv-reads"
config: {"url": "https://biocontainers.pro/tools/extract-sv-reads", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for extract-sv-reads", "latest": {"1.3.0--pl5321h4ac6f70_5": "sha256:92a222d0fd2da68db8b244b1858950b0388445c57dd241fbdae3f50b02eee7d2"}, "tags": {"1.3.0--pl5321h2df963e_3": "sha256:f12edee3c89ff878ec38b1f132ef0f5f9487ef99dcecd5c239c1ac6b70de9622", "1.3.0--pl5321h376f1d3_4": "sha256:ab377bdb5bd02b56da34e4f4ca8871a29bd5351b1031d622b806da2fcf9049cc", "1.3.0--pl5321h4ac6f70_5": "sha256:92a222d0fd2da68db8b244b1858950b0388445c57dd241fbdae3f50b02eee7d2"}, "docker": "quay.io/biocontainers/extract-sv-reads", "aliases": {"extract-sv-reads": "/usr/local/bin/extract-sv-reads", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/extract-sv-reads.
shpc-registry automated BioContainers addition for extract-sv-reads
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/extract-sv-reads
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/extract-sv-reads:1.3.0--pl5321h4ac6f70_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/extract-sv-reads/1.3.0--pl5321h4ac6f70_5
$ module help quay.io/biocontainers/extract-sv-reads/1.3.0--pl5321h4ac6f70_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### extract-sv-reads-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### extract-sv-reads-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### extract-sv-reads-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### extract-sv-reads-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### extract-sv-reads-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### extract-sv-reads-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### extract-sv-reads

```bash
$ singularity exec <container> /usr/local/bin/extract-sv-reads
$ podman run --it --rm --entrypoint /usr/local/bin/extract-sv-reads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract-sv-reads   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### perl5.32.1

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.1
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamzip

```bash
$ singularity exec <container> /usr/local/bin/streamzip
$ podman run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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