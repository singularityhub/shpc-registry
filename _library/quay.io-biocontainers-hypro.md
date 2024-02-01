---
layout: container
name:  "quay.io/biocontainers/hypro"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hypro/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hypro/container.yaml"
updated_at: "2024-02-01 03:06:23.700245"
latest: "0.1--py_0"
container_url: "https://biocontainers.pro/tools/hypro"
aliases:
 - "hypro.py"
 - "mmseqs2.sh"
 - "fix-sqn-date"
 - "faketime"
 - "real-tbl2asn"
 - "prokka-abricate_to_fasta_db"
 - "prokka"
 - "prokka-biocyc_to_fasta_db"
 - "prokka-build_kingdom_dbs"
 - "prokka-cdd_to_hmm"
 - "prokka-clusters_to_hmm"
 - "prokka-genbank_to_fasta_db"
versions:
 - "0.1--py_0"
description: "shpc-registry automated BioContainers addition for hypro"
config: {"url": "https://biocontainers.pro/tools/hypro", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hypro", "latest": {"0.1--py_0": "sha256:22ca9b67892d4b173666a4819253d34a068dbea4cc601bc702d3cbb52496bca8"}, "tags": {"0.1--py_0": "sha256:22ca9b67892d4b173666a4819253d34a068dbea4cc601bc702d3cbb52496bca8"}, "docker": "quay.io/biocontainers/hypro", "aliases": {"hypro.py": "/usr/local/bin/hypro.py", "mmseqs2.sh": "/usr/local/bin/mmseqs2.sh", "fix-sqn-date": "/usr/local/bin/fix-sqn-date", "faketime": "/usr/local/bin/faketime", "real-tbl2asn": "/usr/local/bin/real-tbl2asn", "prokka-abricate_to_fasta_db": "/usr/local/bin/prokka-abricate_to_fasta_db", "prokka": "/usr/local/bin/prokka", "prokka-biocyc_to_fasta_db": "/usr/local/bin/prokka-biocyc_to_fasta_db", "prokka-build_kingdom_dbs": "/usr/local/bin/prokka-build_kingdom_dbs", "prokka-cdd_to_hmm": "/usr/local/bin/prokka-cdd_to_hmm", "prokka-clusters_to_hmm": "/usr/local/bin/prokka-clusters_to_hmm", "prokka-genbank_to_fasta_db": "/usr/local/bin/prokka-genbank_to_fasta_db"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hypro.
shpc-registry automated BioContainers addition for hypro
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hypro
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hypro:0.1--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hypro/0.1--py_0
$ module help quay.io/biocontainers/hypro/0.1--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hypro-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hypro-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hypro-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hypro-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hypro-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hypro-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hypro.py

```bash
$ singularity exec <container> /usr/local/bin/hypro.py
$ podman run --it --rm --entrypoint /usr/local/bin/hypro.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hypro.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mmseqs2.sh

```bash
$ singularity exec <container> /usr/local/bin/mmseqs2.sh
$ podman run --it --rm --entrypoint /usr/local/bin/mmseqs2.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mmseqs2.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fix-sqn-date

```bash
$ singularity exec <container> /usr/local/bin/fix-sqn-date
$ podman run --it --rm --entrypoint /usr/local/bin/fix-sqn-date   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fix-sqn-date   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### faketime

```bash
$ singularity exec <container> /usr/local/bin/faketime
$ podman run --it --rm --entrypoint /usr/local/bin/faketime   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faketime   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### real-tbl2asn

```bash
$ singularity exec <container> /usr/local/bin/real-tbl2asn
$ podman run --it --rm --entrypoint /usr/local/bin/real-tbl2asn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/real-tbl2asn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prokka-abricate_to_fasta_db

```bash
$ singularity exec <container> /usr/local/bin/prokka-abricate_to_fasta_db
$ podman run --it --rm --entrypoint /usr/local/bin/prokka-abricate_to_fasta_db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prokka-abricate_to_fasta_db   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### prokka-genbank_to_fasta_db

```bash
$ singularity exec <container> /usr/local/bin/prokka-genbank_to_fasta_db
$ podman run --it --rm --entrypoint /usr/local/bin/prokka-genbank_to_fasta_db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prokka-genbank_to_fasta_db   -v ${PWD} -w ${PWD} <container> -c " $@"
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