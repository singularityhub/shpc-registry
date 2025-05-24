---
layout: container
name:  "quay.io/biocontainers/pairix"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pairix/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pairix/container.yaml"
updated_at: "2025-05-24 03:48:50.819306"
latest: "0.3.9--py312h4711d71_0"
container_url: "https://biocontainers.pro/tools/pairix"
aliases:
 - "pairix"
 - "bam2pairs"
 - "column_remover.pl"
 - "duplicate_header_remover.pl"
 - "fragment_4dnpairs.pl"
 - "juicer_shortform2pairs.pl"
 - "merge-pairs.sh"
 - "merged_nodup2pairs.pl"
 - "old_merged_nodup2pairs.pl"
 - "pairs_merger"
 - "process_merged_nodup.sh"
versions:
 - "0.3.7--py36haf49e46_4"
 - "0.3.8--py39h3d4b85c_0"
 - "0.3.8--py38h7cf9df2_1"
 - "0.3.8--py39he47c912_2"
 - "0.3.8--py312he57d009_3"
 - "0.3.9--py312h4711d71_0"
description: "shpc-registry automated BioContainers addition for pairix"
config: {"url": "https://biocontainers.pro/tools/pairix", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pairix", "latest": {"0.3.9--py312h4711d71_0": "sha256:035bf01da9f15bb3308547270fa220b59edb8c41e5040779ba0c2ead63b48587"}, "tags": {"0.3.7--py36haf49e46_4": "sha256:beeb156ca2c238c3c6b602f20e75bda97b1866df449fcf0f9a552088b6240fa1", "0.3.8--py39h3d4b85c_0": "sha256:0419eda169a05b2e752da4025cbfe157585864cc705def7ac9d34e76e8370ce7", "0.3.8--py38h7cf9df2_1": "sha256:23e60640106eb04aafd8e82667b7b928702d603408b71c435f1d90e9fdfd9552", "0.3.8--py39he47c912_2": "sha256:8f2fa08ef6b9ba101354d91a490055c6325efafae963e3bc477c4bae0f249796", "0.3.8--py312he57d009_3": "sha256:1e5949b98c1a9029268f3f743924d4e5e7ad11daa12d7822c7216b79537b9d1f", "0.3.9--py312h4711d71_0": "sha256:035bf01da9f15bb3308547270fa220b59edb8c41e5040779ba0c2ead63b48587"}, "docker": "quay.io/biocontainers/pairix", "aliases": {"pairix": "/usr/local/bin/pairix", "bam2pairs": "/usr/local/bin/bam2pairs", "column_remover.pl": "/usr/local/bin/column_remover.pl", "duplicate_header_remover.pl": "/usr/local/bin/duplicate_header_remover.pl", "fragment_4dnpairs.pl": "/usr/local/bin/fragment_4dnpairs.pl", "juicer_shortform2pairs.pl": "/usr/local/bin/juicer_shortform2pairs.pl", "merge-pairs.sh": "/usr/local/bin/merge-pairs.sh", "merged_nodup2pairs.pl": "/usr/local/bin/merged_nodup2pairs.pl", "old_merged_nodup2pairs.pl": "/usr/local/bin/old_merged_nodup2pairs.pl", "pairs_merger": "/usr/local/bin/pairs_merger", "process_merged_nodup.sh": "/usr/local/bin/process_merged_nodup.sh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pairix.
shpc-registry automated BioContainers addition for pairix
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pairix
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pairix:0.3.9--py312h4711d71_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pairix/0.3.9--py312h4711d71_0
$ module help quay.io/biocontainers/pairix/0.3.9--py312h4711d71_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pairix-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pairix-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pairix-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pairix-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pairix-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pairix-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pairix

```bash
$ singularity exec <container> /usr/local/bin/pairix
$ podman run --it --rm --entrypoint /usr/local/bin/pairix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pairix   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### pairs_merger

```bash
$ singularity exec <container> /usr/local/bin/pairs_merger
$ podman run --it --rm --entrypoint /usr/local/bin/pairs_merger   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pairs_merger   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### process_merged_nodup.sh

```bash
$ singularity exec <container> /usr/local/bin/process_merged_nodup.sh
$ podman run --it --rm --entrypoint /usr/local/bin/process_merged_nodup.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/process_merged_nodup.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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