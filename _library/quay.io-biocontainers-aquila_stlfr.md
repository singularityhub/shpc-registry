---
layout: container
name:  "quay.io/biocontainers/aquila_stlfr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/aquila_stlfr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/aquila_stlfr/container.yaml"
updated_at: "2023-10-05 04:00:23.661446"
latest: "1.2.11--py_0"
container_url: "https://biocontainers.pro/tools/aquila_stlfr"
aliases:
 - "Aquila_stLFR_assembly_based_variants_call"
 - "Aquila_stLFR_clean"
 - "Aquila_stLFR_fastq_preprocess"
 - "Aquila_stLFR_phasing_all_variants"
 - "Aquila_stLFR_step1"
 - "Aquila_stLFR_step2"
 - "Aquila_step0_sortbam_hybrid"
 - "Aquila_step1_hybrid"
 - "paftools.js"
 - "minimap2"
 - "k8"
 - "f2py3.7"
 - "2to3-3.7"
 - "idle3.7"
 - "pydoc3.7"
 - "python3.7"
 - "python3.7-config"
 - "python3.7m"
versions:
 - "1.2.9--py_0"
 - "1.2.11--py_0"
description: "shpc-registry automated BioContainers addition for aquila_stlfr"
config: {"url": "https://biocontainers.pro/tools/aquila_stlfr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for aquila_stlfr", "latest": {"1.2.11--py_0": "sha256:f4871f71899e56e8b3549ddece63a1726f7f263ad3e9e91d706fb54062ca99dd"}, "tags": {"1.2.9--py_0": "sha256:4c761deb2bb351fc8214778d87cee91a4c0003899d4b30ae11a3befe458a044e", "1.2.11--py_0": "sha256:f4871f71899e56e8b3549ddece63a1726f7f263ad3e9e91d706fb54062ca99dd"}, "docker": "quay.io/biocontainers/aquila_stlfr", "aliases": {"Aquila_stLFR_assembly_based_variants_call": "/usr/local/bin/Aquila_stLFR_assembly_based_variants_call", "Aquila_stLFR_clean": "/usr/local/bin/Aquila_stLFR_clean", "Aquila_stLFR_fastq_preprocess": "/usr/local/bin/Aquila_stLFR_fastq_preprocess", "Aquila_stLFR_phasing_all_variants": "/usr/local/bin/Aquila_stLFR_phasing_all_variants", "Aquila_stLFR_step1": "/usr/local/bin/Aquila_stLFR_step1", "Aquila_stLFR_step2": "/usr/local/bin/Aquila_stLFR_step2", "Aquila_step0_sortbam_hybrid": "/usr/local/bin/Aquila_step0_sortbam_hybrid", "Aquila_step1_hybrid": "/usr/local/bin/Aquila_step1_hybrid", "paftools.js": "/usr/local/bin/paftools.js", "minimap2": "/usr/local/bin/minimap2", "k8": "/usr/local/bin/k8", "f2py3.7": "/usr/local/bin/f2py3.7", "2to3-3.7": "/usr/local/bin/2to3-3.7", "idle3.7": "/usr/local/bin/idle3.7", "pydoc3.7": "/usr/local/bin/pydoc3.7", "python3.7": "/usr/local/bin/python3.7", "python3.7-config": "/usr/local/bin/python3.7-config", "python3.7m": "/usr/local/bin/python3.7m"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/aquila_stlfr.
shpc-registry automated BioContainers addition for aquila_stlfr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/aquila_stlfr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/aquila_stlfr:1.2.11--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/aquila_stlfr/1.2.11--py_0
$ module help quay.io/biocontainers/aquila_stlfr/1.2.11--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### aquila_stlfr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### aquila_stlfr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### aquila_stlfr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### aquila_stlfr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### aquila_stlfr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### aquila_stlfr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Aquila_stLFR_assembly_based_variants_call

```bash
$ singularity exec <container> /usr/local/bin/Aquila_stLFR_assembly_based_variants_call
$ podman run --it --rm --entrypoint /usr/local/bin/Aquila_stLFR_assembly_based_variants_call   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Aquila_stLFR_assembly_based_variants_call   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Aquila_stLFR_clean

```bash
$ singularity exec <container> /usr/local/bin/Aquila_stLFR_clean
$ podman run --it --rm --entrypoint /usr/local/bin/Aquila_stLFR_clean   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Aquila_stLFR_clean   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Aquila_stLFR_fastq_preprocess

```bash
$ singularity exec <container> /usr/local/bin/Aquila_stLFR_fastq_preprocess
$ podman run --it --rm --entrypoint /usr/local/bin/Aquila_stLFR_fastq_preprocess   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Aquila_stLFR_fastq_preprocess   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Aquila_stLFR_phasing_all_variants

```bash
$ singularity exec <container> /usr/local/bin/Aquila_stLFR_phasing_all_variants
$ podman run --it --rm --entrypoint /usr/local/bin/Aquila_stLFR_phasing_all_variants   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Aquila_stLFR_phasing_all_variants   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Aquila_stLFR_step1

```bash
$ singularity exec <container> /usr/local/bin/Aquila_stLFR_step1
$ podman run --it --rm --entrypoint /usr/local/bin/Aquila_stLFR_step1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Aquila_stLFR_step1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Aquila_stLFR_step2

```bash
$ singularity exec <container> /usr/local/bin/Aquila_stLFR_step2
$ podman run --it --rm --entrypoint /usr/local/bin/Aquila_stLFR_step2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Aquila_stLFR_step2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Aquila_step0_sortbam_hybrid

```bash
$ singularity exec <container> /usr/local/bin/Aquila_step0_sortbam_hybrid
$ podman run --it --rm --entrypoint /usr/local/bin/Aquila_step0_sortbam_hybrid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Aquila_step0_sortbam_hybrid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Aquila_step1_hybrid

```bash
$ singularity exec <container> /usr/local/bin/Aquila_step1_hybrid
$ podman run --it --rm --entrypoint /usr/local/bin/Aquila_step1_hybrid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Aquila_step1_hybrid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### paftools.js

```bash
$ singularity exec <container> /usr/local/bin/paftools.js
$ podman run --it --rm --entrypoint /usr/local/bin/paftools.js   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/paftools.js   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minimap2

```bash
$ singularity exec <container> /usr/local/bin/minimap2
$ podman run --it --rm --entrypoint /usr/local/bin/minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### k8

```bash
$ singularity exec <container> /usr/local/bin/k8
$ podman run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.7

```bash
$ singularity exec <container> /usr/local/bin/f2py3.7
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.7

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.7

```bash
$ singularity exec <container> /usr/local/bin/idle3.7
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.7

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.7
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7

```bash
$ singularity exec <container> /usr/local/bin/python3.7
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7-config

```bash
$ singularity exec <container> /usr/local/bin/python3.7-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.7m

```bash
$ singularity exec <container> /usr/local/bin/python3.7m
$ podman run --it --rm --entrypoint /usr/local/bin/python3.7m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.7m   -v ${PWD} -w ${PWD} <container> -c " $@"
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