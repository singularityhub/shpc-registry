---
layout: container
name:  "quay.io/biocontainers/panpasco"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/panpasco/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/panpasco/container.yaml"
updated_at: "2026-01-25 04:17:34.634699"
latest: "1.0.1--py38r40_0"
container_url: "https://biocontainers.pro/tools/panpasco"
aliases:
 - "GenomeAnalysisTK"
 - "croco-0.6-config"
 - "csslint-0.6"
 - "gatk3"
 - "gatk3-register"
 - "panpasco-distance"
 - "panpasco-pipeline"
 - "x86_64-conda_cos6-linux-gnu-pkg-config"
 - "flash"
 - "picard"
 - "g-ir-annotation-tool"
 - "g-ir-compiler"
 - "g-ir-generate"
 - "g-ir-inspect"
 - "g-ir-scanner"
 - "trimmomatic"
 - "Magick++-config"
 - "MagickCore-config"
versions:
 - "1.0.1--py38r40_0"
description: "shpc-registry automated BioContainers addition for panpasco"
config: {"url": "https://biocontainers.pro/tools/panpasco", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for panpasco", "latest": {"1.0.1--py38r40_0": "sha256:91bbbca7154eab8f3996db20b1c396beb10de5232efd5e0fd1bc1f25aa34a537"}, "tags": {"1.0.1--py38r40_0": "sha256:91bbbca7154eab8f3996db20b1c396beb10de5232efd5e0fd1bc1f25aa34a537"}, "docker": "quay.io/biocontainers/panpasco", "aliases": {"GenomeAnalysisTK": "/usr/local/bin/GenomeAnalysisTK", "croco-0.6-config": "/usr/local/bin/croco-0.6-config", "csslint-0.6": "/usr/local/bin/csslint-0.6", "gatk3": "/usr/local/bin/gatk3", "gatk3-register": "/usr/local/bin/gatk3-register", "panpasco-distance": "/usr/local/bin/panpasco-distance", "panpasco-pipeline": "/usr/local/bin/panpasco-pipeline", "x86_64-conda_cos6-linux-gnu-pkg-config": "/usr/local/bin/x86_64-conda_cos6-linux-gnu-pkg-config", "flash": "/usr/local/bin/flash", "picard": "/usr/local/bin/picard", "g-ir-annotation-tool": "/usr/local/bin/g-ir-annotation-tool", "g-ir-compiler": "/usr/local/bin/g-ir-compiler", "g-ir-generate": "/usr/local/bin/g-ir-generate", "g-ir-inspect": "/usr/local/bin/g-ir-inspect", "g-ir-scanner": "/usr/local/bin/g-ir-scanner", "trimmomatic": "/usr/local/bin/trimmomatic", "Magick++-config": "/usr/local/bin/Magick++-config", "MagickCore-config": "/usr/local/bin/MagickCore-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/panpasco.
shpc-registry automated BioContainers addition for panpasco
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/panpasco
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/panpasco:1.0.1--py38r40_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/panpasco/1.0.1--py38r40_0
$ module help quay.io/biocontainers/panpasco/1.0.1--py38r40_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### panpasco-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### panpasco-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### panpasco-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### panpasco-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### panpasco-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### panpasco-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### GenomeAnalysisTK

```bash
$ singularity exec <container> /usr/local/bin/GenomeAnalysisTK
$ podman run --it --rm --entrypoint /usr/local/bin/GenomeAnalysisTK   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GenomeAnalysisTK   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### croco-0.6-config

```bash
$ singularity exec <container> /usr/local/bin/croco-0.6-config
$ podman run --it --rm --entrypoint /usr/local/bin/croco-0.6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/croco-0.6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csslint-0.6

```bash
$ singularity exec <container> /usr/local/bin/csslint-0.6
$ podman run --it --rm --entrypoint /usr/local/bin/csslint-0.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csslint-0.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gatk3

```bash
$ singularity exec <container> /usr/local/bin/gatk3
$ podman run --it --rm --entrypoint /usr/local/bin/gatk3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gatk3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gatk3-register

```bash
$ singularity exec <container> /usr/local/bin/gatk3-register
$ podman run --it --rm --entrypoint /usr/local/bin/gatk3-register   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gatk3-register   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### panpasco-distance

```bash
$ singularity exec <container> /usr/local/bin/panpasco-distance
$ podman run --it --rm --entrypoint /usr/local/bin/panpasco-distance   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/panpasco-distance   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### panpasco-pipeline

```bash
$ singularity exec <container> /usr/local/bin/panpasco-pipeline
$ podman run --it --rm --entrypoint /usr/local/bin/panpasco-pipeline   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/panpasco-pipeline   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x86_64-conda_cos6-linux-gnu-pkg-config

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda_cos6-linux-gnu-pkg-config
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda_cos6-linux-gnu-pkg-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda_cos6-linux-gnu-pkg-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flash

```bash
$ singularity exec <container> /usr/local/bin/flash
$ podman run --it --rm --entrypoint /usr/local/bin/flash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### picard

```bash
$ singularity exec <container> /usr/local/bin/picard
$ podman run --it --rm --entrypoint /usr/local/bin/picard   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/picard   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g-ir-annotation-tool

```bash
$ singularity exec <container> /usr/local/bin/g-ir-annotation-tool
$ podman run --it --rm --entrypoint /usr/local/bin/g-ir-annotation-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g-ir-annotation-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g-ir-compiler

```bash
$ singularity exec <container> /usr/local/bin/g-ir-compiler
$ podman run --it --rm --entrypoint /usr/local/bin/g-ir-compiler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g-ir-compiler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g-ir-generate

```bash
$ singularity exec <container> /usr/local/bin/g-ir-generate
$ podman run --it --rm --entrypoint /usr/local/bin/g-ir-generate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g-ir-generate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g-ir-inspect

```bash
$ singularity exec <container> /usr/local/bin/g-ir-inspect
$ podman run --it --rm --entrypoint /usr/local/bin/g-ir-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g-ir-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g-ir-scanner

```bash
$ singularity exec <container> /usr/local/bin/g-ir-scanner
$ podman run --it --rm --entrypoint /usr/local/bin/g-ir-scanner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g-ir-scanner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trimmomatic

```bash
$ singularity exec <container> /usr/local/bin/trimmomatic
$ podman run --it --rm --entrypoint /usr/local/bin/trimmomatic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trimmomatic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Magick++-config

```bash
$ singularity exec <container> /usr/local/bin/Magick++-config
$ podman run --it --rm --entrypoint /usr/local/bin/Magick++-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Magick++-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MagickCore-config

```bash
$ singularity exec <container> /usr/local/bin/MagickCore-config
$ podman run --it --rm --entrypoint /usr/local/bin/MagickCore-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MagickCore-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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