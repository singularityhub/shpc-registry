---
layout: container
name:  "quay.io/biocontainers/mhcflurry"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mhcflurry/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/mhcflurry/container.yaml"
updated_at: "2022-10-27 01:01:32.564660"
latest: "2.0.1--pyh864c0ab_0"
container_url: "https://biocontainers.pro/tools/mhcflurry"
aliases:
 - "_mhcflurry-cluster-worker-entry-point"
 - "mhcflurry-calibrate-percentile-ranks"
 - "mhcflurry-class1-select-allele-specific-models"
 - "mhcflurry-class1-select-pan-allele-models"
 - "mhcflurry-class1-select-processing-models"
 - "mhcflurry-class1-train-allele-specific-models"
 - "mhcflurry-class1-train-pan-allele-models"
 - "mhcflurry-class1-train-presentation-models"
 - "mhcflurry-class1-train-processing-models"
 - "mhcflurry-downloads"
 - "mhcflurry-predict"
 - "mhcflurry-predict-scan"
 - "pyjwt"
versions:
 - "2.0.1--pyh864c0ab_0"
description: "shpc-registry automated BioContainers addition for mhcflurry"
config: {"url": "https://biocontainers.pro/tools/mhcflurry", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mhcflurry", "latest": {"2.0.1--pyh864c0ab_0": "sha256:00f87fd3ce4d2c069d14c44822d6ef024dd55165a181cde57bbc96119ce4ee53"}, "tags": {"2.0.1--pyh864c0ab_0": "sha256:00f87fd3ce4d2c069d14c44822d6ef024dd55165a181cde57bbc96119ce4ee53"}, "docker": "quay.io/biocontainers/mhcflurry", "aliases": {"_mhcflurry-cluster-worker-entry-point": "/usr/local/bin/_mhcflurry-cluster-worker-entry-point", "mhcflurry-calibrate-percentile-ranks": "/usr/local/bin/mhcflurry-calibrate-percentile-ranks", "mhcflurry-class1-select-allele-specific-models": "/usr/local/bin/mhcflurry-class1-select-allele-specific-models", "mhcflurry-class1-select-pan-allele-models": "/usr/local/bin/mhcflurry-class1-select-pan-allele-models", "mhcflurry-class1-select-processing-models": "/usr/local/bin/mhcflurry-class1-select-processing-models", "mhcflurry-class1-train-allele-specific-models": "/usr/local/bin/mhcflurry-class1-train-allele-specific-models", "mhcflurry-class1-train-pan-allele-models": "/usr/local/bin/mhcflurry-class1-train-pan-allele-models", "mhcflurry-class1-train-presentation-models": "/usr/local/bin/mhcflurry-class1-train-presentation-models", "mhcflurry-class1-train-processing-models": "/usr/local/bin/mhcflurry-class1-train-processing-models", "mhcflurry-downloads": "/usr/local/bin/mhcflurry-downloads", "mhcflurry-predict": "/usr/local/bin/mhcflurry-predict", "mhcflurry-predict-scan": "/usr/local/bin/mhcflurry-predict-scan", "pyjwt": "/usr/local/bin/pyjwt"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mhcflurry.
shpc-registry automated BioContainers addition for mhcflurry
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mhcflurry
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mhcflurry:2.0.1--pyh864c0ab_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mhcflurry/2.0.1--pyh864c0ab_0
$ module help quay.io/biocontainers/mhcflurry/2.0.1--pyh864c0ab_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mhcflurry-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mhcflurry-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mhcflurry-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mhcflurry-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mhcflurry-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mhcflurry-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### _mhcflurry-cluster-worker-entry-point

```bash
$ singularity exec <container> /usr/local/bin/_mhcflurry-cluster-worker-entry-point
$ podman run --it --rm --entrypoint /usr/local/bin/_mhcflurry-cluster-worker-entry-point   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_mhcflurry-cluster-worker-entry-point   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mhcflurry-calibrate-percentile-ranks

```bash
$ singularity exec <container> /usr/local/bin/mhcflurry-calibrate-percentile-ranks
$ podman run --it --rm --entrypoint /usr/local/bin/mhcflurry-calibrate-percentile-ranks   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mhcflurry-calibrate-percentile-ranks   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mhcflurry-class1-select-allele-specific-models

```bash
$ singularity exec <container> /usr/local/bin/mhcflurry-class1-select-allele-specific-models
$ podman run --it --rm --entrypoint /usr/local/bin/mhcflurry-class1-select-allele-specific-models   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mhcflurry-class1-select-allele-specific-models   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mhcflurry-class1-select-pan-allele-models

```bash
$ singularity exec <container> /usr/local/bin/mhcflurry-class1-select-pan-allele-models
$ podman run --it --rm --entrypoint /usr/local/bin/mhcflurry-class1-select-pan-allele-models   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mhcflurry-class1-select-pan-allele-models   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mhcflurry-class1-select-processing-models

```bash
$ singularity exec <container> /usr/local/bin/mhcflurry-class1-select-processing-models
$ podman run --it --rm --entrypoint /usr/local/bin/mhcflurry-class1-select-processing-models   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mhcflurry-class1-select-processing-models   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mhcflurry-class1-train-allele-specific-models

```bash
$ singularity exec <container> /usr/local/bin/mhcflurry-class1-train-allele-specific-models
$ podman run --it --rm --entrypoint /usr/local/bin/mhcflurry-class1-train-allele-specific-models   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mhcflurry-class1-train-allele-specific-models   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mhcflurry-class1-train-pan-allele-models

```bash
$ singularity exec <container> /usr/local/bin/mhcflurry-class1-train-pan-allele-models
$ podman run --it --rm --entrypoint /usr/local/bin/mhcflurry-class1-train-pan-allele-models   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mhcflurry-class1-train-pan-allele-models   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mhcflurry-class1-train-presentation-models

```bash
$ singularity exec <container> /usr/local/bin/mhcflurry-class1-train-presentation-models
$ podman run --it --rm --entrypoint /usr/local/bin/mhcflurry-class1-train-presentation-models   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mhcflurry-class1-train-presentation-models   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mhcflurry-class1-train-processing-models

```bash
$ singularity exec <container> /usr/local/bin/mhcflurry-class1-train-processing-models
$ podman run --it --rm --entrypoint /usr/local/bin/mhcflurry-class1-train-processing-models   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mhcflurry-class1-train-processing-models   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mhcflurry-downloads

```bash
$ singularity exec <container> /usr/local/bin/mhcflurry-downloads
$ podman run --it --rm --entrypoint /usr/local/bin/mhcflurry-downloads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mhcflurry-downloads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mhcflurry-predict

```bash
$ singularity exec <container> /usr/local/bin/mhcflurry-predict
$ podman run --it --rm --entrypoint /usr/local/bin/mhcflurry-predict   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mhcflurry-predict   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mhcflurry-predict-scan

```bash
$ singularity exec <container> /usr/local/bin/mhcflurry-predict-scan
$ podman run --it --rm --entrypoint /usr/local/bin/mhcflurry-predict-scan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mhcflurry-predict-scan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyjwt

```bash
$ singularity exec <container> /usr/local/bin/pyjwt
$ podman run --it --rm --entrypoint /usr/local/bin/pyjwt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyjwt   -v ${PWD} -w ${PWD} <container> -c " $@"
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