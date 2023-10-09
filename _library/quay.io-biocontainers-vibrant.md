---
layout: container
name:  "quay.io/biocontainers/vibrant"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/vibrant/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/vibrant/container.yaml"
updated_at: "2023-10-09 02:23:52.326143"
latest: "1.2.1--hdfd78af_4"
container_url: "https://biocontainers.pro/tools/vibrant"
aliases:
 - "VIBRANT_annotation.py"
 - "VIBRANT_extract_nucleotide.py"
 - "VIBRANT_extract_protein.py"
 - "VIBRANT_run.py"
 - "download-db.sh"
 - "prodigal"
 - "hmmpgmd_shard"
 - "easel"
 - "esl-mixdchlet"
 - "esl-alimanip"
 - "esl-alimap"
 - "esl-alimask"
 - "esl-alimerge"
 - "esl-alipid"
 - "esl-alirev"
versions:
 - "1.2.1--hdfd78af_2"
 - "1.2.1--hdfd78af_4"
description: "shpc-registry automated BioContainers addition for vibrant"
config: {"url": "https://biocontainers.pro/tools/vibrant", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for vibrant", "latest": {"1.2.1--hdfd78af_4": "sha256:79a3b6eb49d7ded054d8d65e2a7d28c810b2edf6f742437cb697c9484367b6d4"}, "tags": {"1.2.1--hdfd78af_2": "sha256:12d656f306c195b53ef653dd42c2d3558abdb835710112840d62d7c25aa62530", "1.2.1--hdfd78af_4": "sha256:79a3b6eb49d7ded054d8d65e2a7d28c810b2edf6f742437cb697c9484367b6d4"}, "docker": "quay.io/biocontainers/vibrant", "aliases": {"VIBRANT_annotation.py": "/usr/local/bin/VIBRANT_annotation.py", "VIBRANT_extract_nucleotide.py": "/usr/local/bin/VIBRANT_extract_nucleotide.py", "VIBRANT_extract_protein.py": "/usr/local/bin/VIBRANT_extract_protein.py", "VIBRANT_run.py": "/usr/local/bin/VIBRANT_run.py", "download-db.sh": "/usr/local/bin/download-db.sh", "prodigal": "/usr/local/bin/prodigal", "hmmpgmd_shard": "/usr/local/bin/hmmpgmd_shard", "easel": "/usr/local/bin/easel", "esl-mixdchlet": "/usr/local/bin/esl-mixdchlet", "esl-alimanip": "/usr/local/bin/esl-alimanip", "esl-alimap": "/usr/local/bin/esl-alimap", "esl-alimask": "/usr/local/bin/esl-alimask", "esl-alimerge": "/usr/local/bin/esl-alimerge", "esl-alipid": "/usr/local/bin/esl-alipid", "esl-alirev": "/usr/local/bin/esl-alirev"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/vibrant.
shpc-registry automated BioContainers addition for vibrant
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/vibrant
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/vibrant:1.2.1--hdfd78af_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/vibrant/1.2.1--hdfd78af_4
$ module help quay.io/biocontainers/vibrant/1.2.1--hdfd78af_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### vibrant-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### vibrant-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### vibrant-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### vibrant-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### vibrant-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### vibrant-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### VIBRANT_annotation.py

```bash
$ singularity exec <container> /usr/local/bin/VIBRANT_annotation.py
$ podman run --it --rm --entrypoint /usr/local/bin/VIBRANT_annotation.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/VIBRANT_annotation.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### VIBRANT_extract_nucleotide.py

```bash
$ singularity exec <container> /usr/local/bin/VIBRANT_extract_nucleotide.py
$ podman run --it --rm --entrypoint /usr/local/bin/VIBRANT_extract_nucleotide.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/VIBRANT_extract_nucleotide.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### VIBRANT_extract_protein.py

```bash
$ singularity exec <container> /usr/local/bin/VIBRANT_extract_protein.py
$ podman run --it --rm --entrypoint /usr/local/bin/VIBRANT_extract_protein.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/VIBRANT_extract_protein.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### VIBRANT_run.py

```bash
$ singularity exec <container> /usr/local/bin/VIBRANT_run.py
$ podman run --it --rm --entrypoint /usr/local/bin/VIBRANT_run.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/VIBRANT_run.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### download-db.sh

```bash
$ singularity exec <container> /usr/local/bin/download-db.sh
$ podman run --it --rm --entrypoint /usr/local/bin/download-db.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/download-db.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prodigal

```bash
$ singularity exec <container> /usr/local/bin/prodigal
$ podman run --it --rm --entrypoint /usr/local/bin/prodigal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prodigal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmpgmd_shard

```bash
$ singularity exec <container> /usr/local/bin/hmmpgmd_shard
$ podman run --it --rm --entrypoint /usr/local/bin/hmmpgmd_shard   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmpgmd_shard   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### easel

```bash
$ singularity exec <container> /usr/local/bin/easel
$ podman run --it --rm --entrypoint /usr/local/bin/easel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/easel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-mixdchlet

```bash
$ singularity exec <container> /usr/local/bin/esl-mixdchlet
$ podman run --it --rm --entrypoint /usr/local/bin/esl-mixdchlet   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-mixdchlet   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-alimanip

```bash
$ singularity exec <container> /usr/local/bin/esl-alimanip
$ podman run --it --rm --entrypoint /usr/local/bin/esl-alimanip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-alimanip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-alimap

```bash
$ singularity exec <container> /usr/local/bin/esl-alimap
$ podman run --it --rm --entrypoint /usr/local/bin/esl-alimap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-alimap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-alimask

```bash
$ singularity exec <container> /usr/local/bin/esl-alimask
$ podman run --it --rm --entrypoint /usr/local/bin/esl-alimask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-alimask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-alimerge

```bash
$ singularity exec <container> /usr/local/bin/esl-alimerge
$ podman run --it --rm --entrypoint /usr/local/bin/esl-alimerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-alimerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-alipid

```bash
$ singularity exec <container> /usr/local/bin/esl-alipid
$ podman run --it --rm --entrypoint /usr/local/bin/esl-alipid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-alipid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-alirev

```bash
$ singularity exec <container> /usr/local/bin/esl-alirev
$ podman run --it --rm --entrypoint /usr/local/bin/esl-alirev   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-alirev   -v ${PWD} -w ${PWD} <container> -c " $@"
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