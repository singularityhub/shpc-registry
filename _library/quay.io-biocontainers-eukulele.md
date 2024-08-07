---
layout: container
name:  "quay.io/biocontainers/eukulele"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/eukulele/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/eukulele/container.yaml"
updated_at: "2024-08-07 03:21:04.564421"
latest: "2.0.7--pyh78b79e7_0"
container_url: "https://biocontainers.pro/tools/eukulele"
aliases:
 - "EUKulele"
 - "after_job.sh"
 - "concatenate_busco.sh"
 - "configure_busco.sh"
 - "coordinate_batch.sh"
 - "create_protein_table.py"
 - "download_database.sh"
 - "install_dependencies.sh"
 - "run_busco.sh"
 - "test_pcre"
 - "blastdbcp"
 - "gene_info_reader"
 - "seqdb_demo"
 - "seqdb_perf"
 - "diamond"
 - "seedtop"
 - "idn2"
 - "blast_formatter"
 - "blastdb_aliastool"
versions:
 - "2.0.3--pyh723bec7_0"
 - "2.0.5--pyh723bec7_0"
 - "2.0.7--pyh78b79e7_0"
description: "shpc-registry automated BioContainers addition for eukulele"
config: {"url": "https://biocontainers.pro/tools/eukulele", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for eukulele", "latest": {"2.0.7--pyh78b79e7_0": "sha256:d0e461691d1e923a0172d48f00694141bc6f21cafbfd3ae4a8f4b8efa870bca4"}, "tags": {"2.0.3--pyh723bec7_0": "sha256:7933d7d1a2a15a96aef32fd3c49edecb5a5850de0c344ff3920a06a135267578", "2.0.5--pyh723bec7_0": "sha256:316003c5cb7e632ca43464a578bae5272af27ac966743cf752c46e673242ee4f", "2.0.7--pyh78b79e7_0": "sha256:d0e461691d1e923a0172d48f00694141bc6f21cafbfd3ae4a8f4b8efa870bca4"}, "docker": "quay.io/biocontainers/eukulele", "aliases": {"EUKulele": "/usr/local/bin/EUKulele", "after_job.sh": "/usr/local/bin/after_job.sh", "concatenate_busco.sh": "/usr/local/bin/concatenate_busco.sh", "configure_busco.sh": "/usr/local/bin/configure_busco.sh", "coordinate_batch.sh": "/usr/local/bin/coordinate_batch.sh", "create_protein_table.py": "/usr/local/bin/create_protein_table.py", "download_database.sh": "/usr/local/bin/download_database.sh", "install_dependencies.sh": "/usr/local/bin/install_dependencies.sh", "run_busco.sh": "/usr/local/bin/run_busco.sh", "test_pcre": "/usr/local/bin/test_pcre", "blastdbcp": "/usr/local/bin/blastdbcp", "gene_info_reader": "/usr/local/bin/gene_info_reader", "seqdb_demo": "/usr/local/bin/seqdb_demo", "seqdb_perf": "/usr/local/bin/seqdb_perf", "diamond": "/usr/local/bin/diamond", "seedtop": "/usr/local/bin/seedtop", "idn2": "/usr/local/bin/idn2", "blast_formatter": "/usr/local/bin/blast_formatter", "blastdb_aliastool": "/usr/local/bin/blastdb_aliastool"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/eukulele.
shpc-registry automated BioContainers addition for eukulele
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/eukulele
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/eukulele:2.0.7--pyh78b79e7_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/eukulele/2.0.7--pyh78b79e7_0
$ module help quay.io/biocontainers/eukulele/2.0.7--pyh78b79e7_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### eukulele-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### eukulele-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### eukulele-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### eukulele-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### eukulele-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### eukulele-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### EUKulele

```bash
$ singularity exec <container> /usr/local/bin/EUKulele
$ podman run --it --rm --entrypoint /usr/local/bin/EUKulele   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/EUKulele   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### after_job.sh

```bash
$ singularity exec <container> /usr/local/bin/after_job.sh
$ podman run --it --rm --entrypoint /usr/local/bin/after_job.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/after_job.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### concatenate_busco.sh

```bash
$ singularity exec <container> /usr/local/bin/concatenate_busco.sh
$ podman run --it --rm --entrypoint /usr/local/bin/concatenate_busco.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/concatenate_busco.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### configure_busco.sh

```bash
$ singularity exec <container> /usr/local/bin/configure_busco.sh
$ podman run --it --rm --entrypoint /usr/local/bin/configure_busco.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/configure_busco.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coordinate_batch.sh

```bash
$ singularity exec <container> /usr/local/bin/coordinate_batch.sh
$ podman run --it --rm --entrypoint /usr/local/bin/coordinate_batch.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coordinate_batch.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### create_protein_table.py

```bash
$ singularity exec <container> /usr/local/bin/create_protein_table.py
$ podman run --it --rm --entrypoint /usr/local/bin/create_protein_table.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/create_protein_table.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### download_database.sh

```bash
$ singularity exec <container> /usr/local/bin/download_database.sh
$ podman run --it --rm --entrypoint /usr/local/bin/download_database.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/download_database.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### install_dependencies.sh

```bash
$ singularity exec <container> /usr/local/bin/install_dependencies.sh
$ podman run --it --rm --entrypoint /usr/local/bin/install_dependencies.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/install_dependencies.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_busco.sh

```bash
$ singularity exec <container> /usr/local/bin/run_busco.sh
$ podman run --it --rm --entrypoint /usr/local/bin/run_busco.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_busco.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test_pcre

```bash
$ singularity exec <container> /usr/local/bin/test_pcre
$ podman run --it --rm --entrypoint /usr/local/bin/test_pcre   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test_pcre   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastdbcp

```bash
$ singularity exec <container> /usr/local/bin/blastdbcp
$ podman run --it --rm --entrypoint /usr/local/bin/blastdbcp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastdbcp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gene_info_reader

```bash
$ singularity exec <container> /usr/local/bin/gene_info_reader
$ podman run --it --rm --entrypoint /usr/local/bin/gene_info_reader   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gene_info_reader   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqdb_demo

```bash
$ singularity exec <container> /usr/local/bin/seqdb_demo
$ podman run --it --rm --entrypoint /usr/local/bin/seqdb_demo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqdb_demo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqdb_perf

```bash
$ singularity exec <container> /usr/local/bin/seqdb_perf
$ podman run --it --rm --entrypoint /usr/local/bin/seqdb_perf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqdb_perf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### diamond

```bash
$ singularity exec <container> /usr/local/bin/diamond
$ podman run --it --rm --entrypoint /usr/local/bin/diamond   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/diamond   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seedtop

```bash
$ singularity exec <container> /usr/local/bin/seedtop
$ podman run --it --rm --entrypoint /usr/local/bin/seedtop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seedtop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idn2

```bash
$ singularity exec <container> /usr/local/bin/idn2
$ podman run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast_formatter

```bash
$ singularity exec <container> /usr/local/bin/blast_formatter
$ podman run --it --rm --entrypoint /usr/local/bin/blast_formatter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast_formatter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blastdb_aliastool

```bash
$ singularity exec <container> /usr/local/bin/blastdb_aliastool
$ podman run --it --rm --entrypoint /usr/local/bin/blastdb_aliastool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blastdb_aliastool   -v ${PWD} -w ${PWD} <container> -c " $@"
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