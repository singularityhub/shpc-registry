---
layout: container
name:  "quay.io/biocontainers/targetfinder"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/targetfinder/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/targetfinder/container.yaml"
updated_at: "2022-10-27 00:49:23.496344"
latest: "1.7--hdfd78af_4"
container_url: "https://biocontainers.pro/tools/targetfinder"
aliases:
 - "ann_pfam27.pl"
 - "ann_pfam28.pl"
 - "ann_pfam30.pl"
 - "merge_blast_btab.pl"
 - "targetfinder.pl"
 - "targetfinder_threads.pl"
versions:
 - "1.7--hdfd78af_4"
description: "shpc-registry automated BioContainers addition for targetfinder"
config: {"url": "https://biocontainers.pro/tools/targetfinder", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for targetfinder", "latest": {"1.7--hdfd78af_4": "sha256:df77da2360741dab2c559056188a246165448c93ff64b68eae1cddf75843690a"}, "tags": {"1.7--hdfd78af_4": "sha256:df77da2360741dab2c559056188a246165448c93ff64b68eae1cddf75843690a"}, "docker": "quay.io/biocontainers/targetfinder", "aliases": {"ann_pfam27.pl": "/usr/local/bin/ann_pfam27.pl", "ann_pfam28.pl": "/usr/local/bin/ann_pfam28.pl", "ann_pfam30.pl": "/usr/local/bin/ann_pfam30.pl", "merge_blast_btab.pl": "/usr/local/bin/merge_blast_btab.pl", "targetfinder.pl": "/usr/local/bin/targetfinder.pl", "targetfinder_threads.pl": "/usr/local/bin/targetfinder_threads.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/targetfinder.
shpc-registry automated BioContainers addition for targetfinder
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/targetfinder
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/targetfinder:1.7--hdfd78af_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/targetfinder/1.7--hdfd78af_4
$ module help quay.io/biocontainers/targetfinder/1.7--hdfd78af_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### targetfinder-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### targetfinder-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### targetfinder-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### targetfinder-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### targetfinder-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### targetfinder-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ann_pfam27.pl

```bash
$ singularity exec <container> /usr/local/bin/ann_pfam27.pl
$ podman run --it --rm --entrypoint /usr/local/bin/ann_pfam27.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ann_pfam27.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ann_pfam28.pl

```bash
$ singularity exec <container> /usr/local/bin/ann_pfam28.pl
$ podman run --it --rm --entrypoint /usr/local/bin/ann_pfam28.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ann_pfam28.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ann_pfam30.pl

```bash
$ singularity exec <container> /usr/local/bin/ann_pfam30.pl
$ podman run --it --rm --entrypoint /usr/local/bin/ann_pfam30.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ann_pfam30.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merge_blast_btab.pl

```bash
$ singularity exec <container> /usr/local/bin/merge_blast_btab.pl
$ podman run --it --rm --entrypoint /usr/local/bin/merge_blast_btab.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge_blast_btab.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### targetfinder.pl

```bash
$ singularity exec <container> /usr/local/bin/targetfinder.pl
$ podman run --it --rm --entrypoint /usr/local/bin/targetfinder.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/targetfinder.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### targetfinder_threads.pl

```bash
$ singularity exec <container> /usr/local/bin/targetfinder_threads.pl
$ podman run --it --rm --entrypoint /usr/local/bin/targetfinder_threads.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/targetfinder_threads.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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