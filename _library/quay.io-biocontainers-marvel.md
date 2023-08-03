---
layout: container
name:  "quay.io/biocontainers/marvel"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/marvel/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/marvel/container.yaml"
updated_at: "2023-08-03 03:58:02.655462"
latest: "0.2--py39hdfd78af_4"
container_url: "https://biocontainers.pro/tools/marvel"
aliases:
 - "download_and_set_models.py"
 - "marvel"
 - "marvel_prokka"
 - "prokka-make_tarball"
 - "prokka"
 - "prokka-biocyc_to_fasta_db"
 - "prokka-build_kingdom_dbs"
 - "prokka-cdd_to_hmm"
 - "prokka-clusters_to_hmm"
 - "prokka-genbank_to_fasta_db"
 - "prokka-genpept_to_fasta_db"
 - "prokka-hamap_to_hmm"
 - "prokka-tigrfams_to_hmm"
 - "prokka-uniprot_to_fasta_db"
versions:
 - "0.2--py39hdfd78af_4"
description: "shpc-registry automated BioContainers addition for marvel"
config: {"url": "https://biocontainers.pro/tools/marvel", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for marvel", "latest": {"0.2--py39hdfd78af_4": "sha256:7a5d333171e7c4ba1be4322deb498abf8c337650928cd7793f85d3c60096666d"}, "tags": {"0.2--py39hdfd78af_4": "sha256:7a5d333171e7c4ba1be4322deb498abf8c337650928cd7793f85d3c60096666d"}, "docker": "quay.io/biocontainers/marvel", "aliases": {"download_and_set_models.py": "/usr/local/bin/download_and_set_models.py", "marvel": "/usr/local/bin/marvel", "marvel_prokka": "/usr/local/bin/marvel_prokka", "prokka-make_tarball": "/usr/local/bin/prokka-make_tarball", "prokka": "/usr/local/bin/prokka", "prokka-biocyc_to_fasta_db": "/usr/local/bin/prokka-biocyc_to_fasta_db", "prokka-build_kingdom_dbs": "/usr/local/bin/prokka-build_kingdom_dbs", "prokka-cdd_to_hmm": "/usr/local/bin/prokka-cdd_to_hmm", "prokka-clusters_to_hmm": "/usr/local/bin/prokka-clusters_to_hmm", "prokka-genbank_to_fasta_db": "/usr/local/bin/prokka-genbank_to_fasta_db", "prokka-genpept_to_fasta_db": "/usr/local/bin/prokka-genpept_to_fasta_db", "prokka-hamap_to_hmm": "/usr/local/bin/prokka-hamap_to_hmm", "prokka-tigrfams_to_hmm": "/usr/local/bin/prokka-tigrfams_to_hmm", "prokka-uniprot_to_fasta_db": "/usr/local/bin/prokka-uniprot_to_fasta_db"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/marvel.
shpc-registry automated BioContainers addition for marvel
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/marvel
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/marvel:0.2--py39hdfd78af_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/marvel/0.2--py39hdfd78af_4
$ module help quay.io/biocontainers/marvel/0.2--py39hdfd78af_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### marvel-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### marvel-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### marvel-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### marvel-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### marvel-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### marvel-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### download_and_set_models.py

```bash
$ singularity exec <container> /usr/local/bin/download_and_set_models.py
$ podman run --it --rm --entrypoint /usr/local/bin/download_and_set_models.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/download_and_set_models.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### marvel

```bash
$ singularity exec <container> /usr/local/bin/marvel
$ podman run --it --rm --entrypoint /usr/local/bin/marvel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/marvel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### marvel_prokka

```bash
$ singularity exec <container> /usr/local/bin/marvel_prokka
$ podman run --it --rm --entrypoint /usr/local/bin/marvel_prokka   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/marvel_prokka   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prokka-make_tarball

```bash
$ singularity exec <container> /usr/local/bin/prokka-make_tarball
$ podman run --it --rm --entrypoint /usr/local/bin/prokka-make_tarball   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prokka-make_tarball   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### prokka-genpept_to_fasta_db

```bash
$ singularity exec <container> /usr/local/bin/prokka-genpept_to_fasta_db
$ podman run --it --rm --entrypoint /usr/local/bin/prokka-genpept_to_fasta_db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prokka-genpept_to_fasta_db   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prokka-hamap_to_hmm

```bash
$ singularity exec <container> /usr/local/bin/prokka-hamap_to_hmm
$ podman run --it --rm --entrypoint /usr/local/bin/prokka-hamap_to_hmm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prokka-hamap_to_hmm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prokka-tigrfams_to_hmm

```bash
$ singularity exec <container> /usr/local/bin/prokka-tigrfams_to_hmm
$ podman run --it --rm --entrypoint /usr/local/bin/prokka-tigrfams_to_hmm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prokka-tigrfams_to_hmm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prokka-uniprot_to_fasta_db

```bash
$ singularity exec <container> /usr/local/bin/prokka-uniprot_to_fasta_db
$ podman run --it --rm --entrypoint /usr/local/bin/prokka-uniprot_to_fasta_db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prokka-uniprot_to_fasta_db   -v ${PWD} -w ${PWD} <container> -c " $@"
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