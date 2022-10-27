---
layout: container
name:  "quay.io/biocontainers/kneaddata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kneaddata/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/kneaddata/container.yaml"
updated_at: "2022-10-27 00:33:41.356819"
latest: "0.9.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/kneaddata"
aliases:
 - "kneaddata"
 - "kneaddata_bowtie2_discordant_pairs"
 - "kneaddata_build_database"
 - "kneaddata_database"
 - "kneaddata_read_count_table"
 - "kneaddata_test"
 - "kneaddata_trf_parallel"
versions:
 - "0.9.0--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for kneaddata"
config: {"url": "https://biocontainers.pro/tools/kneaddata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for kneaddata", "latest": {"0.9.0--pyhdfd78af_0": "sha256:82470860691070b1a8934fa77a0b149c74e10b2c4d41f2ea534f36e9cce00a25"}, "tags": {"0.9.0--pyhdfd78af_0": "sha256:82470860691070b1a8934fa77a0b149c74e10b2c4d41f2ea534f36e9cce00a25"}, "docker": "quay.io/biocontainers/kneaddata", "aliases": {"kneaddata": "/usr/local/bin/kneaddata", "kneaddata_bowtie2_discordant_pairs": "/usr/local/bin/kneaddata_bowtie2_discordant_pairs", "kneaddata_build_database": "/usr/local/bin/kneaddata_build_database", "kneaddata_database": "/usr/local/bin/kneaddata_database", "kneaddata_read_count_table": "/usr/local/bin/kneaddata_read_count_table", "kneaddata_test": "/usr/local/bin/kneaddata_test", "kneaddata_trf_parallel": "/usr/local/bin/kneaddata_trf_parallel"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/kneaddata.
shpc-registry automated BioContainers addition for kneaddata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kneaddata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kneaddata:0.9.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kneaddata/0.9.0--pyhdfd78af_0
$ module help quay.io/biocontainers/kneaddata/0.9.0--pyhdfd78af_0
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