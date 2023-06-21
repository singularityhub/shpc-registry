---
layout: container
name:  "quay.io/biocontainers/satrap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/satrap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/satrap/container.yaml"
updated_at: "2023-06-21 03:03:01.825085"
latest: "0.2--h4ac6f70_6"
container_url: "https://biocontainers.pro/tools/satrap"
aliases:
 - "2csfastq_1csfastq"
 - "cs2bs_assembly"
 - "csfasta_to_fastq"
 - "fasta_remove"
 - "pass"
 - "rename_fastq_tag"
 - "satrap"
 - "cd-hit-est"
versions:
 - "0.2--h9f5acd7_4"
 - "0.2--h4ac6f70_6"
description: "shpc-registry automated BioContainers addition for satrap"
config: {"url": "https://biocontainers.pro/tools/satrap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for satrap", "latest": {"0.2--h4ac6f70_6": "sha256:c7253a080b55a2730a09d36eeb41a82ac888ef0562177006e4c265cf096d16e0"}, "tags": {"0.2--h9f5acd7_4": "sha256:7a8fedacbd66ec9ea029931f76ac926c95ae3b0168088daec30808fde0b8219e", "0.2--h4ac6f70_6": "sha256:c7253a080b55a2730a09d36eeb41a82ac888ef0562177006e4c265cf096d16e0"}, "docker": "quay.io/biocontainers/satrap", "aliases": {"2csfastq_1csfastq": "/usr/local/bin/2csfastq_1csfastq", "cs2bs_assembly": "/usr/local/bin/cs2bs_assembly", "csfasta_to_fastq": "/usr/local/bin/csfasta_to_fastq", "fasta_remove": "/usr/local/bin/fasta_remove", "pass": "/usr/local/bin/pass", "rename_fastq_tag": "/usr/local/bin/rename_fastq_tag", "satrap": "/usr/local/bin/satrap", "cd-hit-est": "/usr/local/bin/cd-hit-est"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/satrap.
shpc-registry automated BioContainers addition for satrap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/satrap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/satrap:0.2--h4ac6f70_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/satrap/0.2--h4ac6f70_6
$ module help quay.io/biocontainers/satrap/0.2--h4ac6f70_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### satrap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### satrap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### satrap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### satrap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### satrap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### satrap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 2csfastq_1csfastq

```bash
$ singularity exec <container> /usr/local/bin/2csfastq_1csfastq
$ podman run --it --rm --entrypoint /usr/local/bin/2csfastq_1csfastq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2csfastq_1csfastq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cs2bs_assembly

```bash
$ singularity exec <container> /usr/local/bin/cs2bs_assembly
$ podman run --it --rm --entrypoint /usr/local/bin/cs2bs_assembly   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cs2bs_assembly   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csfasta_to_fastq

```bash
$ singularity exec <container> /usr/local/bin/csfasta_to_fastq
$ podman run --it --rm --entrypoint /usr/local/bin/csfasta_to_fastq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csfasta_to_fastq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta_remove

```bash
$ singularity exec <container> /usr/local/bin/fasta_remove
$ podman run --it --rm --entrypoint /usr/local/bin/fasta_remove   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta_remove   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pass

```bash
$ singularity exec <container> /usr/local/bin/pass
$ podman run --it --rm --entrypoint /usr/local/bin/pass   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pass   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rename_fastq_tag

```bash
$ singularity exec <container> /usr/local/bin/rename_fastq_tag
$ podman run --it --rm --entrypoint /usr/local/bin/rename_fastq_tag   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rename_fastq_tag   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### satrap

```bash
$ singularity exec <container> /usr/local/bin/satrap
$ podman run --it --rm --entrypoint /usr/local/bin/satrap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/satrap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cd-hit-est

```bash
$ singularity exec <container> /usr/local/bin/cd-hit-est
$ podman run --it --rm --entrypoint /usr/local/bin/cd-hit-est   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cd-hit-est   -v ${PWD} -w ${PWD} <container> -c " $@"
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