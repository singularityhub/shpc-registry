---
layout: container
name:  "quay.io/biocontainers/prokka"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/prokka/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/prokka/container.yaml"
updated_at: "2023-12-13 02:58:26.627971"
latest: "1.14.6--pl5321hdfd78af_5"
container_url: "https://biocontainers.pro/tools/prokka"
aliases:
 - "prokka"
 - "prokka-abricate_to_fasta_db"
 - "prokka-biocyc_to_fasta_db"
 - "prokka-build_kingdom_dbs"
 - "prokka-cdd_to_hmm"
 - "prokka-clusters_to_hmm"
 - "prokka-genbank_to_fasta_db"
 - "prokka-genpept_to_fasta_db"
 - "prokka-hamap_to_hmm"
 - "prokka-tigrfams_to_hmm"
 - "prokka-uniprot_to_fasta_db"
 - "tbl2asn-test"
 - "fix-sqn-date"
 - "faketime"
 - "real-tbl2asn"
 - "minced"
 - "tbl2asn"
 - "idn"
 - "aragorn"
 - "barrnap"
 - "bp_aacomp"
 - "bp_bioflat_index"
versions:
 - "1.14.6--pl5321hdfd78af_4"
 - "1.14.6--pl5321hdfd78af_5"
description: "shpc-registry automated BioContainers addition for prokka"
config: {"url": "https://biocontainers.pro/tools/prokka", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for prokka", "latest": {"1.14.6--pl5321hdfd78af_5": "sha256:207b52fbb5580394fbcc1fe58af62bb2fac80ae980d1173384bb2c4feab4bf18"}, "tags": {"1.14.6--pl5321hdfd78af_4": "sha256:d68768c8a51763cb6de66a96e34107874556cee935a70e21c3369680e07b9e14", "1.14.6--pl5321hdfd78af_5": "sha256:207b52fbb5580394fbcc1fe58af62bb2fac80ae980d1173384bb2c4feab4bf18"}, "docker": "quay.io/biocontainers/prokka", "aliases": {"prokka": "/usr/local/bin/prokka", "prokka-abricate_to_fasta_db": "/usr/local/bin/prokka-abricate_to_fasta_db", "prokka-biocyc_to_fasta_db": "/usr/local/bin/prokka-biocyc_to_fasta_db", "prokka-build_kingdom_dbs": "/usr/local/bin/prokka-build_kingdom_dbs", "prokka-cdd_to_hmm": "/usr/local/bin/prokka-cdd_to_hmm", "prokka-clusters_to_hmm": "/usr/local/bin/prokka-clusters_to_hmm", "prokka-genbank_to_fasta_db": "/usr/local/bin/prokka-genbank_to_fasta_db", "prokka-genpept_to_fasta_db": "/usr/local/bin/prokka-genpept_to_fasta_db", "prokka-hamap_to_hmm": "/usr/local/bin/prokka-hamap_to_hmm", "prokka-tigrfams_to_hmm": "/usr/local/bin/prokka-tigrfams_to_hmm", "prokka-uniprot_to_fasta_db": "/usr/local/bin/prokka-uniprot_to_fasta_db", "tbl2asn-test": "/usr/local/bin/tbl2asn-test", "fix-sqn-date": "/usr/local/bin/fix-sqn-date", "faketime": "/usr/local/bin/faketime", "real-tbl2asn": "/usr/local/bin/real-tbl2asn", "minced": "/usr/local/bin/minced", "tbl2asn": "/usr/local/bin/tbl2asn", "idn": "/usr/local/bin/idn", "aragorn": "/usr/local/bin/aragorn", "barrnap": "/usr/local/bin/barrnap", "bp_aacomp": "/usr/local/bin/bp_aacomp", "bp_bioflat_index": "/usr/local/bin/bp_bioflat_index"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/prokka.
shpc-registry automated BioContainers addition for prokka
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/prokka
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/prokka:1.14.6--pl5321hdfd78af_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/prokka/1.14.6--pl5321hdfd78af_5
$ module help quay.io/biocontainers/prokka/1.14.6--pl5321hdfd78af_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### prokka-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### prokka-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### prokka-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### prokka-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### prokka-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### prokka-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### prokka

```bash
$ singularity exec <container> /usr/local/bin/prokka
$ podman run --it --rm --entrypoint /usr/local/bin/prokka   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prokka   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prokka-abricate_to_fasta_db

```bash
$ singularity exec <container> /usr/local/bin/prokka-abricate_to_fasta_db
$ podman run --it --rm --entrypoint /usr/local/bin/prokka-abricate_to_fasta_db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prokka-abricate_to_fasta_db   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### tbl2asn-test

```bash
$ singularity exec <container> /usr/local/bin/tbl2asn-test
$ podman run --it --rm --entrypoint /usr/local/bin/tbl2asn-test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tbl2asn-test   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### minced

```bash
$ singularity exec <container> /usr/local/bin/minced
$ podman run --it --rm --entrypoint /usr/local/bin/minced   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minced   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tbl2asn

```bash
$ singularity exec <container> /usr/local/bin/tbl2asn
$ podman run --it --rm --entrypoint /usr/local/bin/tbl2asn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tbl2asn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idn

```bash
$ singularity exec <container> /usr/local/bin/idn
$ podman run --it --rm --entrypoint /usr/local/bin/idn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aragorn

```bash
$ singularity exec <container> /usr/local/bin/aragorn
$ podman run --it --rm --entrypoint /usr/local/bin/aragorn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aragorn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### barrnap

```bash
$ singularity exec <container> /usr/local/bin/barrnap
$ podman run --it --rm --entrypoint /usr/local/bin/barrnap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/barrnap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_aacomp

```bash
$ singularity exec <container> /usr/local/bin/bp_aacomp
$ podman run --it --rm --entrypoint /usr/local/bin/bp_aacomp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_aacomp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bp_bioflat_index

```bash
$ singularity exec <container> /usr/local/bin/bp_bioflat_index
$ podman run --it --rm --entrypoint /usr/local/bin/bp_bioflat_index   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bp_bioflat_index   -v ${PWD} -w ${PWD} <container> -c " $@"
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