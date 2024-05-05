---
layout: container
name:  "quay.io/biocontainers/plascope"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/plascope/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/plascope/container.yaml"
updated_at: "2024-05-05 03:00:45.125734"
latest: "1.3.1--hdfd78af_4"
container_url: "https://biocontainers.pro/tools/plascope"
aliases:
 - "centrifuge"
 - "centrifuge-BuildSharedSequence.pl"
 - "centrifuge-RemoveEmptySequence.pl"
 - "centrifuge-RemoveN.pl"
 - "centrifuge-build"
 - "centrifuge-build-bin"
 - "centrifuge-class"
 - "centrifuge-compress.pl"
 - "centrifuge-download"
 - "centrifuge-inspect"
 - "centrifuge-inspect-bin"
 - "centrifuge-kreport"
 - "centrifuge-sort-nt.pl"
 - "centrifuge_evaluate.py"
 - "centrifuge_simulate_reads.py"
 - "plaScope.sh"
 - "cds-mapping-stats"
 - "cds-subgraphs"
 - "mag-improve"
 - "spades-convert-bin-to-fasta"
 - "spades-gsimplifier"
 - "spades-kmer-estimating"
 - "spades-read-filter"
 - "spaligner"
 - "spades-bwa"
 - "spades-core"
versions:
 - "1.3.1--hdfd78af_4"
 - "1.3--1"
description: "shpc-registry automated BioContainers addition for plascope"
config: {"url": "https://biocontainers.pro/tools/plascope", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for plascope", "latest": {"1.3.1--hdfd78af_4": "sha256:83394fc0465c426bc4737c888e0f549682b70d1819a41c468f561b60a71b2943"}, "tags": {"1.3.1--hdfd78af_4": "sha256:83394fc0465c426bc4737c888e0f549682b70d1819a41c468f561b60a71b2943", "1.3--1": "sha256:0d577796cf7808065c09725558459527dc3df1c24dafffe769132d81a4b5b596"}, "docker": "quay.io/biocontainers/plascope", "aliases": {"centrifuge": "/usr/local/bin/centrifuge", "centrifuge-BuildSharedSequence.pl": "/usr/local/bin/centrifuge-BuildSharedSequence.pl", "centrifuge-RemoveEmptySequence.pl": "/usr/local/bin/centrifuge-RemoveEmptySequence.pl", "centrifuge-RemoveN.pl": "/usr/local/bin/centrifuge-RemoveN.pl", "centrifuge-build": "/usr/local/bin/centrifuge-build", "centrifuge-build-bin": "/usr/local/bin/centrifuge-build-bin", "centrifuge-class": "/usr/local/bin/centrifuge-class", "centrifuge-compress.pl": "/usr/local/bin/centrifuge-compress.pl", "centrifuge-download": "/usr/local/bin/centrifuge-download", "centrifuge-inspect": "/usr/local/bin/centrifuge-inspect", "centrifuge-inspect-bin": "/usr/local/bin/centrifuge-inspect-bin", "centrifuge-kreport": "/usr/local/bin/centrifuge-kreport", "centrifuge-sort-nt.pl": "/usr/local/bin/centrifuge-sort-nt.pl", "centrifuge_evaluate.py": "/usr/local/bin/centrifuge_evaluate.py", "centrifuge_simulate_reads.py": "/usr/local/bin/centrifuge_simulate_reads.py", "plaScope.sh": "/usr/local/bin/plaScope.sh", "cds-mapping-stats": "/usr/local/bin/cds-mapping-stats", "cds-subgraphs": "/usr/local/bin/cds-subgraphs", "mag-improve": "/usr/local/bin/mag-improve", "spades-convert-bin-to-fasta": "/usr/local/bin/spades-convert-bin-to-fasta", "spades-gsimplifier": "/usr/local/bin/spades-gsimplifier", "spades-kmer-estimating": "/usr/local/bin/spades-kmer-estimating", "spades-read-filter": "/usr/local/bin/spades-read-filter", "spaligner": "/usr/local/bin/spaligner", "spades-bwa": "/usr/local/bin/spades-bwa", "spades-core": "/usr/local/bin/spades-core"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/plascope.
shpc-registry automated BioContainers addition for plascope
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/plascope
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/plascope:1.3.1--hdfd78af_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/plascope/1.3.1--hdfd78af_4
$ module help quay.io/biocontainers/plascope/1.3.1--hdfd78af_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### plascope-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### plascope-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### plascope-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### plascope-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### plascope-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### plascope-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### centrifuge

```bash
$ singularity exec <container> /usr/local/bin/centrifuge
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-BuildSharedSequence.pl

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-BuildSharedSequence.pl
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-BuildSharedSequence.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-BuildSharedSequence.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-RemoveEmptySequence.pl

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-RemoveEmptySequence.pl
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-RemoveEmptySequence.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-RemoveEmptySequence.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-RemoveN.pl

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-RemoveN.pl
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-RemoveN.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-RemoveN.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-build

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-build
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-build-bin

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-build-bin
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-build-bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-build-bin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-class

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-class
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-class   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-class   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-compress.pl

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-compress.pl
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-compress.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-compress.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-download

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-download
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-download   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-download   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-inspect

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-inspect
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-inspect-bin

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-inspect-bin
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-inspect-bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-inspect-bin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-kreport

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-kreport
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-kreport   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-kreport   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge-sort-nt.pl

```bash
$ singularity exec <container> /usr/local/bin/centrifuge-sort-nt.pl
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge-sort-nt.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge-sort-nt.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge_evaluate.py

```bash
$ singularity exec <container> /usr/local/bin/centrifuge_evaluate.py
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge_evaluate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge_evaluate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrifuge_simulate_reads.py

```bash
$ singularity exec <container> /usr/local/bin/centrifuge_simulate_reads.py
$ podman run --it --rm --entrypoint /usr/local/bin/centrifuge_simulate_reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrifuge_simulate_reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plaScope.sh

```bash
$ singularity exec <container> /usr/local/bin/plaScope.sh
$ podman run --it --rm --entrypoint /usr/local/bin/plaScope.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plaScope.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cds-mapping-stats

```bash
$ singularity exec <container> /usr/local/bin/cds-mapping-stats
$ podman run --it --rm --entrypoint /usr/local/bin/cds-mapping-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cds-mapping-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cds-subgraphs

```bash
$ singularity exec <container> /usr/local/bin/cds-subgraphs
$ podman run --it --rm --entrypoint /usr/local/bin/cds-subgraphs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cds-subgraphs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mag-improve

```bash
$ singularity exec <container> /usr/local/bin/mag-improve
$ podman run --it --rm --entrypoint /usr/local/bin/mag-improve   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mag-improve   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-convert-bin-to-fasta

```bash
$ singularity exec <container> /usr/local/bin/spades-convert-bin-to-fasta
$ podman run --it --rm --entrypoint /usr/local/bin/spades-convert-bin-to-fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-convert-bin-to-fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-gsimplifier

```bash
$ singularity exec <container> /usr/local/bin/spades-gsimplifier
$ podman run --it --rm --entrypoint /usr/local/bin/spades-gsimplifier   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-gsimplifier   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-kmer-estimating

```bash
$ singularity exec <container> /usr/local/bin/spades-kmer-estimating
$ podman run --it --rm --entrypoint /usr/local/bin/spades-kmer-estimating   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-kmer-estimating   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-read-filter

```bash
$ singularity exec <container> /usr/local/bin/spades-read-filter
$ podman run --it --rm --entrypoint /usr/local/bin/spades-read-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-read-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spaligner

```bash
$ singularity exec <container> /usr/local/bin/spaligner
$ podman run --it --rm --entrypoint /usr/local/bin/spaligner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spaligner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-bwa

```bash
$ singularity exec <container> /usr/local/bin/spades-bwa
$ podman run --it --rm --entrypoint /usr/local/bin/spades-bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-core

```bash
$ singularity exec <container> /usr/local/bin/spades-core
$ podman run --it --rm --entrypoint /usr/local/bin/spades-core   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-core   -v ${PWD} -w ${PWD} <container> -c " $@"
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