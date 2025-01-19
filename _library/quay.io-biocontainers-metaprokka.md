---
layout: container
name:  "quay.io/biocontainers/metaprokka"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metaprokka/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/metaprokka/container.yaml"
updated_at: "2025-01-19 03:40:33.985411"
latest: "1.15.0--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/metaprokka"
aliases:
 - "metaprokka"
 - "tbl2asn-test"
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
 - "1.14.6_1--pl5321hdfd78af_2"
 - "1.15.0--pl5321hdfd78af_0"
 - "1.14.6_1--pl5321hdfd78af_3"
description: "shpc-registry automated BioContainers addition for metaprokka"
config: {"url": "https://biocontainers.pro/tools/metaprokka", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for metaprokka", "latest": {"1.15.0--pl5321hdfd78af_0": "sha256:1a900076d10232daee13c215a31b4a5a15e705e573df5ee66126e4aed1f314c6"}, "tags": {"1.14.6_1--pl5321hdfd78af_2": "sha256:27ae7fd133dbeb44836f1452e328a6a7b108f0e2b97851fa055c72c9068c550e", "1.15.0--pl5321hdfd78af_0": "sha256:1a900076d10232daee13c215a31b4a5a15e705e573df5ee66126e4aed1f314c6", "1.14.6_1--pl5321hdfd78af_3": "sha256:e70b9cb26d25edea065fa5ce828fb6a4f0ec4890c8bd34102dcccf08c07b9933"}, "docker": "quay.io/biocontainers/metaprokka", "aliases": {"metaprokka": "/usr/local/bin/metaprokka", "tbl2asn-test": "/usr/local/bin/tbl2asn-test", "fix-sqn-date": "/usr/local/bin/fix-sqn-date", "faketime": "/usr/local/bin/faketime", "real-tbl2asn": "/usr/local/bin/real-tbl2asn", "prokka-abricate_to_fasta_db": "/usr/local/bin/prokka-abricate_to_fasta_db", "prokka": "/usr/local/bin/prokka", "prokka-biocyc_to_fasta_db": "/usr/local/bin/prokka-biocyc_to_fasta_db", "prokka-build_kingdom_dbs": "/usr/local/bin/prokka-build_kingdom_dbs", "prokka-cdd_to_hmm": "/usr/local/bin/prokka-cdd_to_hmm", "prokka-clusters_to_hmm": "/usr/local/bin/prokka-clusters_to_hmm", "prokka-genbank_to_fasta_db": "/usr/local/bin/prokka-genbank_to_fasta_db"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metaprokka.
shpc-registry automated BioContainers addition for metaprokka
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metaprokka
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metaprokka:1.15.0--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metaprokka/1.15.0--pl5321hdfd78af_0
$ module help quay.io/biocontainers/metaprokka/1.15.0--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metaprokka-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metaprokka-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metaprokka-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metaprokka-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metaprokka-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metaprokka-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### metaprokka

```bash
$ singularity exec <container> /usr/local/bin/metaprokka
$ podman run --it --rm --entrypoint /usr/local/bin/metaprokka   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaprokka   -v ${PWD} -w ${PWD} <container> -c " $@"
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