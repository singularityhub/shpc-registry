---
layout: container
name:  "quay.io/biocontainers/magmax"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/magmax/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/magmax/container.yaml"
updated_at: "2025-12-20 03:46:11.057031"
latest: "1.1.0--ha6fb395_0"
container_url: "https://biocontainers.pro/tools/magmax"
aliases:
 - "binspreader"
 - "magmax"
 - "pathracer"
 - "pathracer-seq-fs"
 - "skani"
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
 - "spades-bwa"
 - "spades-core"
 - "spades-corrector-core"
 - "spades-gbuilder"
 - "spades-gmapper"
 - "spades-hammer"
 - "spades-ionhammer"
 - "spades-kmercount"
 - "metaspades.py"
 - "plasmidspades.py"
 - "rnaspades.py"
 - "spades.py"
 - "spades_init.py"
 - "seqtk"
 - "shmemrun"
 - "oshCC"
versions:
 - "1.0.0--ha6fb395_0"
 - "1.1.0--ha6fb395_0"
description: "singularity registry hpc automated addition for magmax"
config: {"url": "https://biocontainers.pro/tools/magmax", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for magmax", "latest": {"1.1.0--ha6fb395_0": "sha256:156eda80fc7120e04a82e78b61de98da367440c04999e2b6d0174bea671a4992"}, "tags": {"1.0.0--ha6fb395_0": "sha256:c20f5a6e0285ca137290c5084c3804c63674772d4d67d159a88c2a31363b1486", "1.1.0--ha6fb395_0": "sha256:156eda80fc7120e04a82e78b61de98da367440c04999e2b6d0174bea671a4992"}, "docker": "quay.io/biocontainers/magmax", "aliases": {"binspreader": "/usr/local/bin/binspreader", "magmax": "/usr/local/bin/magmax", "pathracer": "/usr/local/bin/pathracer", "pathracer-seq-fs": "/usr/local/bin/pathracer-seq-fs", "skani": "/usr/local/bin/skani", "spades-gfa-split": "/usr/local/bin/spades-gfa-split", "spades-hpc": "/usr/local/bin/spades-hpc", "coronaspades.py": "/usr/local/bin/coronaspades.py", "metaplasmidspades.py": "/usr/local/bin/metaplasmidspades.py", "metaviralspades.py": "/usr/local/bin/metaviralspades.py", "rnaviralspades.py": "/usr/local/bin/rnaviralspades.py", "spaligner": "/usr/local/bin/spaligner", "spades-convert-bin-to-fasta": "/usr/local/bin/spades-convert-bin-to-fasta", "spades-gsimplifier": "/usr/local/bin/spades-gsimplifier", "spades-kmer-estimating": "/usr/local/bin/spades-kmer-estimating", "spades-read-filter": "/usr/local/bin/spades-read-filter", "spades-bwa": "/usr/local/bin/spades-bwa", "spades-core": "/usr/local/bin/spades-core", "spades-corrector-core": "/usr/local/bin/spades-corrector-core", "spades-gbuilder": "/usr/local/bin/spades-gbuilder", "spades-gmapper": "/usr/local/bin/spades-gmapper", "spades-hammer": "/usr/local/bin/spades-hammer", "spades-ionhammer": "/usr/local/bin/spades-ionhammer", "spades-kmercount": "/usr/local/bin/spades-kmercount", "metaspades.py": "/usr/local/bin/metaspades.py", "plasmidspades.py": "/usr/local/bin/plasmidspades.py", "rnaspades.py": "/usr/local/bin/rnaspades.py", "spades.py": "/usr/local/bin/spades.py", "spades_init.py": "/usr/local/bin/spades_init.py", "seqtk": "/usr/local/bin/seqtk", "shmemrun": "/usr/local/bin/shmemrun", "oshCC": "/usr/local/bin/oshCC"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/magmax.
singularity registry hpc automated addition for magmax
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/magmax
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/magmax:1.1.0--ha6fb395_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/magmax/1.1.0--ha6fb395_0
$ module help quay.io/biocontainers/magmax/1.1.0--ha6fb395_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### magmax-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### magmax-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### magmax-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### magmax-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### magmax-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### magmax-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### binspreader

```bash
$ singularity exec <container> /usr/local/bin/binspreader
$ podman run --it --rm --entrypoint /usr/local/bin/binspreader   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/binspreader   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### magmax

```bash
$ singularity exec <container> /usr/local/bin/magmax
$ podman run --it --rm --entrypoint /usr/local/bin/magmax   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/magmax   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### skani

```bash
$ singularity exec <container> /usr/local/bin/skani
$ podman run --it --rm --entrypoint /usr/local/bin/skani   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/skani   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### seqtk

```bash
$ singularity exec <container> /usr/local/bin/seqtk
$ podman run --it --rm --entrypoint /usr/local/bin/seqtk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqtk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shmemrun

```bash
$ singularity exec <container> /usr/local/bin/shmemrun
$ podman run --it --rm --entrypoint /usr/local/bin/shmemrun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shmemrun   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oshCC

```bash
$ singularity exec <container> /usr/local/bin/oshCC
$ podman run --it --rm --entrypoint /usr/local/bin/oshCC   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oshCC   -v ${PWD} -w ${PWD} <container> -c " $@"
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