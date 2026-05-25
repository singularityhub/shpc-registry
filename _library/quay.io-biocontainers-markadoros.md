---
layout: container
name:  "quay.io/biocontainers/markadoros"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/markadoros/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/markadoros/container.yaml"
updated_at: "2026-05-25 07:24:33.172129"
latest: "1.1.0--pyh106432d_0"
container_url: "https://biocontainers.pro/tools/markadoros"
aliases:
 - "binspreader"
 - "hifiasm"
 - "markadoros"
 - "pathracer"
 - "pathracer-seq-fs"
 - "spades-gfa-split"
 - "spades-hpc"
 - "coronaspades.py"
 - "metaplasmidspades.py"
 - "metaviralspades.py"
 - "rnaviralspades.py"
 - "spaligner"
 - "spades-convert-bin-to-fasta"
 - "spades-gsimplifier"
 - "spades-kmer-estimating"
 - "spades-read-filter"
 - "aria2c"
 - "spades-bwa"
 - "spades-core"
 - "spades-corrector-core"
 - "spades-gbuilder"
 - "spades-gmapper"
 - "spades-hammer"
 - "spades-ionhammer"
 - "spades-kmercount"
 - "gawk-5.3.1"
 - "metaspades.py"
 - "plasmidspades.py"
 - "rnaspades.py"
 - "spades.py"
 - "spades_init.py"
 - "mmseqs"
versions:
 - "1.0.0--pyh106432d_0"
 - "1.1.0--pyh106432d_0"
description: "singularity registry hpc automated addition for markadoros"
config: {"url": "https://biocontainers.pro/tools/markadoros", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for markadoros", "latest": {"1.1.0--pyh106432d_0": "sha256:5b935212f92675e8252a5caa922f2cca15796a4046bbb850848b52a72bfa0244"}, "tags": {"1.0.0--pyh106432d_0": "sha256:72ab85e586102803c1d43660427945b965b385e042aa7b3e432266ceb0f6e1c5", "1.1.0--pyh106432d_0": "sha256:5b935212f92675e8252a5caa922f2cca15796a4046bbb850848b52a72bfa0244"}, "docker": "quay.io/biocontainers/markadoros", "aliases": {"binspreader": "/usr/local/bin/binspreader", "hifiasm": "/usr/local/bin/hifiasm", "markadoros": "/usr/local/bin/markadoros", "pathracer": "/usr/local/bin/pathracer", "pathracer-seq-fs": "/usr/local/bin/pathracer-seq-fs", "spades-gfa-split": "/usr/local/bin/spades-gfa-split", "spades-hpc": "/usr/local/bin/spades-hpc", "coronaspades.py": "/usr/local/bin/coronaspades.py", "metaplasmidspades.py": "/usr/local/bin/metaplasmidspades.py", "metaviralspades.py": "/usr/local/bin/metaviralspades.py", "rnaviralspades.py": "/usr/local/bin/rnaviralspades.py", "spaligner": "/usr/local/bin/spaligner", "spades-convert-bin-to-fasta": "/usr/local/bin/spades-convert-bin-to-fasta", "spades-gsimplifier": "/usr/local/bin/spades-gsimplifier", "spades-kmer-estimating": "/usr/local/bin/spades-kmer-estimating", "spades-read-filter": "/usr/local/bin/spades-read-filter", "aria2c": "/usr/local/bin/aria2c", "spades-bwa": "/usr/local/bin/spades-bwa", "spades-core": "/usr/local/bin/spades-core", "spades-corrector-core": "/usr/local/bin/spades-corrector-core", "spades-gbuilder": "/usr/local/bin/spades-gbuilder", "spades-gmapper": "/usr/local/bin/spades-gmapper", "spades-hammer": "/usr/local/bin/spades-hammer", "spades-ionhammer": "/usr/local/bin/spades-ionhammer", "spades-kmercount": "/usr/local/bin/spades-kmercount", "gawk-5.3.1": "/usr/local/bin/gawk-5.3.1", "metaspades.py": "/usr/local/bin/metaspades.py", "plasmidspades.py": "/usr/local/bin/plasmidspades.py", "rnaspades.py": "/usr/local/bin/rnaspades.py", "spades.py": "/usr/local/bin/spades.py", "spades_init.py": "/usr/local/bin/spades_init.py", "mmseqs": "/usr/local/bin/mmseqs"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/markadoros.
singularity registry hpc automated addition for markadoros
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/markadoros
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/markadoros:1.1.0--pyh106432d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/markadoros/1.1.0--pyh106432d_0
$ module help quay.io/biocontainers/markadoros/1.1.0--pyh106432d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### markadoros-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### markadoros-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### markadoros-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### markadoros-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### markadoros-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### markadoros-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### binspreader

```bash
$ singularity exec <container> /usr/local/bin/binspreader
$ podman run --it --rm --entrypoint /usr/local/bin/binspreader   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/binspreader   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hifiasm

```bash
$ singularity exec <container> /usr/local/bin/hifiasm
$ podman run --it --rm --entrypoint /usr/local/bin/hifiasm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hifiasm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### markadoros

```bash
$ singularity exec <container> /usr/local/bin/markadoros
$ podman run --it --rm --entrypoint /usr/local/bin/markadoros   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/markadoros   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pathracer

```bash
$ singularity exec <container> /usr/local/bin/pathracer
$ podman run --it --rm --entrypoint /usr/local/bin/pathracer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pathracer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pathracer-seq-fs

```bash
$ singularity exec <container> /usr/local/bin/pathracer-seq-fs
$ podman run --it --rm --entrypoint /usr/local/bin/pathracer-seq-fs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pathracer-seq-fs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-gfa-split

```bash
$ singularity exec <container> /usr/local/bin/spades-gfa-split
$ podman run --it --rm --entrypoint /usr/local/bin/spades-gfa-split   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-gfa-split   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-hpc

```bash
$ singularity exec <container> /usr/local/bin/spades-hpc
$ podman run --it --rm --entrypoint /usr/local/bin/spades-hpc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-hpc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coronaspades.py

```bash
$ singularity exec <container> /usr/local/bin/coronaspades.py
$ podman run --it --rm --entrypoint /usr/local/bin/coronaspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coronaspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaplasmidspades.py

```bash
$ singularity exec <container> /usr/local/bin/metaplasmidspades.py
$ podman run --it --rm --entrypoint /usr/local/bin/metaplasmidspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaplasmidspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaviralspades.py

```bash
$ singularity exec <container> /usr/local/bin/metaviralspades.py
$ podman run --it --rm --entrypoint /usr/local/bin/metaviralspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaviralspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rnaviralspades.py

```bash
$ singularity exec <container> /usr/local/bin/rnaviralspades.py
$ podman run --it --rm --entrypoint /usr/local/bin/rnaviralspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rnaviralspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spaligner

```bash
$ singularity exec <container> /usr/local/bin/spaligner
$ podman run --it --rm --entrypoint /usr/local/bin/spaligner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spaligner   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### aria2c

```bash
$ singularity exec <container> /usr/local/bin/aria2c
$ podman run --it --rm --entrypoint /usr/local/bin/aria2c   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aria2c   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### spades-corrector-core

```bash
$ singularity exec <container> /usr/local/bin/spades-corrector-core
$ podman run --it --rm --entrypoint /usr/local/bin/spades-corrector-core   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-corrector-core   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-gbuilder

```bash
$ singularity exec <container> /usr/local/bin/spades-gbuilder
$ podman run --it --rm --entrypoint /usr/local/bin/spades-gbuilder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-gbuilder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-gmapper

```bash
$ singularity exec <container> /usr/local/bin/spades-gmapper
$ podman run --it --rm --entrypoint /usr/local/bin/spades-gmapper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-gmapper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-hammer

```bash
$ singularity exec <container> /usr/local/bin/spades-hammer
$ podman run --it --rm --entrypoint /usr/local/bin/spades-hammer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-hammer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-ionhammer

```bash
$ singularity exec <container> /usr/local/bin/spades-ionhammer
$ podman run --it --rm --entrypoint /usr/local/bin/spades-ionhammer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-ionhammer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades-kmercount

```bash
$ singularity exec <container> /usr/local/bin/spades-kmercount
$ podman run --it --rm --entrypoint /usr/local/bin/spades-kmercount   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades-kmercount   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk-5.3.1

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.3.1
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaspades.py

```bash
$ singularity exec <container> /usr/local/bin/metaspades.py
$ podman run --it --rm --entrypoint /usr/local/bin/metaspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plasmidspades.py

```bash
$ singularity exec <container> /usr/local/bin/plasmidspades.py
$ podman run --it --rm --entrypoint /usr/local/bin/plasmidspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plasmidspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rnaspades.py

```bash
$ singularity exec <container> /usr/local/bin/rnaspades.py
$ podman run --it --rm --entrypoint /usr/local/bin/rnaspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rnaspades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades.py

```bash
$ singularity exec <container> /usr/local/bin/spades.py
$ podman run --it --rm --entrypoint /usr/local/bin/spades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spades_init.py

```bash
$ singularity exec <container> /usr/local/bin/spades_init.py
$ podman run --it --rm --entrypoint /usr/local/bin/spades_init.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spades_init.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mmseqs

```bash
$ singularity exec <container> /usr/local/bin/mmseqs
$ podman run --it --rm --entrypoint /usr/local/bin/mmseqs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mmseqs   -v ${PWD} -w ${PWD} <container> -c " $@"
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