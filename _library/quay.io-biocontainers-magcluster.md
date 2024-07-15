---
layout: container
name:  "quay.io/biocontainers/magcluster"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/magcluster/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/magcluster/container.yaml"
updated_at: "2024-07-15 02:55:50.236456"
latest: "0.2.5--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/magcluster"
aliases:
 - "clinker"
 - "magcluster"
 - "prokka-make_tarball"
 - "prokka-abricate_to_fasta_db"
 - "prokka"
 - "prokka-biocyc_to_fasta_db"
 - "prokka-build_kingdom_dbs"
 - "prokka-cdd_to_hmm"
 - "prokka-clusters_to_hmm"
 - "prokka-genbank_to_fasta_db"
 - "prokka-genpept_to_fasta_db"
 - "prokka-hamap_to_hmm"
 - "prokka-tigrfams_to_hmm"
versions:
 - "0.2.2--pyhdfd78af_0"
 - "0.2.5--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for magcluster"
config: {"url": "https://biocontainers.pro/tools/magcluster", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for magcluster", "latest": {"0.2.5--pyhdfd78af_0": "sha256:268c4c8f634b86c3d38a13e2e1fa929fa3c53a0daf36d7a57b858827136873db"}, "tags": {"0.2.2--pyhdfd78af_0": "sha256:8b2fc39941c2aa679e313e1061956ddba48d8d89fc5ea294615190349e1fe52d", "0.2.5--pyhdfd78af_0": "sha256:268c4c8f634b86c3d38a13e2e1fa929fa3c53a0daf36d7a57b858827136873db"}, "docker": "quay.io/biocontainers/magcluster", "aliases": {"clinker": "/usr/local/bin/clinker", "magcluster": "/usr/local/bin/magcluster", "prokka-make_tarball": "/usr/local/bin/prokka-make_tarball", "prokka-abricate_to_fasta_db": "/usr/local/bin/prokka-abricate_to_fasta_db", "prokka": "/usr/local/bin/prokka", "prokka-biocyc_to_fasta_db": "/usr/local/bin/prokka-biocyc_to_fasta_db", "prokka-build_kingdom_dbs": "/usr/local/bin/prokka-build_kingdom_dbs", "prokka-cdd_to_hmm": "/usr/local/bin/prokka-cdd_to_hmm", "prokka-clusters_to_hmm": "/usr/local/bin/prokka-clusters_to_hmm", "prokka-genbank_to_fasta_db": "/usr/local/bin/prokka-genbank_to_fasta_db", "prokka-genpept_to_fasta_db": "/usr/local/bin/prokka-genpept_to_fasta_db", "prokka-hamap_to_hmm": "/usr/local/bin/prokka-hamap_to_hmm", "prokka-tigrfams_to_hmm": "/usr/local/bin/prokka-tigrfams_to_hmm"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/magcluster.
shpc-registry automated BioContainers addition for magcluster
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/magcluster
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/magcluster:0.2.5--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/magcluster/0.2.5--pyhdfd78af_0
$ module help quay.io/biocontainers/magcluster/0.2.5--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### magcluster-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### magcluster-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### magcluster-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### magcluster-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### magcluster-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### magcluster-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### clinker

```bash
$ singularity exec <container> /usr/local/bin/clinker
$ podman run --it --rm --entrypoint /usr/local/bin/clinker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clinker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### magcluster

```bash
$ singularity exec <container> /usr/local/bin/magcluster
$ podman run --it --rm --entrypoint /usr/local/bin/magcluster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/magcluster   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prokka-make_tarball

```bash
$ singularity exec <container> /usr/local/bin/prokka-make_tarball
$ podman run --it --rm --entrypoint /usr/local/bin/prokka-make_tarball   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prokka-make_tarball   -v ${PWD} -w ${PWD} <container> -c " $@"
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