---
layout: container
name:  "quay.io/biocontainers/vcf-validator"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/vcf-validator/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/vcf-validator/container.yaml"
updated_at: "2025-01-25 02:54:51.373246"
latest: "0.10.0--h9cfbc0b_2"
container_url: "https://biocontainers.pro/tools/vcf-validator"
aliases:
 - "vcf_assembly_checker"
 - "vcf_validator"
versions:
 - "0.9.7--h9ee0642_0"
 - "0.10.0--h05c6178_1"
 - "0.10.0--h9cfbc0b_2"
description: "singularity registry hpc automated addition for vcf-validator"
config: {"url": "https://biocontainers.pro/tools/vcf-validator", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for vcf-validator", "latest": {"0.10.0--h9cfbc0b_2": "sha256:9a39fc4d05f390be21a4dbe4bf82760398566370861a56cf41c4e5523acb6419"}, "tags": {"0.9.7--h9ee0642_0": "sha256:b42848a514ba7781cd894af60deb443d96487fc0cd826dd4674457a9c0ddc79e", "0.10.0--h05c6178_1": "sha256:7ce1b513659c52481b6afddfc9360f3f567b1b3a6417a3268a34ad400a55f08a", "0.10.0--h9cfbc0b_2": "sha256:9a39fc4d05f390be21a4dbe4bf82760398566370861a56cf41c4e5523acb6419"}, "docker": "quay.io/biocontainers/vcf-validator", "aliases": {"vcf_assembly_checker": "/usr/local/bin/vcf_assembly_checker", "vcf_validator": "/usr/local/bin/vcf_validator"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/vcf-validator.
singularity registry hpc automated addition for vcf-validator
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/vcf-validator
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/vcf-validator:0.10.0--h9cfbc0b_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/vcf-validator/0.10.0--h9cfbc0b_2
$ module help quay.io/biocontainers/vcf-validator/0.10.0--h9cfbc0b_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### vcf-validator-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### vcf-validator-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### vcf-validator-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### vcf-validator-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### vcf-validator-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### vcf-validator-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### vcf_assembly_checker

```bash
$ singularity exec <container> /usr/local/bin/vcf_assembly_checker
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_assembly_checker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_assembly_checker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_validator

```bash
$ singularity exec <container> /usr/local/bin/vcf_validator
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_validator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_validator   -v ${PWD} -w ${PWD} <container> -c " $@"
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