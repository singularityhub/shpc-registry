---
layout: container
name:  "quay.io/biocontainers/phantasm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/phantasm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/phantasm/container.yaml"
updated_at: "2024-01-11 03:11:47.151557"
latest: "1.1.3--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/phantasm"
aliases:
 - "average_nucleotide_identity.py"
 - "delta_filter_wrapper.py"
 - "genbank_get_genomes_by_taxon.py"
 - "generax"
 - "phantasm"
 - "pysemver"
 - "xenoGI"
 - "iqtree2"
 - "blastn_vdb"
 - "tblastn_vdb"
 - "iqtree"
 - "pcre2posix_test"
 - "bl2seq"
 - "blastall"
 - "blastclust"
 - "blastpgp"
 - "copymat"
 - "fastacmd"
 - "formatdb"
 - "formatrpsdb"
 - "impala"
 - "makemat"
 - "megablast"
 - "uuid"
 - "uuid-config"
 - "oshCC"
 - "oshc++"
 - "oshcxx"
 - "shmemCC"
 - "shmemc++"
 - "shmemcxx"
 - "oshcc"
versions:
 - "1.1.3--pyhdfd78af_0"
description: "singularity registry hpc automated addition for phantasm"
config: {"url": "https://biocontainers.pro/tools/phantasm", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for phantasm", "latest": {"1.1.3--pyhdfd78af_0": "sha256:4a6c27cfc6cd74d275c582f1e7460f3d2f24529dc30d981fa3b62ad56f9007e7"}, "tags": {"1.1.3--pyhdfd78af_0": "sha256:4a6c27cfc6cd74d275c582f1e7460f3d2f24529dc30d981fa3b62ad56f9007e7"}, "docker": "quay.io/biocontainers/phantasm", "aliases": {"average_nucleotide_identity.py": "/usr/local/bin/average_nucleotide_identity.py", "delta_filter_wrapper.py": "/usr/local/bin/delta_filter_wrapper.py", "genbank_get_genomes_by_taxon.py": "/usr/local/bin/genbank_get_genomes_by_taxon.py", "generax": "/usr/local/bin/generax", "phantasm": "/usr/local/bin/phantasm", "pysemver": "/usr/local/bin/pysemver", "xenoGI": "/usr/local/bin/xenoGI", "iqtree2": "/usr/local/bin/iqtree2", "blastn_vdb": "/usr/local/bin/blastn_vdb", "tblastn_vdb": "/usr/local/bin/tblastn_vdb", "iqtree": "/usr/local/bin/iqtree", "pcre2posix_test": "/usr/local/bin/pcre2posix_test", "bl2seq": "/usr/local/bin/bl2seq", "blastall": "/usr/local/bin/blastall", "blastclust": "/usr/local/bin/blastclust", "blastpgp": "/usr/local/bin/blastpgp", "copymat": "/usr/local/bin/copymat", "fastacmd": "/usr/local/bin/fastacmd", "formatdb": "/usr/local/bin/formatdb", "formatrpsdb": "/usr/local/bin/formatrpsdb", "impala": "/usr/local/bin/impala", "makemat": "/usr/local/bin/makemat", "megablast": "/usr/local/bin/megablast", "uuid": "/usr/local/bin/uuid", "uuid-config": "/usr/local/bin/uuid-config", "oshCC": "/usr/local/bin/oshCC", "oshc++": "/usr/local/bin/oshc++", "oshcxx": "/usr/local/bin/oshcxx", "shmemCC": "/usr/local/bin/shmemCC", "shmemc++": "/usr/local/bin/shmemc++", "shmemcxx": "/usr/local/bin/shmemcxx", "oshcc": "/usr/local/bin/oshcc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/phantasm.
singularity registry hpc automated addition for phantasm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/phantasm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/phantasm:1.1.3--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/phantasm/1.1.3--pyhdfd78af_0
$ module help quay.io/biocontainers/phantasm/1.1.3--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### phantasm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### phantasm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### phantasm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### phantasm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### phantasm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### phantasm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### average_nucleotide_identity.py

```bash
$ singularity exec <container> /usr/local/bin/average_nucleotide_identity.py
$ podman run --it --rm --entrypoint /usr/local/bin/average_nucleotide_identity.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/average_nucleotide_identity.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### delta_filter_wrapper.py

```bash
$ singularity exec <container> /usr/local/bin/delta_filter_wrapper.py
$ podman run --it --rm --entrypoint /usr/local/bin/delta_filter_wrapper.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/delta_filter_wrapper.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genbank_get_genomes_by_taxon.py

```bash
$ singularity exec <container> /usr/local/bin/genbank_get_genomes_by_taxon.py
$ podman run --it --rm --entrypoint /usr/local/bin/genbank_get_genomes_by_taxon.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genbank_get_genomes_by_taxon.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### generax

```bash
$ singularity exec <container> /usr/local/bin/generax
$ podman run --it --rm --entrypoint /usr/local/bin/generax   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/generax   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phantasm

```bash
$ singularity exec <container> /usr/local/bin/phantasm
$ podman run --it --rm --entrypoint /usr/local/bin/phantasm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phantasm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pysemver

```bash
$ singularity exec <container> /usr/local/bin/pysemver
$ podman run --it --rm --entrypoint /usr/local/bin/pysemver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pysemver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xenoGI

```bash
$ singularity exec <container> /usr/local/bin/xenoGI
$ podman run --it --rm --entrypoint /usr/local/bin/xenoGI   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xenoGI   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iqtree2

```bash
$ singularity exec <container> /usr/local/bin/iqtree2
$ podman run --it --rm --entrypoint /usr/local/bin/iqtree2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iqtree2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastn_vdb

```bash
$ singularity exec <container> /usr/local/bin/blastn_vdb
$ podman run --it --rm --entrypoint /usr/local/bin/blastn_vdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastn_vdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tblastn_vdb

```bash
$ singularity exec <container> /usr/local/bin/tblastn_vdb
$ podman run --it --rm --entrypoint /usr/local/bin/tblastn_vdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tblastn_vdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iqtree

```bash
$ singularity exec <container> /usr/local/bin/iqtree
$ podman run --it --rm --entrypoint /usr/local/bin/iqtree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iqtree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pcre2posix_test

```bash
$ singularity exec <container> /usr/local/bin/pcre2posix_test
$ podman run --it --rm --entrypoint /usr/local/bin/pcre2posix_test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pcre2posix_test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bl2seq

```bash
$ singularity exec <container> /usr/local/bin/bl2seq
$ podman run --it --rm --entrypoint /usr/local/bin/bl2seq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bl2seq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastall

```bash
$ singularity exec <container> /usr/local/bin/blastall
$ podman run --it --rm --entrypoint /usr/local/bin/blastall   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastall   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastclust

```bash
$ singularity exec <container> /usr/local/bin/blastclust
$ podman run --it --rm --entrypoint /usr/local/bin/blastclust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastclust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastpgp

```bash
$ singularity exec <container> /usr/local/bin/blastpgp
$ podman run --it --rm --entrypoint /usr/local/bin/blastpgp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastpgp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### copymat

```bash
$ singularity exec <container> /usr/local/bin/copymat
$ podman run --it --rm --entrypoint /usr/local/bin/copymat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/copymat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastacmd

```bash
$ singularity exec <container> /usr/local/bin/fastacmd
$ podman run --it --rm --entrypoint /usr/local/bin/fastacmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastacmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### formatdb

```bash
$ singularity exec <container> /usr/local/bin/formatdb
$ podman run --it --rm --entrypoint /usr/local/bin/formatdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/formatdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### formatrpsdb

```bash
$ singularity exec <container> /usr/local/bin/formatrpsdb
$ podman run --it --rm --entrypoint /usr/local/bin/formatrpsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/formatrpsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### impala

```bash
$ singularity exec <container> /usr/local/bin/impala
$ podman run --it --rm --entrypoint /usr/local/bin/impala   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/impala   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makemat

```bash
$ singularity exec <container> /usr/local/bin/makemat
$ podman run --it --rm --entrypoint /usr/local/bin/makemat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makemat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### megablast

```bash
$ singularity exec <container> /usr/local/bin/megablast
$ podman run --it --rm --entrypoint /usr/local/bin/megablast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/megablast   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uuid

```bash
$ singularity exec <container> /usr/local/bin/uuid
$ podman run --it --rm --entrypoint /usr/local/bin/uuid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uuid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uuid-config

```bash
$ singularity exec <container> /usr/local/bin/uuid-config
$ podman run --it --rm --entrypoint /usr/local/bin/uuid-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uuid-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oshCC

```bash
$ singularity exec <container> /usr/local/bin/oshCC
$ podman run --it --rm --entrypoint /usr/local/bin/oshCC   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oshCC   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oshc++

```bash
$ singularity exec <container> /usr/local/bin/oshc++
$ podman run --it --rm --entrypoint /usr/local/bin/oshc++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oshc++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oshcxx

```bash
$ singularity exec <container> /usr/local/bin/oshcxx
$ podman run --it --rm --entrypoint /usr/local/bin/oshcxx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oshcxx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shmemCC

```bash
$ singularity exec <container> /usr/local/bin/shmemCC
$ podman run --it --rm --entrypoint /usr/local/bin/shmemCC   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shmemCC   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shmemc++

```bash
$ singularity exec <container> /usr/local/bin/shmemc++
$ podman run --it --rm --entrypoint /usr/local/bin/shmemc++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shmemc++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shmemcxx

```bash
$ singularity exec <container> /usr/local/bin/shmemcxx
$ podman run --it --rm --entrypoint /usr/local/bin/shmemcxx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shmemcxx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oshcc

```bash
$ singularity exec <container> /usr/local/bin/oshcc
$ podman run --it --rm --entrypoint /usr/local/bin/oshcc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oshcc   -v ${PWD} -w ${PWD} <container> -c " $@"
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