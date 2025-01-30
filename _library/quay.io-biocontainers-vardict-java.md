---
layout: container
name:  "quay.io/biocontainers/vardict-java"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/vardict-java/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/vardict-java/container.yaml"
updated_at: "2025-01-30 02:55:57.783027"
latest: "1.8.3--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/vardict-java"
aliases:
 - "testsomatic.R"
 - "teststrandbias.R"
 - "var2vcf_paired.pl"
 - "var2vcf_valid.pl"
 - "vardict-java"
 - "jaotc"
 - "jdeprscan"
 - "jhsdb"
 - "jimage"
 - "jlink"
 - "jmod"
 - "jshell"
 - "jjs"
 - "pack200"
 - "rmic"
versions:
 - "1.8.3--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for vardict-java"
config: {"url": "https://biocontainers.pro/tools/vardict-java", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for vardict-java", "latest": {"1.8.3--hdfd78af_0": "sha256:4069c082c97470bce4a07f228dbf74b6ea3fc5c4eaa93ba76d2826a496ca3c44"}, "tags": {"1.8.3--hdfd78af_0": "sha256:4069c082c97470bce4a07f228dbf74b6ea3fc5c4eaa93ba76d2826a496ca3c44"}, "docker": "quay.io/biocontainers/vardict-java", "aliases": {"testsomatic.R": "/usr/local/bin/testsomatic.R", "teststrandbias.R": "/usr/local/bin/teststrandbias.R", "var2vcf_paired.pl": "/usr/local/bin/var2vcf_paired.pl", "var2vcf_valid.pl": "/usr/local/bin/var2vcf_valid.pl", "vardict-java": "/usr/local/bin/vardict-java", "jaotc": "/usr/local/bin/jaotc", "jdeprscan": "/usr/local/bin/jdeprscan", "jhsdb": "/usr/local/bin/jhsdb", "jimage": "/usr/local/bin/jimage", "jlink": "/usr/local/bin/jlink", "jmod": "/usr/local/bin/jmod", "jshell": "/usr/local/bin/jshell", "jjs": "/usr/local/bin/jjs", "pack200": "/usr/local/bin/pack200", "rmic": "/usr/local/bin/rmic"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/vardict-java.
shpc-registry automated BioContainers addition for vardict-java
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/vardict-java
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/vardict-java:1.8.3--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/vardict-java/1.8.3--hdfd78af_0
$ module help quay.io/biocontainers/vardict-java/1.8.3--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### vardict-java-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### vardict-java-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### vardict-java-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### vardict-java-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### vardict-java-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### vardict-java-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### testsomatic.R

```bash
$ singularity exec <container> /usr/local/bin/testsomatic.R
$ podman run --it --rm --entrypoint /usr/local/bin/testsomatic.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/testsomatic.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### teststrandbias.R

```bash
$ singularity exec <container> /usr/local/bin/teststrandbias.R
$ podman run --it --rm --entrypoint /usr/local/bin/teststrandbias.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/teststrandbias.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### var2vcf_paired.pl

```bash
$ singularity exec <container> /usr/local/bin/var2vcf_paired.pl
$ podman run --it --rm --entrypoint /usr/local/bin/var2vcf_paired.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/var2vcf_paired.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### var2vcf_valid.pl

```bash
$ singularity exec <container> /usr/local/bin/var2vcf_valid.pl
$ podman run --it --rm --entrypoint /usr/local/bin/var2vcf_valid.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/var2vcf_valid.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vardict-java

```bash
$ singularity exec <container> /usr/local/bin/vardict-java
$ podman run --it --rm --entrypoint /usr/local/bin/vardict-java   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vardict-java   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jaotc

```bash
$ singularity exec <container> /usr/local/bin/jaotc
$ podman run --it --rm --entrypoint /usr/local/bin/jaotc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jaotc   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### jmod

```bash
$ singularity exec <container> /usr/local/bin/jmod
$ podman run --it --rm --entrypoint /usr/local/bin/jmod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jmod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jshell

```bash
$ singularity exec <container> /usr/local/bin/jshell
$ podman run --it --rm --entrypoint /usr/local/bin/jshell   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jshell   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jjs

```bash
$ singularity exec <container> /usr/local/bin/jjs
$ podman run --it --rm --entrypoint /usr/local/bin/jjs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jjs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pack200

```bash
$ singularity exec <container> /usr/local/bin/pack200
$ podman run --it --rm --entrypoint /usr/local/bin/pack200   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pack200   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rmic

```bash
$ singularity exec <container> /usr/local/bin/rmic
$ podman run --it --rm --entrypoint /usr/local/bin/rmic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rmic   -v ${PWD} -w ${PWD} <container> -c " $@"
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