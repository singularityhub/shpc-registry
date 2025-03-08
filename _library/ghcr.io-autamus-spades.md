---
layout: container
name:  "ghcr.io/autamus/spades"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/spades/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/spades/container.yaml"
updated_at: "2025-03-08 03:20:10.991242"
latest: "3.15.3"
container_url: "https://github.com/orgs/autamus/packages/container/package/spades"
aliases:
 - "spades-bwa"
 - "spades-convert-bin-to-fasta"
 - "spades-core"
 - "spades-corrector-core"
 - "spades-gbuilder"
 - "spades-gmapper"
 - "spades-gsimplifier"
 - "spades-hammer"
 - "spades-ionhammer"
 - "spades-kmer-estimating"
 - "spades-kmercount"
 - "spades-read-filter"
 - "spades-truseq-scfcorrection"
 - "spades.py"
 - "spaligner"
versions:
 - "3.15.2"
 - "3.15.3"
 - "latest"
 - "3.15.5"
description: "St. Petersburg genome assembler – an assembly toolkit containing various assembly pipelines."
config: {"docker": "ghcr.io/autamus/spades", "url": "https://github.com/orgs/autamus/packages/container/package/spades", "maintainer": "@vsoch", "description": "St. Petersburg genome assembler \u2013 an assembly toolkit containing various assembly pipelines.", "latest": {"3.15.3": "sha256:a225a30c5d2861784184b59149e75d1b5b0594827a4d03e23aa246ea980130e7"}, "tags": {"3.15.2": "sha256:f93ed1e3cff94d5db0e8ab238fc2287222536763bd2f5471a5cf8580cea963cf", "3.15.3": "sha256:a225a30c5d2861784184b59149e75d1b5b0594827a4d03e23aa246ea980130e7", "latest": "sha256:32dc7c7cf7a2940cfc664bcb74e6a6c4e387fb2ecc4b6bf81c1a3f8c976329db", "3.15.5": "sha256:32dc7c7cf7a2940cfc664bcb74e6a6c4e387fb2ecc4b6bf81c1a3f8c976329db"}, "aliases": {"spades-bwa": "/opt/view/bin/spades-bwa", "spades-convert-bin-to-fasta": "/opt/view/bin/spades-convert-bin-to-fasta", "spades-core": "/opt/view/bin/spades-core", "spades-corrector-core": "/opt/view/bin/spades-corrector-core", "spades-gbuilder": "/opt/view/bin/spades-gbuilder", "spades-gmapper": "/opt/view/bin/spades-gmapper", "spades-gsimplifier": "/opt/view/bin/spades-gsimplifier", "spades-hammer": "/opt/view/bin/spades-hammer", "spades-ionhammer": "/opt/view/bin/spades-ionhammer", "spades-kmer-estimating": "/opt/view/bin/spades-kmer-estimating", "spades-kmercount": "/opt/view/bin/spades-kmercount", "spades-read-filter": "/opt/view/bin/spades-read-filter", "spades-truseq-scfcorrection": "/opt/view/bin/spades-truseq-scfcorrection", "spades.py": "/opt/view/bin/spades.py", "spaligner": "/opt/view/bin/spaligner"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/spades.
St. Petersburg genome assembler – an assembly toolkit containing various assembly pipelines.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/spades
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/spades:3.15.3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/spades/3.15.3
$ module help ghcr.io/autamus/spades/3.15.3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### spades-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### spades-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### spades-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### spades-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### spades-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### spades-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### spades-bwa

```bash
$ singularity exec <container> /opt/view/bin/spades-bwa
$ podman run --it --rm --entrypoint /opt/view/bin/spades-bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/spades-bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-convert-bin-to-fasta

```bash
$ singularity exec <container> /opt/view/bin/spades-convert-bin-to-fasta
$ podman run --it --rm --entrypoint /opt/view/bin/spades-convert-bin-to-fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/spades-convert-bin-to-fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-core

```bash
$ singularity exec <container> /opt/view/bin/spades-core
$ podman run --it --rm --entrypoint /opt/view/bin/spades-core   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/spades-core   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-corrector-core

```bash
$ singularity exec <container> /opt/view/bin/spades-corrector-core
$ podman run --it --rm --entrypoint /opt/view/bin/spades-corrector-core   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/spades-corrector-core   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-gbuilder

```bash
$ singularity exec <container> /opt/view/bin/spades-gbuilder
$ podman run --it --rm --entrypoint /opt/view/bin/spades-gbuilder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/spades-gbuilder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-gmapper

```bash
$ singularity exec <container> /opt/view/bin/spades-gmapper
$ podman run --it --rm --entrypoint /opt/view/bin/spades-gmapper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/spades-gmapper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-gsimplifier

```bash
$ singularity exec <container> /opt/view/bin/spades-gsimplifier
$ podman run --it --rm --entrypoint /opt/view/bin/spades-gsimplifier   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/spades-gsimplifier   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-hammer

```bash
$ singularity exec <container> /opt/view/bin/spades-hammer
$ podman run --it --rm --entrypoint /opt/view/bin/spades-hammer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/spades-hammer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-ionhammer

```bash
$ singularity exec <container> /opt/view/bin/spades-ionhammer
$ podman run --it --rm --entrypoint /opt/view/bin/spades-ionhammer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/spades-ionhammer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-kmer-estimating

```bash
$ singularity exec <container> /opt/view/bin/spades-kmer-estimating
$ podman run --it --rm --entrypoint /opt/view/bin/spades-kmer-estimating   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/spades-kmer-estimating   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-kmercount

```bash
$ singularity exec <container> /opt/view/bin/spades-kmercount
$ podman run --it --rm --entrypoint /opt/view/bin/spades-kmercount   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/spades-kmercount   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-read-filter

```bash
$ singularity exec <container> /opt/view/bin/spades-read-filter
$ podman run --it --rm --entrypoint /opt/view/bin/spades-read-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/spades-read-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-truseq-scfcorrection

```bash
$ singularity exec <container> /opt/view/bin/spades-truseq-scfcorrection
$ podman run --it --rm --entrypoint /opt/view/bin/spades-truseq-scfcorrection   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/spades-truseq-scfcorrection   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades.py

```bash
$ singularity exec <container> /opt/view/bin/spades.py
$ podman run --it --rm --entrypoint /opt/view/bin/spades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/spades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spaligner

```bash
$ singularity exec <container> /opt/view/bin/spaligner
$ podman run --it --rm --entrypoint /opt/view/bin/spaligner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/spaligner   -v ${PWD} -w ${PWD} <container> -c " $@"
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