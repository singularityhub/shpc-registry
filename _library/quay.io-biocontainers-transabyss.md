---
layout: container
name:  "quay.io/biocontainers/transabyss"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/transabyss/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/transabyss/container.yaml"
updated_at: "2025-04-26 03:27:22.872212"
latest: "2.0.1--pyh864c0ab_7"
container_url: "https://biocontainers.pro/tools/transabyss"
aliases:
 - "abyss-db-csv"
 - "skip_psl_self.awk"
 - "skip_psl_self_ss.awk"
 - "strip_sam_qual.awk"
 - "strip_sam_seq_qual.awk"
 - "strip_sam_seq_qual_noself.awk"
 - "transabyss"
 - "transabyss-merge"
 - "abyss-bloom-dbg"
 - "abyss-bloom-dist.mk.Makefile"
 - "abyss-db-txt"
 - "abyss-dida"
 - "abyss-paired-dbg"
 - "abyss-paired-dbg-mpi"
 - "abyss-pe.Makefile"
 - "abyss-sealer"
 - "ABYSS"
 - "ABYSS-P"
versions:
 - "2.0.1--pyh864c0ab_7"
description: "shpc-registry automated BioContainers addition for transabyss"
config: {"url": "https://biocontainers.pro/tools/transabyss", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for transabyss", "latest": {"2.0.1--pyh864c0ab_7": "sha256:ddd0b0fab398267c0a1257cc36f0d880d72fdaaa59e5113552cb770c812b34f7"}, "tags": {"2.0.1--pyh864c0ab_7": "sha256:ddd0b0fab398267c0a1257cc36f0d880d72fdaaa59e5113552cb770c812b34f7"}, "docker": "quay.io/biocontainers/transabyss", "aliases": {"abyss-db-csv": "/usr/local/bin/abyss-db-csv", "skip_psl_self.awk": "/usr/local/bin/skip_psl_self.awk", "skip_psl_self_ss.awk": "/usr/local/bin/skip_psl_self_ss.awk", "strip_sam_qual.awk": "/usr/local/bin/strip_sam_qual.awk", "strip_sam_seq_qual.awk": "/usr/local/bin/strip_sam_seq_qual.awk", "strip_sam_seq_qual_noself.awk": "/usr/local/bin/strip_sam_seq_qual_noself.awk", "transabyss": "/usr/local/bin/transabyss", "transabyss-merge": "/usr/local/bin/transabyss-merge", "abyss-bloom-dbg": "/usr/local/bin/abyss-bloom-dbg", "abyss-bloom-dist.mk.Makefile": "/usr/local/bin/abyss-bloom-dist.mk.Makefile", "abyss-db-txt": "/usr/local/bin/abyss-db-txt", "abyss-dida": "/usr/local/bin/abyss-dida", "abyss-paired-dbg": "/usr/local/bin/abyss-paired-dbg", "abyss-paired-dbg-mpi": "/usr/local/bin/abyss-paired-dbg-mpi", "abyss-pe.Makefile": "/usr/local/bin/abyss-pe.Makefile", "abyss-sealer": "/usr/local/bin/abyss-sealer", "ABYSS": "/usr/local/bin/ABYSS", "ABYSS-P": "/usr/local/bin/ABYSS-P"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/transabyss.
shpc-registry automated BioContainers addition for transabyss
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/transabyss
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/transabyss:2.0.1--pyh864c0ab_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/transabyss/2.0.1--pyh864c0ab_7
$ module help quay.io/biocontainers/transabyss/2.0.1--pyh864c0ab_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### transabyss-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### transabyss-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### transabyss-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### transabyss-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### transabyss-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### transabyss-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### abyss-db-csv

```bash
$ singularity exec <container> /usr/local/bin/abyss-db-csv
$ podman run --it --rm --entrypoint /usr/local/bin/abyss-db-csv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abyss-db-csv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### skip_psl_self.awk

```bash
$ singularity exec <container> /usr/local/bin/skip_psl_self.awk
$ podman run --it --rm --entrypoint /usr/local/bin/skip_psl_self.awk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/skip_psl_self.awk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### skip_psl_self_ss.awk

```bash
$ singularity exec <container> /usr/local/bin/skip_psl_self_ss.awk
$ podman run --it --rm --entrypoint /usr/local/bin/skip_psl_self_ss.awk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/skip_psl_self_ss.awk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### strip_sam_qual.awk

```bash
$ singularity exec <container> /usr/local/bin/strip_sam_qual.awk
$ podman run --it --rm --entrypoint /usr/local/bin/strip_sam_qual.awk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/strip_sam_qual.awk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### strip_sam_seq_qual.awk

```bash
$ singularity exec <container> /usr/local/bin/strip_sam_seq_qual.awk
$ podman run --it --rm --entrypoint /usr/local/bin/strip_sam_seq_qual.awk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/strip_sam_seq_qual.awk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### strip_sam_seq_qual_noself.awk

```bash
$ singularity exec <container> /usr/local/bin/strip_sam_seq_qual_noself.awk
$ podman run --it --rm --entrypoint /usr/local/bin/strip_sam_seq_qual_noself.awk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/strip_sam_seq_qual_noself.awk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### transabyss

```bash
$ singularity exec <container> /usr/local/bin/transabyss
$ podman run --it --rm --entrypoint /usr/local/bin/transabyss   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/transabyss   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### transabyss-merge

```bash
$ singularity exec <container> /usr/local/bin/transabyss-merge
$ podman run --it --rm --entrypoint /usr/local/bin/transabyss-merge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/transabyss-merge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abyss-bloom-dbg

```bash
$ singularity exec <container> /usr/local/bin/abyss-bloom-dbg
$ podman run --it --rm --entrypoint /usr/local/bin/abyss-bloom-dbg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abyss-bloom-dbg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abyss-bloom-dist.mk.Makefile

```bash
$ singularity exec <container> /usr/local/bin/abyss-bloom-dist.mk.Makefile
$ podman run --it --rm --entrypoint /usr/local/bin/abyss-bloom-dist.mk.Makefile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abyss-bloom-dist.mk.Makefile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abyss-db-txt

```bash
$ singularity exec <container> /usr/local/bin/abyss-db-txt
$ podman run --it --rm --entrypoint /usr/local/bin/abyss-db-txt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abyss-db-txt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abyss-dida

```bash
$ singularity exec <container> /usr/local/bin/abyss-dida
$ podman run --it --rm --entrypoint /usr/local/bin/abyss-dida   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abyss-dida   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abyss-paired-dbg

```bash
$ singularity exec <container> /usr/local/bin/abyss-paired-dbg
$ podman run --it --rm --entrypoint /usr/local/bin/abyss-paired-dbg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abyss-paired-dbg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abyss-paired-dbg-mpi

```bash
$ singularity exec <container> /usr/local/bin/abyss-paired-dbg-mpi
$ podman run --it --rm --entrypoint /usr/local/bin/abyss-paired-dbg-mpi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abyss-paired-dbg-mpi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abyss-pe.Makefile

```bash
$ singularity exec <container> /usr/local/bin/abyss-pe.Makefile
$ podman run --it --rm --entrypoint /usr/local/bin/abyss-pe.Makefile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abyss-pe.Makefile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abyss-sealer

```bash
$ singularity exec <container> /usr/local/bin/abyss-sealer
$ podman run --it --rm --entrypoint /usr/local/bin/abyss-sealer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abyss-sealer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ABYSS

```bash
$ singularity exec <container> /usr/local/bin/ABYSS
$ podman run --it --rm --entrypoint /usr/local/bin/ABYSS   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ABYSS   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ABYSS-P

```bash
$ singularity exec <container> /usr/local/bin/ABYSS-P
$ podman run --it --rm --entrypoint /usr/local/bin/ABYSS-P   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ABYSS-P   -v ${PWD} -w ${PWD} <container> -c " $@"
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