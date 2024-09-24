---
layout: container
name:  "quay.io/biocontainers/metaclock"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metaclock/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/metaclock/container.yaml"
updated_at: "2024-09-24 03:30:02.815925"
latest: "1.0.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/metaclock"
aliases:
 - "bo6_screen.py"
 - "breadth_depth.py"
 - "consensus.py"
 - "consensus_aDNA.py"
 - "filter.py"
 - "mapDamage"
 - "metaclock_combiner"
 - "metaclock_mac"
 - "metaclock_mac_template_configs"
 - "metaclock_tailor"
 - "metaclock_visualizer"
 - "poly.py"
 - "polymut.py"
 - "prokka-make_tarball"
 - "readal"
 - "statal"
 - "trimal"
 - "filter-table"
 - "spdi2prod"
 - "prokka"
 - "prokka-biocyc_to_fasta_db"
 - "prokka-build_kingdom_dbs"
 - "prokka-cdd_to_hmm"
 - "prokka-clusters_to_hmm"
versions:
 - "1.0.0--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for metaclock"
config: {"url": "https://biocontainers.pro/tools/metaclock", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for metaclock", "latest": {"1.0.0--pyhdfd78af_0": "sha256:3328e51bc1908151a0716e74ec59054b29d118b2b39151ff5aa6f738a56cfb47"}, "tags": {"1.0.0--pyhdfd78af_0": "sha256:3328e51bc1908151a0716e74ec59054b29d118b2b39151ff5aa6f738a56cfb47"}, "docker": "quay.io/biocontainers/metaclock", "aliases": {"bo6_screen.py": "/usr/local/bin/bo6_screen.py", "breadth_depth.py": "/usr/local/bin/breadth_depth.py", "consensus.py": "/usr/local/bin/consensus.py", "consensus_aDNA.py": "/usr/local/bin/consensus_aDNA.py", "filter.py": "/usr/local/bin/filter.py", "mapDamage": "/usr/local/bin/mapDamage", "metaclock_combiner": "/usr/local/bin/metaclock_combiner", "metaclock_mac": "/usr/local/bin/metaclock_mac", "metaclock_mac_template_configs": "/usr/local/bin/metaclock_mac_template_configs", "metaclock_tailor": "/usr/local/bin/metaclock_tailor", "metaclock_visualizer": "/usr/local/bin/metaclock_visualizer", "poly.py": "/usr/local/bin/poly.py", "polymut.py": "/usr/local/bin/polymut.py", "prokka-make_tarball": "/usr/local/bin/prokka-make_tarball", "readal": "/usr/local/bin/readal", "statal": "/usr/local/bin/statal", "trimal": "/usr/local/bin/trimal", "filter-table": "/usr/local/bin/filter-table", "spdi2prod": "/usr/local/bin/spdi2prod", "prokka": "/usr/local/bin/prokka", "prokka-biocyc_to_fasta_db": "/usr/local/bin/prokka-biocyc_to_fasta_db", "prokka-build_kingdom_dbs": "/usr/local/bin/prokka-build_kingdom_dbs", "prokka-cdd_to_hmm": "/usr/local/bin/prokka-cdd_to_hmm", "prokka-clusters_to_hmm": "/usr/local/bin/prokka-clusters_to_hmm"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metaclock.
shpc-registry automated BioContainers addition for metaclock
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metaclock
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metaclock:1.0.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metaclock/1.0.0--pyhdfd78af_0
$ module help quay.io/biocontainers/metaclock/1.0.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metaclock-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metaclock-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metaclock-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metaclock-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metaclock-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metaclock-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bo6_screen.py

```bash
$ singularity exec <container> /usr/local/bin/bo6_screen.py
$ podman run --it --rm --entrypoint /usr/local/bin/bo6_screen.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bo6_screen.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### breadth_depth.py

```bash
$ singularity exec <container> /usr/local/bin/breadth_depth.py
$ podman run --it --rm --entrypoint /usr/local/bin/breadth_depth.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/breadth_depth.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### consensus.py

```bash
$ singularity exec <container> /usr/local/bin/consensus.py
$ podman run --it --rm --entrypoint /usr/local/bin/consensus.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/consensus.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### consensus_aDNA.py

```bash
$ singularity exec <container> /usr/local/bin/consensus_aDNA.py
$ podman run --it --rm --entrypoint /usr/local/bin/consensus_aDNA.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/consensus_aDNA.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter.py

```bash
$ singularity exec <container> /usr/local/bin/filter.py
$ podman run --it --rm --entrypoint /usr/local/bin/filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mapDamage

```bash
$ singularity exec <container> /usr/local/bin/mapDamage
$ podman run --it --rm --entrypoint /usr/local/bin/mapDamage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mapDamage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaclock_combiner

```bash
$ singularity exec <container> /usr/local/bin/metaclock_combiner
$ podman run --it --rm --entrypoint /usr/local/bin/metaclock_combiner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaclock_combiner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaclock_mac

```bash
$ singularity exec <container> /usr/local/bin/metaclock_mac
$ podman run --it --rm --entrypoint /usr/local/bin/metaclock_mac   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaclock_mac   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaclock_mac_template_configs

```bash
$ singularity exec <container> /usr/local/bin/metaclock_mac_template_configs
$ podman run --it --rm --entrypoint /usr/local/bin/metaclock_mac_template_configs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaclock_mac_template_configs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaclock_tailor

```bash
$ singularity exec <container> /usr/local/bin/metaclock_tailor
$ podman run --it --rm --entrypoint /usr/local/bin/metaclock_tailor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaclock_tailor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaclock_visualizer

```bash
$ singularity exec <container> /usr/local/bin/metaclock_visualizer
$ podman run --it --rm --entrypoint /usr/local/bin/metaclock_visualizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaclock_visualizer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### poly.py

```bash
$ singularity exec <container> /usr/local/bin/poly.py
$ podman run --it --rm --entrypoint /usr/local/bin/poly.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/poly.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### polymut.py

```bash
$ singularity exec <container> /usr/local/bin/polymut.py
$ podman run --it --rm --entrypoint /usr/local/bin/polymut.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/polymut.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prokka-make_tarball

```bash
$ singularity exec <container> /usr/local/bin/prokka-make_tarball
$ podman run --it --rm --entrypoint /usr/local/bin/prokka-make_tarball   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prokka-make_tarball   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### readal

```bash
$ singularity exec <container> /usr/local/bin/readal
$ podman run --it --rm --entrypoint /usr/local/bin/readal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/readal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### statal

```bash
$ singularity exec <container> /usr/local/bin/statal
$ podman run --it --rm --entrypoint /usr/local/bin/statal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/statal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trimal

```bash
$ singularity exec <container> /usr/local/bin/trimal
$ podman run --it --rm --entrypoint /usr/local/bin/trimal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trimal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter-table

```bash
$ singularity exec <container> /usr/local/bin/filter-table
$ podman run --it --rm --entrypoint /usr/local/bin/filter-table   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter-table   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spdi2prod

```bash
$ singularity exec <container> /usr/local/bin/spdi2prod
$ podman run --it --rm --entrypoint /usr/local/bin/spdi2prod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spdi2prod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prokka

```bash
$ singularity exec <container> /usr/local/bin/prokka
$ podman run --it --rm --entrypoint /usr/local/bin/prokka   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prokka   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prokka-biocyc_to_fasta_db

```bash
$ singularity exec <container> /usr/local/bin/prokka-biocyc_to_fasta_db
$ podman run --it --rm --entrypoint /usr/local/bin/prokka-biocyc_to_fasta_db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prokka-biocyc_to_fasta_db   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prokka-build_kingdom_dbs

```bash
$ singularity exec <container> /usr/local/bin/prokka-build_kingdom_dbs
$ podman run --it --rm --entrypoint /usr/local/bin/prokka-build_kingdom_dbs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prokka-build_kingdom_dbs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prokka-cdd_to_hmm

```bash
$ singularity exec <container> /usr/local/bin/prokka-cdd_to_hmm
$ podman run --it --rm --entrypoint /usr/local/bin/prokka-cdd_to_hmm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prokka-cdd_to_hmm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prokka-clusters_to_hmm

```bash
$ singularity exec <container> /usr/local/bin/prokka-clusters_to_hmm
$ podman run --it --rm --entrypoint /usr/local/bin/prokka-clusters_to_hmm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prokka-clusters_to_hmm   -v ${PWD} -w ${PWD} <container> -c " $@"
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