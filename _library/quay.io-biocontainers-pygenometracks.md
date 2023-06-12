---
layout: container
name:  "quay.io/biocontainers/pygenometracks"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pygenometracks/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pygenometracks/container.yaml"
updated_at: "2023-06-12 03:29:44.419380"
latest: "3.8--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/pygenometracks"
aliases:
 - "make_tracks_file"
 - "pgt"
 - "pyGenomeTracks"
 - "cooler"
 - "bam2pairs"
 - "column_remover.pl"
 - "duplicate_header_remover.pl"
 - "fragment_4dnpairs.pl"
 - "juicer_shortform2pairs.pl"
 - "merge-pairs.sh"
 - "merged_nodup2pairs.pl"
 - "old_merged_nodup2pairs.pl"
 - "pairix"
versions:
 - "3.7--pyhdfd78af_0"
 - "3.8--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for pygenometracks"
config: {"url": "https://biocontainers.pro/tools/pygenometracks", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pygenometracks", "latest": {"3.8--pyhdfd78af_0": "sha256:3fa00e0a232714693f7bb6ba31a2063ce14b4f65b274bb49469af19f2b903409"}, "tags": {"3.7--pyhdfd78af_0": "sha256:275cc3a08e50ecd803ae7fd5e572cf4fb640d06a51792a313260bd9a8e2a54ee", "3.8--pyhdfd78af_0": "sha256:3fa00e0a232714693f7bb6ba31a2063ce14b4f65b274bb49469af19f2b903409"}, "docker": "quay.io/biocontainers/pygenometracks", "aliases": {"make_tracks_file": "/usr/local/bin/make_tracks_file", "pgt": "/usr/local/bin/pgt", "pyGenomeTracks": "/usr/local/bin/pyGenomeTracks", "cooler": "/usr/local/bin/cooler", "bam2pairs": "/usr/local/bin/bam2pairs", "column_remover.pl": "/usr/local/bin/column_remover.pl", "duplicate_header_remover.pl": "/usr/local/bin/duplicate_header_remover.pl", "fragment_4dnpairs.pl": "/usr/local/bin/fragment_4dnpairs.pl", "juicer_shortform2pairs.pl": "/usr/local/bin/juicer_shortform2pairs.pl", "merge-pairs.sh": "/usr/local/bin/merge-pairs.sh", "merged_nodup2pairs.pl": "/usr/local/bin/merged_nodup2pairs.pl", "old_merged_nodup2pairs.pl": "/usr/local/bin/old_merged_nodup2pairs.pl", "pairix": "/usr/local/bin/pairix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pygenometracks.
shpc-registry automated BioContainers addition for pygenometracks
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pygenometracks
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pygenometracks:3.8--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pygenometracks/3.8--pyhdfd78af_0
$ module help quay.io/biocontainers/pygenometracks/3.8--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pygenometracks-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pygenometracks-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pygenometracks-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pygenometracks-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pygenometracks-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pygenometracks-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### make_tracks_file

```bash
$ singularity exec <container> /usr/local/bin/make_tracks_file
$ podman run --it --rm --entrypoint /usr/local/bin/make_tracks_file   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_tracks_file   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pgt

```bash
$ singularity exec <container> /usr/local/bin/pgt
$ podman run --it --rm --entrypoint /usr/local/bin/pgt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pgt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyGenomeTracks

```bash
$ singularity exec <container> /usr/local/bin/pyGenomeTracks
$ podman run --it --rm --entrypoint /usr/local/bin/pyGenomeTracks   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyGenomeTracks   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cooler

```bash
$ singularity exec <container> /usr/local/bin/cooler
$ podman run --it --rm --entrypoint /usr/local/bin/cooler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cooler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2pairs

```bash
$ singularity exec <container> /usr/local/bin/bam2pairs
$ podman run --it --rm --entrypoint /usr/local/bin/bam2pairs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2pairs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### column_remover.pl

```bash
$ singularity exec <container> /usr/local/bin/column_remover.pl
$ podman run --it --rm --entrypoint /usr/local/bin/column_remover.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/column_remover.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### duplicate_header_remover.pl

```bash
$ singularity exec <container> /usr/local/bin/duplicate_header_remover.pl
$ podman run --it --rm --entrypoint /usr/local/bin/duplicate_header_remover.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/duplicate_header_remover.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fragment_4dnpairs.pl

```bash
$ singularity exec <container> /usr/local/bin/fragment_4dnpairs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fragment_4dnpairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fragment_4dnpairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### juicer_shortform2pairs.pl

```bash
$ singularity exec <container> /usr/local/bin/juicer_shortform2pairs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/juicer_shortform2pairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/juicer_shortform2pairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merge-pairs.sh

```bash
$ singularity exec <container> /usr/local/bin/merge-pairs.sh
$ podman run --it --rm --entrypoint /usr/local/bin/merge-pairs.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge-pairs.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merged_nodup2pairs.pl

```bash
$ singularity exec <container> /usr/local/bin/merged_nodup2pairs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/merged_nodup2pairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merged_nodup2pairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### old_merged_nodup2pairs.pl

```bash
$ singularity exec <container> /usr/local/bin/old_merged_nodup2pairs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/old_merged_nodup2pairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/old_merged_nodup2pairs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pairix

```bash
$ singularity exec <container> /usr/local/bin/pairix
$ podman run --it --rm --entrypoint /usr/local/bin/pairix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pairix   -v ${PWD} -w ${PWD} <container> -c " $@"
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