---
layout: container
name:  "quay.io/biocontainers/chewiesnake"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/chewiesnake/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/chewiesnake/container.yaml"
updated_at: "2023-07-05 03:34:31.259973"
latest: "3.0.0--hdfd78af_2"
container_url: "https://biocontainers.pro/tools/chewiesnake"
aliases:
 - "Clustering_DistanceMatrix.R"
 - "alleleprofile_hasher.py"
 - "chewBBACA.py"
 - "chewie"
 - "chewiesnake"
 - "chewiesnake_join"
 - "create_alleledbSheet.sh"
 - "create_sampleSheet.sh"
 - "grapetree"
 - "hashID.py"
 - "lighter"
 - "shovill"
 - "skesa"
 - "stone"
 - "megahit_core"
 - "megahit_core_no_hw_accel"
 - "megahit_core_popcnt"
 - "fastp"
 - "flash"
 - "megahit"
 - "megahit_toolkit"
 - "pilon"
 - "unidecode"
versions:
 - "3.0.0--hdfd78af_2"
description: "shpc-registry automated BioContainers addition for chewiesnake"
config: {"url": "https://biocontainers.pro/tools/chewiesnake", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for chewiesnake", "latest": {"3.0.0--hdfd78af_2": "sha256:62ec678ea64f72d175cb829038c34aa9910beddc663adbdbfaf8959e5f385575"}, "tags": {"3.0.0--hdfd78af_2": "sha256:62ec678ea64f72d175cb829038c34aa9910beddc663adbdbfaf8959e5f385575"}, "docker": "quay.io/biocontainers/chewiesnake", "aliases": {"Clustering_DistanceMatrix.R": "/usr/local/bin/Clustering_DistanceMatrix.R", "alleleprofile_hasher.py": "/usr/local/bin/alleleprofile_hasher.py", "chewBBACA.py": "/usr/local/bin/chewBBACA.py", "chewie": "/usr/local/bin/chewie", "chewiesnake": "/usr/local/bin/chewiesnake", "chewiesnake_join": "/usr/local/bin/chewiesnake_join", "create_alleledbSheet.sh": "/usr/local/bin/create_alleledbSheet.sh", "create_sampleSheet.sh": "/usr/local/bin/create_sampleSheet.sh", "grapetree": "/usr/local/bin/grapetree", "hashID.py": "/usr/local/bin/hashID.py", "lighter": "/usr/local/bin/lighter", "shovill": "/usr/local/bin/shovill", "skesa": "/usr/local/bin/skesa", "stone": "/usr/local/bin/stone", "megahit_core": "/usr/local/bin/megahit_core", "megahit_core_no_hw_accel": "/usr/local/bin/megahit_core_no_hw_accel", "megahit_core_popcnt": "/usr/local/bin/megahit_core_popcnt", "fastp": "/usr/local/bin/fastp", "flash": "/usr/local/bin/flash", "megahit": "/usr/local/bin/megahit", "megahit_toolkit": "/usr/local/bin/megahit_toolkit", "pilon": "/usr/local/bin/pilon", "unidecode": "/usr/local/bin/unidecode"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/chewiesnake.
shpc-registry automated BioContainers addition for chewiesnake
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/chewiesnake
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/chewiesnake:3.0.0--hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/chewiesnake/3.0.0--hdfd78af_2
$ module help quay.io/biocontainers/chewiesnake/3.0.0--hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### chewiesnake-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### chewiesnake-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### chewiesnake-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### chewiesnake-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### chewiesnake-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### chewiesnake-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Clustering_DistanceMatrix.R

```bash
$ singularity exec <container> /usr/local/bin/Clustering_DistanceMatrix.R
$ podman run --it --rm --entrypoint /usr/local/bin/Clustering_DistanceMatrix.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Clustering_DistanceMatrix.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alleleprofile_hasher.py

```bash
$ singularity exec <container> /usr/local/bin/alleleprofile_hasher.py
$ podman run --it --rm --entrypoint /usr/local/bin/alleleprofile_hasher.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alleleprofile_hasher.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chewBBACA.py

```bash
$ singularity exec <container> /usr/local/bin/chewBBACA.py
$ podman run --it --rm --entrypoint /usr/local/bin/chewBBACA.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chewBBACA.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chewie

```bash
$ singularity exec <container> /usr/local/bin/chewie
$ podman run --it --rm --entrypoint /usr/local/bin/chewie   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chewie   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chewiesnake

```bash
$ singularity exec <container> /usr/local/bin/chewiesnake
$ podman run --it --rm --entrypoint /usr/local/bin/chewiesnake   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chewiesnake   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chewiesnake_join

```bash
$ singularity exec <container> /usr/local/bin/chewiesnake_join
$ podman run --it --rm --entrypoint /usr/local/bin/chewiesnake_join   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chewiesnake_join   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### create_alleledbSheet.sh

```bash
$ singularity exec <container> /usr/local/bin/create_alleledbSheet.sh
$ podman run --it --rm --entrypoint /usr/local/bin/create_alleledbSheet.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/create_alleledbSheet.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### create_sampleSheet.sh

```bash
$ singularity exec <container> /usr/local/bin/create_sampleSheet.sh
$ podman run --it --rm --entrypoint /usr/local/bin/create_sampleSheet.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/create_sampleSheet.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grapetree

```bash
$ singularity exec <container> /usr/local/bin/grapetree
$ podman run --it --rm --entrypoint /usr/local/bin/grapetree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grapetree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hashID.py

```bash
$ singularity exec <container> /usr/local/bin/hashID.py
$ podman run --it --rm --entrypoint /usr/local/bin/hashID.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hashID.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lighter

```bash
$ singularity exec <container> /usr/local/bin/lighter
$ podman run --it --rm --entrypoint /usr/local/bin/lighter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lighter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shovill

```bash
$ singularity exec <container> /usr/local/bin/shovill
$ podman run --it --rm --entrypoint /usr/local/bin/shovill   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shovill   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### skesa

```bash
$ singularity exec <container> /usr/local/bin/skesa
$ podman run --it --rm --entrypoint /usr/local/bin/skesa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/skesa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stone

```bash
$ singularity exec <container> /usr/local/bin/stone
$ podman run --it --rm --entrypoint /usr/local/bin/stone   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stone   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### megahit_core

```bash
$ singularity exec <container> /usr/local/bin/megahit_core
$ podman run --it --rm --entrypoint /usr/local/bin/megahit_core   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/megahit_core   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### megahit_core_no_hw_accel

```bash
$ singularity exec <container> /usr/local/bin/megahit_core_no_hw_accel
$ podman run --it --rm --entrypoint /usr/local/bin/megahit_core_no_hw_accel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/megahit_core_no_hw_accel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### megahit_core_popcnt

```bash
$ singularity exec <container> /usr/local/bin/megahit_core_popcnt
$ podman run --it --rm --entrypoint /usr/local/bin/megahit_core_popcnt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/megahit_core_popcnt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastp

```bash
$ singularity exec <container> /usr/local/bin/fastp
$ podman run --it --rm --entrypoint /usr/local/bin/fastp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flash

```bash
$ singularity exec <container> /usr/local/bin/flash
$ podman run --it --rm --entrypoint /usr/local/bin/flash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### megahit

```bash
$ singularity exec <container> /usr/local/bin/megahit
$ podman run --it --rm --entrypoint /usr/local/bin/megahit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/megahit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### megahit_toolkit

```bash
$ singularity exec <container> /usr/local/bin/megahit_toolkit
$ podman run --it --rm --entrypoint /usr/local/bin/megahit_toolkit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/megahit_toolkit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pilon

```bash
$ singularity exec <container> /usr/local/bin/pilon
$ podman run --it --rm --entrypoint /usr/local/bin/pilon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pilon   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unidecode

```bash
$ singularity exec <container> /usr/local/bin/unidecode
$ podman run --it --rm --entrypoint /usr/local/bin/unidecode   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unidecode   -v ${PWD} -w ${PWD} <container> -c " $@"
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