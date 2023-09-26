---
layout: container
name:  "quay.io/biocontainers/probeit"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/probeit/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/probeit/container.yaml"
updated_at: "2023-09-26 03:13:46.148787"
latest: "2.2--py38hcbe9525_2"
container_url: "https://biocontainers.pro/tools/probeit"
aliases:
 - "genmap"
 - "probeit"
 - "setcover"
 - "seqkit"
 - "mmseqs"
 - "gawk-5.1.0"
 - "awk"
 - "gawk"
 - "idn2"
 - "shiftBed"
 - "annotateBed"
 - "bamToBed"
 - "bamToFastq"
versions:
 - "v1.9--py38hc37a69a_1"
 - "2.2--py38h8ded8fe_1"
 - "2.0--py27h304d29a_0"
 - "2.2--py38hcbe9525_2"
description: "shpc-registry automated BioContainers addition for probeit"
config: {"url": "https://biocontainers.pro/tools/probeit", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for probeit", "latest": {"2.2--py38hcbe9525_2": "sha256:082267955930a425b7a16f241e8d1c310bd6a9a1035187def52024c1f0980465"}, "tags": {"v1.9--py38hc37a69a_1": "sha256:a6f818dede4e5c1528dfaef296dcad730de61579254380369f2e8abc148e3dc4", "2.2--py38h8ded8fe_1": "sha256:e26ae46557525d14b86447cd9f68d25a3e8173ff7d1693020220f0be59b5c30c", "2.0--py27h304d29a_0": "sha256:c4968c0ac245eaea703feef94f1fec3ae96be982640ce194e0852a63ac785ef2", "2.2--py38hcbe9525_2": "sha256:082267955930a425b7a16f241e8d1c310bd6a9a1035187def52024c1f0980465"}, "docker": "quay.io/biocontainers/probeit", "aliases": {"genmap": "/usr/local/bin/genmap", "probeit": "/usr/local/bin/probeit", "setcover": "/usr/local/bin/setcover", "seqkit": "/usr/local/bin/seqkit", "mmseqs": "/usr/local/bin/mmseqs", "gawk-5.1.0": "/usr/local/bin/gawk-5.1.0", "awk": "/usr/local/bin/awk", "gawk": "/usr/local/bin/gawk", "idn2": "/usr/local/bin/idn2", "shiftBed": "/usr/local/bin/shiftBed", "annotateBed": "/usr/local/bin/annotateBed", "bamToBed": "/usr/local/bin/bamToBed", "bamToFastq": "/usr/local/bin/bamToFastq"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/probeit.
shpc-registry automated BioContainers addition for probeit
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/probeit
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/probeit:2.2--py38hcbe9525_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/probeit/2.2--py38hcbe9525_2
$ module help quay.io/biocontainers/probeit/2.2--py38hcbe9525_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### probeit-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### probeit-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### probeit-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### probeit-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### probeit-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### probeit-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### genmap

```bash
$ singularity exec <container> /usr/local/bin/genmap
$ podman run --it --rm --entrypoint /usr/local/bin/genmap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genmap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### probeit

```bash
$ singularity exec <container> /usr/local/bin/probeit
$ podman run --it --rm --entrypoint /usr/local/bin/probeit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/probeit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### setcover

```bash
$ singularity exec <container> /usr/local/bin/setcover
$ podman run --it --rm --entrypoint /usr/local/bin/setcover   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/setcover   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqkit

```bash
$ singularity exec <container> /usr/local/bin/seqkit
$ podman run --it --rm --entrypoint /usr/local/bin/seqkit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqkit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mmseqs

```bash
$ singularity exec <container> /usr/local/bin/mmseqs
$ podman run --it --rm --entrypoint /usr/local/bin/mmseqs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mmseqs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk-5.1.0

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.1.0
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### awk

```bash
$ singularity exec <container> /usr/local/bin/awk
$ podman run --it --rm --entrypoint /usr/local/bin/awk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/awk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk

```bash
$ singularity exec <container> /usr/local/bin/gawk
$ podman run --it --rm --entrypoint /usr/local/bin/gawk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idn2

```bash
$ singularity exec <container> /usr/local/bin/idn2
$ podman run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shiftBed

```bash
$ singularity exec <container> /usr/local/bin/shiftBed
$ podman run --it --rm --entrypoint /usr/local/bin/shiftBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shiftBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotateBed

```bash
$ singularity exec <container> /usr/local/bin/annotateBed
$ podman run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamToBed

```bash
$ singularity exec <container> /usr/local/bin/bamToBed
$ podman run --it --rm --entrypoint /usr/local/bin/bamToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamToFastq

```bash
$ singularity exec <container> /usr/local/bin/bamToFastq
$ podman run --it --rm --entrypoint /usr/local/bin/bamToFastq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamToFastq   -v ${PWD} -w ${PWD} <container> -c " $@"
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