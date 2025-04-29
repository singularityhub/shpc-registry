---
layout: container
name:  "quay.io/biocontainers/bioconductor-ompbam"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ompbam/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ompbam/container.yaml"
updated_at: "2025-04-29 03:09:52.304430"
latest: "1.10.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ompbam"

versions:
 - "1.2.0--r42hc247a5b_0"
 - "1.2.0--r42hf17093f_1"
 - "1.4.0--r43hf17093f_0"
 - "1.6.0--r43hf17093f_0"
 - "1.10.0--r44he5774e6_0"
description: "singularity registry hpc automated addition for bioconductor-ompbam"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ompbam", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bioconductor-ompbam", "latest": {"1.10.0--r44he5774e6_0": "sha256:f4499f38d1e02679c1822d90500e7d331ec0953b57a2cebbdf09cc87a4807cec"}, "tags": {"1.2.0--r42hc247a5b_0": "sha256:bbd78db9870b497796cc8fd86f2b5994e34895f4adcb306b9f4d54f089706e7d", "1.2.0--r42hf17093f_1": "sha256:463c070c6c2da625c90459b7f7f319a19149ac78cae5474c1358b4c1b8ba1699", "1.4.0--r43hf17093f_0": "sha256:e97c18882020addb5f3211d83a5b0b0d7a6f30fd1ee4a1f9adc0802b73202c9d", "1.6.0--r43hf17093f_0": "sha256:470c37a4a17adcc128a6083761b79fd433f1746d535122a959c055912f332908", "1.10.0--r44he5774e6_0": "sha256:f4499f38d1e02679c1822d90500e7d331ec0953b57a2cebbdf09cc87a4807cec"}, "docker": "quay.io/biocontainers/bioconductor-ompbam"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ompbam.
singularity registry hpc automated addition for bioconductor-ompbam
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ompbam
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ompbam:1.10.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ompbam/1.10.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-ompbam/1.10.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ompbam-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ompbam-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ompbam-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ompbam-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ompbam-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ompbam-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ompbam

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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