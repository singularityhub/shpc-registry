---
layout: container
name:  "quay.io/biocontainers/macaron"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/macaron/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/macaron/container.yaml"
updated_at: "2023-06-30 03:12:13.483060"
latest: "1.0--pyh864c0ab_1"
container_url: "https://biocontainers.pro/tools/macaron"
aliases:
 - "MACARON"
 - "MACARON_validate"
 - "gatk"
 - "snpEff"
 - "extcheck"
 - "java-rmi.cgi"
 - "javah"
 - "jhat"
 - "jsadebugd"
 - "native2ascii"
 - "policytool"
 - "appletviewer"
versions:
 - "1.0--pyh864c0ab_1"
description: "shpc-registry automated BioContainers addition for macaron"
config: {"url": "https://biocontainers.pro/tools/macaron", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for macaron", "latest": {"1.0--pyh864c0ab_1": "sha256:a99862a78cb795988247ef4e2bdada2750d45294191f9277203c80b06d84bea6"}, "tags": {"1.0--pyh864c0ab_1": "sha256:a99862a78cb795988247ef4e2bdada2750d45294191f9277203c80b06d84bea6"}, "docker": "quay.io/biocontainers/macaron", "aliases": {"MACARON": "/usr/local/bin/MACARON", "MACARON_validate": "/usr/local/bin/MACARON_validate", "gatk": "/usr/local/bin/gatk", "snpEff": "/usr/local/bin/snpEff", "extcheck": "/usr/local/bin/extcheck", "java-rmi.cgi": "/usr/local/bin/java-rmi.cgi", "javah": "/usr/local/bin/javah", "jhat": "/usr/local/bin/jhat", "jsadebugd": "/usr/local/bin/jsadebugd", "native2ascii": "/usr/local/bin/native2ascii", "policytool": "/usr/local/bin/policytool", "appletviewer": "/usr/local/bin/appletviewer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/macaron.
shpc-registry automated BioContainers addition for macaron
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/macaron
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/macaron:1.0--pyh864c0ab_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/macaron/1.0--pyh864c0ab_1
$ module help quay.io/biocontainers/macaron/1.0--pyh864c0ab_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### macaron-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### macaron-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### macaron-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### macaron-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### macaron-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### macaron-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### MACARON

```bash
$ singularity exec <container> /usr/local/bin/MACARON
$ podman run --it --rm --entrypoint /usr/local/bin/MACARON   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MACARON   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MACARON_validate

```bash
$ singularity exec <container> /usr/local/bin/MACARON_validate
$ podman run --it --rm --entrypoint /usr/local/bin/MACARON_validate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MACARON_validate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gatk

```bash
$ singularity exec <container> /usr/local/bin/gatk
$ podman run --it --rm --entrypoint /usr/local/bin/gatk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gatk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snpEff

```bash
$ singularity exec <container> /usr/local/bin/snpEff
$ podman run --it --rm --entrypoint /usr/local/bin/snpEff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snpEff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extcheck

```bash
$ singularity exec <container> /usr/local/bin/extcheck
$ podman run --it --rm --entrypoint /usr/local/bin/extcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### java-rmi.cgi

```bash
$ singularity exec <container> /usr/local/bin/java-rmi.cgi
$ podman run --it --rm --entrypoint /usr/local/bin/java-rmi.cgi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/java-rmi.cgi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### javah

```bash
$ singularity exec <container> /usr/local/bin/javah
$ podman run --it --rm --entrypoint /usr/local/bin/javah   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/javah   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jhat

```bash
$ singularity exec <container> /usr/local/bin/jhat
$ podman run --it --rm --entrypoint /usr/local/bin/jhat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jhat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jsadebugd

```bash
$ singularity exec <container> /usr/local/bin/jsadebugd
$ podman run --it --rm --entrypoint /usr/local/bin/jsadebugd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jsadebugd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### native2ascii

```bash
$ singularity exec <container> /usr/local/bin/native2ascii
$ podman run --it --rm --entrypoint /usr/local/bin/native2ascii   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/native2ascii   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### policytool

```bash
$ singularity exec <container> /usr/local/bin/policytool
$ podman run --it --rm --entrypoint /usr/local/bin/policytool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/policytool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### appletviewer

```bash
$ singularity exec <container> /usr/local/bin/appletviewer
$ podman run --it --rm --entrypoint /usr/local/bin/appletviewer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/appletviewer   -v ${PWD} -w ${PWD} <container> -c " $@"
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