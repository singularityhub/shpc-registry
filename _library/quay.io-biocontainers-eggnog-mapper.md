---
layout: container
name:  "quay.io/biocontainers/eggnog-mapper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/eggnog-mapper/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/eggnog-mapper/container.yaml"
updated_at: "2024-06-08 02:40:38.056123"
latest: "2.1.12--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/eggnog-mapper"
aliases:
 - "create_dbs.py"
 - "download_eggnog_data.py"
 - "emapper.py"
 - "hmm_mapper.py"
 - "hmm_server.py"
 - "hmm_worker.py"
 - "mmseqs"
 - "vba_extract.py"
 - "gawk-5.1.0"
 - "awk"
 - "gawk"
 - "diamond"
 - "prodigal"
 - "hmmpgmd_shard"
 - "easel"
 - "esl-mixdchlet"
versions:
 - "2.1.9--pyhdfd78af_0"
 - "2.1.10--pyhdfd78af_0"
 - "2.1.11--pyhdfd78af_0"
 - "2.1.12--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for eggnog-mapper"
config: {"url": "https://biocontainers.pro/tools/eggnog-mapper", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for eggnog-mapper", "latest": {"2.1.12--pyhdfd78af_0": "sha256:d32edadcbcca32d4783e5275f848df1ab23a7df7ce819ac64c161e850ae2b235"}, "tags": {"2.1.9--pyhdfd78af_0": "sha256:c583657bc48787ef25c96a7a78e195dcaf78b3864b37f945b514a81e9f29581b", "2.1.10--pyhdfd78af_0": "sha256:59e9957433b320777286281994407748ed21c87f96171f876d48f3a349255ce2", "2.1.11--pyhdfd78af_0": "sha256:00c0226f06e558ec26cb048aa5c4700a7f58197885cd35eca01ca61c9707ef53", "2.1.12--pyhdfd78af_0": "sha256:d32edadcbcca32d4783e5275f848df1ab23a7df7ce819ac64c161e850ae2b235"}, "docker": "quay.io/biocontainers/eggnog-mapper", "aliases": {"create_dbs.py": "/usr/local/bin/create_dbs.py", "download_eggnog_data.py": "/usr/local/bin/download_eggnog_data.py", "emapper.py": "/usr/local/bin/emapper.py", "hmm_mapper.py": "/usr/local/bin/hmm_mapper.py", "hmm_server.py": "/usr/local/bin/hmm_server.py", "hmm_worker.py": "/usr/local/bin/hmm_worker.py", "mmseqs": "/usr/local/bin/mmseqs", "vba_extract.py": "/usr/local/bin/vba_extract.py", "gawk-5.1.0": "/usr/local/bin/gawk-5.1.0", "awk": "/usr/local/bin/awk", "gawk": "/usr/local/bin/gawk", "diamond": "/usr/local/bin/diamond", "prodigal": "/usr/local/bin/prodigal", "hmmpgmd_shard": "/usr/local/bin/hmmpgmd_shard", "easel": "/usr/local/bin/easel", "esl-mixdchlet": "/usr/local/bin/esl-mixdchlet"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/eggnog-mapper.
shpc-registry automated BioContainers addition for eggnog-mapper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/eggnog-mapper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/eggnog-mapper:2.1.12--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/eggnog-mapper/2.1.12--pyhdfd78af_0
$ module help quay.io/biocontainers/eggnog-mapper/2.1.12--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### eggnog-mapper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### eggnog-mapper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### eggnog-mapper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### eggnog-mapper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### eggnog-mapper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### eggnog-mapper-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### create_dbs.py

```bash
$ singularity exec <container> /usr/local/bin/create_dbs.py
$ podman run --it --rm --entrypoint /usr/local/bin/create_dbs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/create_dbs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### download_eggnog_data.py

```bash
$ singularity exec <container> /usr/local/bin/download_eggnog_data.py
$ podman run --it --rm --entrypoint /usr/local/bin/download_eggnog_data.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/download_eggnog_data.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### emapper.py

```bash
$ singularity exec <container> /usr/local/bin/emapper.py
$ podman run --it --rm --entrypoint /usr/local/bin/emapper.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/emapper.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmm_mapper.py

```bash
$ singularity exec <container> /usr/local/bin/hmm_mapper.py
$ podman run --it --rm --entrypoint /usr/local/bin/hmm_mapper.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmm_mapper.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmm_server.py

```bash
$ singularity exec <container> /usr/local/bin/hmm_server.py
$ podman run --it --rm --entrypoint /usr/local/bin/hmm_server.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmm_server.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmm_worker.py

```bash
$ singularity exec <container> /usr/local/bin/hmm_worker.py
$ podman run --it --rm --entrypoint /usr/local/bin/hmm_worker.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmm_worker.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mmseqs

```bash
$ singularity exec <container> /usr/local/bin/mmseqs
$ podman run --it --rm --entrypoint /usr/local/bin/mmseqs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mmseqs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vba_extract.py

```bash
$ singularity exec <container> /usr/local/bin/vba_extract.py
$ podman run --it --rm --entrypoint /usr/local/bin/vba_extract.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vba_extract.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### diamond

```bash
$ singularity exec <container> /usr/local/bin/diamond
$ podman run --it --rm --entrypoint /usr/local/bin/diamond   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/diamond   -v ${PWD} -w ${PWD} <container> -c " $@"
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