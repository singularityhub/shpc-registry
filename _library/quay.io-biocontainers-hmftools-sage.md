---
layout: container
name:  "quay.io/biocontainers/hmftools-sage"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hmftools-sage/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hmftools-sage/container.yaml"
updated_at: "2024-08-24 02:43:51.561035"
latest: "3.4.4--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/hmftools-sage"
aliases:
 - "SAGE"
 - "cups-config"
 - "ippeveprinter"
 - "ipptool"
 - "jfr"
 - "jaotc"
 - "aserver"
 - "jdeprscan"
 - "jhsdb"
 - "jimage"
 - "jlink"
versions:
 - "3.1--hdfd78af_0"
 - "3.2.3--hdfd78af_0"
 - "3.4--hdfd78af_1"
 - "3.4.2--hdfd78af_0"
 - "3.4.3--hdfd78af_0"
 - "3.4.4--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for hmftools-sage"
config: {"url": "https://biocontainers.pro/tools/hmftools-sage", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hmftools-sage", "latest": {"3.4.4--hdfd78af_0": "sha256:f04ed632a1cbce61c26424dd4547533fdc3ff294165b3e3c0b25f8a72075b65e"}, "tags": {"3.1--hdfd78af_0": "sha256:3804df655d9ae7c37ba5ba816ca5a95446bdb3d7fcb0fc587a83618e167f3ce1", "3.2.3--hdfd78af_0": "sha256:9711d591611abea80ceb161042efc4f6684cd276eb416cbeb60bc3da10078ce3", "3.4--hdfd78af_1": "sha256:87ab9632273ebc30fbe2a32cfd4f25e6c16c80668a23f376d584f1f8d3688c34", "3.4.2--hdfd78af_0": "sha256:7f7612702c75074a5e542996a5c0d573edc8601768f3ee8658d586a3662a3d00", "3.4.3--hdfd78af_0": "sha256:606410e57eb5eece65ba77a098f6015808af209f5ff8f327ab0dda1ce0d716f0", "3.4.4--hdfd78af_0": "sha256:f04ed632a1cbce61c26424dd4547533fdc3ff294165b3e3c0b25f8a72075b65e"}, "docker": "quay.io/biocontainers/hmftools-sage", "aliases": {"SAGE": "/usr/local/bin/SAGE", "cups-config": "/usr/local/bin/cups-config", "ippeveprinter": "/usr/local/bin/ippeveprinter", "ipptool": "/usr/local/bin/ipptool", "jfr": "/usr/local/bin/jfr", "jaotc": "/usr/local/bin/jaotc", "aserver": "/usr/local/bin/aserver", "jdeprscan": "/usr/local/bin/jdeprscan", "jhsdb": "/usr/local/bin/jhsdb", "jimage": "/usr/local/bin/jimage", "jlink": "/usr/local/bin/jlink"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hmftools-sage.
shpc-registry automated BioContainers addition for hmftools-sage
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hmftools-sage
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hmftools-sage:3.4.4--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hmftools-sage/3.4.4--hdfd78af_0
$ module help quay.io/biocontainers/hmftools-sage/3.4.4--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hmftools-sage-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hmftools-sage-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hmftools-sage-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hmftools-sage-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hmftools-sage-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hmftools-sage-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### SAGE

```bash
$ singularity exec <container> /usr/local/bin/SAGE
$ podman run --it --rm --entrypoint /usr/local/bin/SAGE   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SAGE   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cups-config

```bash
$ singularity exec <container> /usr/local/bin/cups-config
$ podman run --it --rm --entrypoint /usr/local/bin/cups-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cups-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ippeveprinter

```bash
$ singularity exec <container> /usr/local/bin/ippeveprinter
$ podman run --it --rm --entrypoint /usr/local/bin/ippeveprinter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ippeveprinter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipptool

```bash
$ singularity exec <container> /usr/local/bin/ipptool
$ podman run --it --rm --entrypoint /usr/local/bin/ipptool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipptool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jfr

```bash
$ singularity exec <container> /usr/local/bin/jfr
$ podman run --it --rm --entrypoint /usr/local/bin/jfr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jfr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jaotc

```bash
$ singularity exec <container> /usr/local/bin/jaotc
$ podman run --it --rm --entrypoint /usr/local/bin/jaotc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jaotc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aserver

```bash
$ singularity exec <container> /usr/local/bin/aserver
$ podman run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jdeprscan

```bash
$ singularity exec <container> /usr/local/bin/jdeprscan
$ podman run --it --rm --entrypoint /usr/local/bin/jdeprscan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jdeprscan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jhsdb

```bash
$ singularity exec <container> /usr/local/bin/jhsdb
$ podman run --it --rm --entrypoint /usr/local/bin/jhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jimage

```bash
$ singularity exec <container> /usr/local/bin/jimage
$ podman run --it --rm --entrypoint /usr/local/bin/jimage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jimage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jlink

```bash
$ singularity exec <container> /usr/local/bin/jlink
$ podman run --it --rm --entrypoint /usr/local/bin/jlink   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jlink   -v ${PWD} -w ${PWD} <container> -c " $@"
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