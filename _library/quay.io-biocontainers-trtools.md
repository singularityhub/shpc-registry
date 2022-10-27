---
layout: container
name:  "quay.io/biocontainers/trtools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/trtools/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/trtools/container.yaml"
updated_at: "2022-10-27 00:50:10.452608"
latest: "4.2.1--pyhb765511_0"
container_url: "https://biocontainers.pro/tools/trtools"
aliases:
 - "compareSTR"
 - "dumpSTR"
 - "mergeSTR"
 - "qcSTR"
 - "statSTR"
 - "test_trtools.sh"
 - "trtools_prep_beagle_vcf.sh"
versions:
 - "4.2.1--pyhb765511_0"
description: "shpc-registry automated BioContainers addition for trtools"
config: {"url": "https://biocontainers.pro/tools/trtools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for trtools", "latest": {"4.2.1--pyhb765511_0": "sha256:503e5b4beab6b212fdd777e59cc6f84b944d63665105b77d0e3374d8391d498a"}, "tags": {"4.2.1--pyhb765511_0": "sha256:503e5b4beab6b212fdd777e59cc6f84b944d63665105b77d0e3374d8391d498a"}, "docker": "quay.io/biocontainers/trtools", "aliases": {"compareSTR": "/usr/local/bin/compareSTR", "dumpSTR": "/usr/local/bin/dumpSTR", "mergeSTR": "/usr/local/bin/mergeSTR", "qcSTR": "/usr/local/bin/qcSTR", "statSTR": "/usr/local/bin/statSTR", "test_trtools.sh": "/usr/local/bin/test_trtools.sh", "trtools_prep_beagle_vcf.sh": "/usr/local/bin/trtools_prep_beagle_vcf.sh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/trtools.
shpc-registry automated BioContainers addition for trtools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/trtools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/trtools:4.2.1--pyhb765511_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/trtools/4.2.1--pyhb765511_0
$ module help quay.io/biocontainers/trtools/4.2.1--pyhb765511_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### trtools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### trtools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### trtools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### trtools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### trtools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### trtools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### compareSTR

```bash
$ singularity exec <container> /usr/local/bin/compareSTR
$ podman run --it --rm --entrypoint /usr/local/bin/compareSTR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compareSTR   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dumpSTR

```bash
$ singularity exec <container> /usr/local/bin/dumpSTR
$ podman run --it --rm --entrypoint /usr/local/bin/dumpSTR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dumpSTR   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mergeSTR

```bash
$ singularity exec <container> /usr/local/bin/mergeSTR
$ podman run --it --rm --entrypoint /usr/local/bin/mergeSTR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mergeSTR   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qcSTR

```bash
$ singularity exec <container> /usr/local/bin/qcSTR
$ podman run --it --rm --entrypoint /usr/local/bin/qcSTR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qcSTR   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### statSTR

```bash
$ singularity exec <container> /usr/local/bin/statSTR
$ podman run --it --rm --entrypoint /usr/local/bin/statSTR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/statSTR   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test_trtools.sh

```bash
$ singularity exec <container> /usr/local/bin/test_trtools.sh
$ podman run --it --rm --entrypoint /usr/local/bin/test_trtools.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test_trtools.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trtools_prep_beagle_vcf.sh

```bash
$ singularity exec <container> /usr/local/bin/trtools_prep_beagle_vcf.sh
$ podman run --it --rm --entrypoint /usr/local/bin/trtools_prep_beagle_vcf.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trtools_prep_beagle_vcf.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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