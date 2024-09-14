---
layout: container
name:  "quay.io/biocontainers/kneaddata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kneaddata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/kneaddata/container.yaml"
updated_at: "2024-09-14 03:11:42.807315"
latest: "0.12.0--pyhdfd78af_1"
container_url: "https://biocontainers.pro/tools/kneaddata"
aliases:
 - "kneaddata"
 - "kneaddata_bowtie2_discordant_pairs"
 - "kneaddata_build_database"
 - "kneaddata_database"
 - "kneaddata_read_count_table"
 - "kneaddata_test"
 - "kneaddata_trf_parallel"
 - "trf4.10.0-rc.2.linux64.exe"
 - "trf"
 - "fastqc"
 - "trimmomatic"
 - "bowtie2"
 - "bowtie2-align-l"
 - "bowtie2-align-s"
 - "bowtie2-build"
 - "bowtie2-build-l"
 - "bowtie2-build-s"
versions:
 - "0.9.0--pyhdfd78af_0"
 - "0.12.0--pyhdfd78af_0"
 - "0.10.0--pyhdfd78af_0"
 - "0.12.0--pyhdfd78af_1"
description: "shpc-registry automated BioContainers addition for kneaddata"
config: {"url": "https://biocontainers.pro/tools/kneaddata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for kneaddata", "latest": {"0.12.0--pyhdfd78af_1": "sha256:e887a204da73e4c8362e7abe4998b516867609213e14d71b0ef05bb01427f55f"}, "tags": {"0.9.0--pyhdfd78af_0": "sha256:82470860691070b1a8934fa77a0b149c74e10b2c4d41f2ea534f36e9cce00a25", "0.12.0--pyhdfd78af_0": "sha256:bd990e3d0f22d21a3322c3808a866d4a52b8b8d04129dfb7b1e3cd087a5ed732", "0.10.0--pyhdfd78af_0": "sha256:9ee7eb1d0ac4809beaadde622a0299677575708fa6cb45e9f1ad55388860aea4", "0.12.0--pyhdfd78af_1": "sha256:e887a204da73e4c8362e7abe4998b516867609213e14d71b0ef05bb01427f55f"}, "docker": "quay.io/biocontainers/kneaddata", "aliases": {"kneaddata": "/usr/local/bin/kneaddata", "kneaddata_bowtie2_discordant_pairs": "/usr/local/bin/kneaddata_bowtie2_discordant_pairs", "kneaddata_build_database": "/usr/local/bin/kneaddata_build_database", "kneaddata_database": "/usr/local/bin/kneaddata_database", "kneaddata_read_count_table": "/usr/local/bin/kneaddata_read_count_table", "kneaddata_test": "/usr/local/bin/kneaddata_test", "kneaddata_trf_parallel": "/usr/local/bin/kneaddata_trf_parallel", "trf4.10.0-rc.2.linux64.exe": "/usr/local/bin/trf4.10.0-rc.2.linux64.exe", "trf": "/usr/local/bin/trf", "fastqc": "/usr/local/bin/fastqc", "trimmomatic": "/usr/local/bin/trimmomatic", "bowtie2": "/usr/local/bin/bowtie2", "bowtie2-align-l": "/usr/local/bin/bowtie2-align-l", "bowtie2-align-s": "/usr/local/bin/bowtie2-align-s", "bowtie2-build": "/usr/local/bin/bowtie2-build", "bowtie2-build-l": "/usr/local/bin/bowtie2-build-l", "bowtie2-build-s": "/usr/local/bin/bowtie2-build-s"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/kneaddata.
shpc-registry automated BioContainers addition for kneaddata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kneaddata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kneaddata:0.12.0--pyhdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kneaddata/0.12.0--pyhdfd78af_1
$ module help quay.io/biocontainers/kneaddata/0.12.0--pyhdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kneaddata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kneaddata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kneaddata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kneaddata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kneaddata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kneaddata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### kneaddata

```bash
$ singularity exec <container> /usr/local/bin/kneaddata
$ podman run --it --rm --entrypoint /usr/local/bin/kneaddata   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kneaddata   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kneaddata_bowtie2_discordant_pairs

```bash
$ singularity exec <container> /usr/local/bin/kneaddata_bowtie2_discordant_pairs
$ podman run --it --rm --entrypoint /usr/local/bin/kneaddata_bowtie2_discordant_pairs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kneaddata_bowtie2_discordant_pairs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kneaddata_build_database

```bash
$ singularity exec <container> /usr/local/bin/kneaddata_build_database
$ podman run --it --rm --entrypoint /usr/local/bin/kneaddata_build_database   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kneaddata_build_database   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kneaddata_database

```bash
$ singularity exec <container> /usr/local/bin/kneaddata_database
$ podman run --it --rm --entrypoint /usr/local/bin/kneaddata_database   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kneaddata_database   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kneaddata_read_count_table

```bash
$ singularity exec <container> /usr/local/bin/kneaddata_read_count_table
$ podman run --it --rm --entrypoint /usr/local/bin/kneaddata_read_count_table   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kneaddata_read_count_table   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kneaddata_test

```bash
$ singularity exec <container> /usr/local/bin/kneaddata_test
$ podman run --it --rm --entrypoint /usr/local/bin/kneaddata_test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kneaddata_test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kneaddata_trf_parallel

```bash
$ singularity exec <container> /usr/local/bin/kneaddata_trf_parallel
$ podman run --it --rm --entrypoint /usr/local/bin/kneaddata_trf_parallel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kneaddata_trf_parallel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trf4.10.0-rc.2.linux64.exe

```bash
$ singularity exec <container> /usr/local/bin/trf4.10.0-rc.2.linux64.exe
$ podman run --it --rm --entrypoint /usr/local/bin/trf4.10.0-rc.2.linux64.exe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trf4.10.0-rc.2.linux64.exe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trf

```bash
$ singularity exec <container> /usr/local/bin/trf
$ podman run --it --rm --entrypoint /usr/local/bin/trf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastqc

```bash
$ singularity exec <container> /usr/local/bin/fastqc
$ podman run --it --rm --entrypoint /usr/local/bin/fastqc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastqc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trimmomatic

```bash
$ singularity exec <container> /usr/local/bin/trimmomatic
$ podman run --it --rm --entrypoint /usr/local/bin/trimmomatic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trimmomatic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2

```bash
$ singularity exec <container> /usr/local/bin/bowtie2
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-align-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-align-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-align-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-align-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-build

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-build
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-build-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-build-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-build-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-build-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-build-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-build-s   -v ${PWD} -w ${PWD} <container> -c " $@"
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